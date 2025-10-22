"""
Speech-to-text and text-to-speech services
Whisper for STT, ElevenLabs + macOS say for TTS
"""
import os
import re
from openai import OpenAI
from config.settings import (
    OPENAI_API_KEY, ELEVENLABS_API_KEY,
    MACOS_VOICE, MACOS_SPEECH_RATE, ELEVENLABS_MODEL
)
from config.agents import AGENT_MAP
from utils import print_status

# Optional: ElevenLabs for better TTS
try:
    from elevenlabs.client import ElevenLabs
    from elevenlabs import play
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False


class SpeechToText:
    """Converts audio to text using OpenAI Whisper"""

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def transcribe(self, audio_file):
        """Transcribe audio file to text"""
        print_status("Transcribing...", "🤔")

        try:
            with open(audio_file, 'rb') as f:
                transcript = self.client.audio.transcriptions.create(
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


class TextToSpeech:
    """Converts text to speech using ElevenLabs or macOS say"""

    def __init__(self):
        self.elevenlabs_client = None
        if ELEVENLABS_AVAILABLE and ELEVENLABS_API_KEY:
            self.elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    def speak(self, text, agent_name="atlas"):
        """Convert text to speech"""
        print_status("Speaking response...", "🔊")

        # Clean markdown formatting from text
        text = self._clean_markdown(text)

        # Try ElevenLabs first if available
        if self.elevenlabs_client:
            try:
                voice_id = AGENT_MAP.get(agent_name, {}).get(
                    "voice_id",
                    "21m00Tcm4TlvDq8ikWAM"  # Default voice
                )

                audio_generator = self.elevenlabs_client.generate(
                    text=text,
                    voice=voice_id,
                    model=ELEVENLABS_MODEL
                )
                play(audio_generator)
                return

            except Exception as e:
                print_status(
                    f"ElevenLabs error (falling back to macOS say): {e}",
                    "⚠️"
                )

        # Fallback to macOS say command
        self._macos_say(text)

    def _clean_markdown(self, text):
        """Remove markdown formatting for cleaner TTS"""
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

        return text

    def _macos_say(self, text):
        """Speak using macOS say command"""
        # Escape quotes for shell command
        text = text.replace('"', '\\"')
        os.system(f'say -v {MACOS_VOICE} -r {MACOS_SPEECH_RATE} "{text}"')
