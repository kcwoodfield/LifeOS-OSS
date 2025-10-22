"""
Configuration settings for LifeOS Voice Assistant
All constants, paths, and API configuration
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
PORCUPINE_ACCESS_KEY = os.getenv("PORCUPINE_ACCESS_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Audio settings
CHUNK = 320  # 20ms frames at 16kHz for webrtcvad compatibility
SAMPLE_RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5
MAX_RECORDING_TIME = 15  # Maximum recording duration in seconds

# Voice Activity Detection
VAD_AGGRESSIVENESS = 1  # 0-3 (lower = less aggressive, better for quiet speech)
VAD_RING_BUFFER_SIZE = 20  # ~0.6 seconds of buffering
VAD_SILENCE_THRESHOLD = 30  # ~1 second of silence to stop recording

# LifeOS paths - go up from .system/apps/voice-assistant/ to LifeOS root, then into .system/
LIFEOS_ROOT = Path(__file__).parent.parent.parent.parent
AGENTS_DIR = LIFEOS_ROOT / ".system" / "agents"
CONTEXT_DIR = LIFEOS_ROOT / ".system" / "context"
WAKE_WORDS_DIR = Path(__file__).parent.parent / "wake-words"

# Temporary audio file location
TEMP_AUDIO_FILE = "/tmp/lifeos_question.wav"

# Claude API settings
CLAUDE_MODEL = "claude-sonnet-4-20250514"
CLAUDE_MAX_TOKENS = 1024
CONVERSATION_HISTORY_LIMIT = 20  # Keep last 10 exchanges (20 messages)

# ElevenLabs settings
ELEVENLABS_MODEL = "eleven_turbo_v2"

# TTS settings
MACOS_VOICE = "Daniel"  # British voice for fallback
MACOS_SPEECH_RATE = 180  # Words per minute
