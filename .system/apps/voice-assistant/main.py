#!/usr/bin/env python3
"""
LifeOS Voice Assistant
Voice-activated Cabinet consultation system

Usage:
    python3 main.py

Say "Hey Atlas" (or other agent names) and ask questions.
Press Ctrl+C to exit.
"""
import sys
from config.settings import (
    OPENAI_API_KEY, ANTHROPIC_API_KEY, PORCUPINE_ACCESS_KEY,
    AGENTS_DIR, CONTEXT_DIR
)
from core import (
    AudioRecorder, WakeWordDetector,
    SpeechToText, TextToSpeech, ConversationHistory
)
from agents import AgentRouter, ClaudeClient
from utils import print_status


def check_api_keys():
    """Verify all required API keys are present"""
    if not OPENAI_API_KEY:
        print("❌ Error: OPENAI_API_KEY not found in .env")
        sys.exit(1)
    if not ANTHROPIC_API_KEY:
        print("❌ Error: ANTHROPIC_API_KEY not found in .env")
        sys.exit(1)
    if not PORCUPINE_ACCESS_KEY:
        print("❌ Error: PORCUPINE_ACCESS_KEY not found in .env")
        sys.exit(1)

    print_status("All API keys loaded ✓", "✅")
    print_status(f"Agents directory: {AGENTS_DIR}", "📁")
    print_status(f"Context directory: {CONTEXT_DIR}", "📁")


def main():
    """Main voice assistant loop"""
    print("=" * 60)
    print("  LIFEOS VOICE ASSISTANT")
    print("  Voice-Activated Cabinet Consultation")
    print("=" * 60)
    print("\nPress Ctrl+C to exit\n")

    # Check configuration
    check_api_keys()

    # Initialize components
    wake_word_detector = WakeWordDetector()
    audio_recorder = AudioRecorder()
    speech_to_text = SpeechToText()
    text_to_speech = TextToSpeech()
    claude_client = ClaudeClient()
    conversation = ConversationHistory()

    while True:
        try:
            # 1. Wait for wake word
            agent_name = wake_word_detector.listen()

            # 2. Record question
            audio_file = audio_recorder.record()

            # 3. Transcribe to text
            question = speech_to_text.transcribe(audio_file)

            # Skip if no valid transcription
            if not question:
                print_status("Ready for next question...", "👂")
                continue

            # 4. Get agent response
            answer = claude_client.ask_agent(agent_name, question, conversation)

            # Skip if no answer
            if not answer:
                print_status("No response from agent. Try again.", "⚠️")
                print_status("Ready for next question...", "👂")
                continue

            # 5. Add to conversation history
            conversation.add_exchange(question, answer)

            # 6. Speak response
            text_to_speech.speak(answer, agent_name)

            print_status("Ready for next question...", "👂")

        except KeyboardInterrupt:
            print_status("\nShutting down voice assistant. Goodbye!", "👋")
            break
        except Exception as e:
            print_status(f"Unexpected error: {e}", "❌")
            print_status("Continuing to listen...", "👂")


if __name__ == "__main__":
    main()
