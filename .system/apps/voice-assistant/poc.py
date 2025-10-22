#!/usr/bin/env python3
"""
LifeOS Voice Assistant POC
Voice-activated Cabinet consultation system

Usage:
    python3 poc.py

Say "Hey Atlas" (or other agent names) and ask questions.
Press Ctrl+C to exit.
"""

import os
import sys
import time
import wave
import struct
import collections
import pyaudio
import pvporcupine
import webrtcvad
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

# Optional: ElevenLabs for better TTS
try:
    from elevenlabs.client import ElevenLabs
    from elevenlabs import play
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False

# Load environment variables
load_dotenv()

# Initialize API clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Audio settings
CHUNK = 320  # 20ms frames at 16kHz for webrtcvad compatibility (320/16000 = 0.02s)
SAMPLE_RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5

# LifeOS paths - go up two levels from voice-assistant to LifeOS root
LIFEOS_ROOT = Path(__file__).parent.parent.parent
AGENTS_DIR = LIFEOS_ROOT / "agents"
CONTEXT_DIR = LIFEOS_ROOT / "context"
WAKE_WORDS_DIR = Path(__file__).parent / "wake-words"

# Agent wake word mapping
AGENT_MAP = {
    "atlas": {"file": "atlas-operations.md", "name": "Atlas"},
    "banker": {"file": "banker.md", "name": "Banker"},
    "strategist": {"file": "strategist.md", "name": "Strategist"},
    "sage": {"file": "sage.md", "name": "Sage"},
    "commander": {"file": "commander.md", "name": "Commander"},
    "engineer": {"file": "engineer.md", "name": "Engineer"},
    "designer": {"file": "designer.md", "name": "Designer"},
    "artist": {"file": "artist.md", "name": "Artist"},
}

# Conversation history (persists during session)
conversation_history = []


def print_status(message, emoji="🔷"):
    """Print formatted status message"""
    print(f"\n{emoji} {message}")


def load_agent_prompt(agent_name):
    """Load agent system prompt from markdown file"""
    agent_file = AGENTS_DIR / AGENT_MAP[agent_name]["file"]

    if not agent_file.exists():
        print_status(f"Warning: Agent file not found: {agent_file}", "⚠️")
        return f"You are {AGENT_MAP[agent_name]['name']}, a helpful AI assistant."

    with open(agent_file, 'r') as f:
        content = f.read()
        # Extract content after frontmatter (if any)
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].strip()
        return content


def load_context():
    """Load relevant LifeOS context for agent"""
    context = {}

    for context_file in ["career.md", "wealth.md", "preferences.md"]:
        file_path = CONTEXT_DIR / context_file
        if file_path.exists():
            with open(file_path, 'r') as f:
                context[context_file.replace('.md', '')] = f.read()

    return context


def detect_wake_word():
    """Listen for wake word using Porcupine"""
    porcupine = None
    pa = None
    audio_stream = None

    try:
        # Initialize Porcupine with custom "Atlas" wake word
        atlas_wake_word_path = str(WAKE_WORDS_DIR / "atlas.ppn")

        porcupine = pvporcupine.create(
            access_key=os.getenv("PORCUPINE_ACCESS_KEY"),
            keyword_paths=[atlas_wake_word_path]
        )

        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print_status("Listening for 'Hey Atlas'...", "👂")

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print_status("Wake word detected!", "✅")
                return "atlas"  # Default to Atlas for POC

    except KeyboardInterrupt:
        print_status("Exiting...", "👋")
        sys.exit(0)
    finally:
        if audio_stream:
            audio_stream.close()
        if pa:
            pa.terminate()
        if porcupine:
            porcupine.delete()


def record_question(duration=RECORD_SECONDS):
    """Record audio question with voice activity detection"""
    print_status("Ask your question now! (stops when you stop talking)", "🎤")

    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    # Initialize voice activity detector
    vad = webrtcvad.Vad(1)  # Aggressiveness: 0-3 (1 is less aggressive, better for quiet speech)

    frames = []
    voiced_frames = []
    ring_buffer = collections.deque(maxlen=20)  # ~0.6 seconds of buffering
    triggered = False
    num_unvoiced = 0
    max_recording_time = 15  # Maximum 15 seconds
    start_time = time.time()

    while True:
        # Check if we've exceeded max recording time
        if time.time() - start_time > max_recording_time:
            print_status("Max recording time reached", "⏱️")
            break

        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

        # VAD requires 10, 20, or 30ms frames at 8kHz, 16kHz, or 32kHz
        # We're using 16kHz with CHUNK=512, which is 32ms
        is_speech = vad.is_speech(data, SAMPLE_RATE)

        if not triggered:
            # Waiting for speech to start
            ring_buffer.append((data, is_speech))
            num_voiced = len([f for f, speech in ring_buffer if speech])

            if num_voiced > 0.5 * ring_buffer.maxlen:
                triggered = True
                print_status("Speech detected...", "🗣️")
                # Add buffered audio
                for f, s in ring_buffer:
                    voiced_frames.append(f)
                ring_buffer.clear()
        else:
            # Currently recording speech
            voiced_frames.append(data)

            if not is_speech:
                num_unvoiced += 1
            else:
                num_unvoiced = 0

            # Stop if we have 1 second of silence
            if num_unvoiced > 30:  # ~1 second of silence
                print_status("Recording complete", "✅")
                break

    stream.stop_stream()
    stream.close()
    pa.terminate()

    # If no speech was detected, use all frames
    if not voiced_frames:
        print_status("No clear speech detected, using full recording", "⚠️")
        voiced_frames = frames

    # Save to temporary WAV file
    temp_audio = "/tmp/lifeos_question.wav"
    wf = wave.open(temp_audio, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b''.join(voiced_frames))
    wf.close()

    return temp_audio


def transcribe_audio(audio_file):
    """Transcribe audio to text using Whisper API"""
    print_status("Transcribing...", "🤔")

    try:
        with open(audio_file, 'rb') as f:
            transcript = openai_client.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )

        question = transcript.text.strip()

        # Check if transcription is empty or just silence
        if not question or len(question) < 2:
            print_status("No speech detected. Try again.", "⚠️")
            return None

        print_status(f"You asked: \"{question}\"", "💬")
        return question

    except Exception as e:
        print_status(f"Transcription error: {e}", "❌")
        return None


def ask_agent(agent_name, question):
    """Send question to Claude with agent persona and conversation history"""
    global conversation_history

    print_status(f"Asking {AGENT_MAP[agent_name]['name']}...", "🤔")

    # Load agent prompt and context
    agent_prompt = load_agent_prompt(agent_name)
    context = load_context()

    # Build context string
    context_str = "\n\n".join([f"# {k.upper()}\n{v}" for k, v in context.items()])

    # Prepare system message
    system_message = f"""{agent_prompt}

You have access to User's context:

{context_str}

Use this context to provide personalized, specific advice.

IMPORTANT: You are speaking via text-to-speech. Do not use markdown formatting (no asterisks, no bold, no headers). Speak naturally in plain text only. Use your wit and personality through word choice, not formatting."""

    # Build conversation messages with history
    messages = conversation_history + [{
        "role": "user",
        "content": question
    }]

    try:
        # Call Claude API
        response = anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=system_message,
            messages=messages
        )

        answer = response.content[0].text
        print_status(f"{AGENT_MAP[agent_name]['name']} responds:", "🗣️")
        print(f"\n{answer}\n")

        # Add to conversation history
        conversation_history.append({"role": "user", "content": question})
        conversation_history.append({"role": "assistant", "content": answer})

        # Keep history reasonable (last 10 exchanges = 20 messages)
        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]

        return answer

    except Exception as e:
        print_status(f"Agent error: {e}", "❌")
        return None


def speak(text, agent_name="atlas"):
    """Convert text to speech using ElevenLabs or macOS say command"""
    print_status("Speaking response...", "🔊")

    # Strip markdown formatting for cleaner TTS
    import re

    # Remove bold/italic markers
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)  # ***text***
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)      # **text**
    text = re.sub(r'\*(.+?)\*', r'\1', text)          # *text*
    text = re.sub(r'_(.+?)_', r'\1', text)            # _text_

    # Remove links but keep text: [text](url) -> text
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)

    # Remove code blocks
    text = re.sub(r'`(.+?)`', r'\1', text)

    # Remove headers
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)

    # Try ElevenLabs first if available and configured
    if ELEVENLABS_AVAILABLE and os.getenv("ELEVENLABS_API_KEY"):
        try:
            # Voice IDs - Custom voice clones from ElevenLabs
            # Default voice
            voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel (default)

            # Agent-specific voices
            agent_voices = {
                "atlas": "63sBmV7S2RAUbcLcDUeW",  # Tyrion Lannister voice clone
                "banker": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Banker voice
                "strategist": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Strategist voice
            }

            voice_id = agent_voices.get(agent_name, voice_id)

            client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

            # Generate and play audio
            audio_generator = client.generate(
                text=text,
                voice=voice_id,
                model="eleven_turbo_v2"  # Faster model
            )
            play(audio_generator)
            return

        except Exception as e:
            print_status(f"ElevenLabs error (falling back to macOS say): {e}", "⚠️")

    # Fallback to macOS say command
    # Escape quotes for shell command
    text = text.replace('"', '\\"')

    # Use macOS say command with Daniel (British voice for Atlas/Tyrion)
    # Options: Alex (US male), Daniel (GB male), Samantha (US female), Fred (deeper US)
    os.system(f'say -v Daniel -r 180 "{text}"')


def main():
    """Main voice assistant loop"""
    print("=" * 60)
    print("  LIFEOS VOICE ASSISTANT POC")
    print("  Voice-Activated Cabinet Consultation")
    print("=" * 60)
    print("\nPress Ctrl+C to exit\n")

    # Check API keys
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in .env")
        sys.exit(1)
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ Error: ANTHROPIC_API_KEY not found in .env")
        sys.exit(1)
    if not os.getenv("PORCUPINE_ACCESS_KEY"):
        print("❌ Error: PORCUPINE_ACCESS_KEY not found in .env")
        sys.exit(1)

    print_status("All API keys loaded ✓", "✅")
    print_status(f"Agents directory: {AGENTS_DIR}", "📁")
    print_status(f"Context directory: {CONTEXT_DIR}", "📁")

    while True:
        try:
            # 1. Wait for wake word
            agent_name = detect_wake_word()

            # 2. Record question
            audio_file = record_question()

            # 3. Transcribe to text
            question = transcribe_audio(audio_file)

            # Skip if no valid transcription
            if not question:
                print_status("Ready for next question...", "👂")
                continue

            # 4. Get agent response
            answer = ask_agent(agent_name, question)

            # Skip if no answer
            if not answer:
                print_status("No response from agent. Try again.", "⚠️")
                print_status("Ready for next question...", "👂")
                continue

            # 5. Speak response
            speak(answer, agent_name)

            print_status("Ready for next question...", "👂")

        except KeyboardInterrupt:
            print_status("\nShutting down voice assistant. Goodbye!", "👋")
            break
        except Exception as e:
            print_status(f"Unexpected error: {e}", "❌")
            print_status("Continuing to listen...", "👂")


if __name__ == "__main__":
    main()
