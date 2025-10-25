# LifeOS Voice Assistant

Voice-activated interface to the Cabinet system. Say "Hey Atlas" and talk to your AI advisors.

## Quick Start

### 1. Install Dependencies

```bash
cd /Users/kcw/Sites/LifeOS/LifeOS/.system/apps/voice-assistant
pip3 install -r requirements.txt
```

### 2. Set Up API Keys

```bash
# Copy template
cp .env.template .env

# Edit .env and add your actual API keys
# - OpenAI: https://platform.openai.com/api-keys
# - Anthropic: https://console.anthropic.com/settings/keys
# - Porcupine: https://console.picovoice.ai/
# - ElevenLabs: https://elevenlabs.io/app/settings/api-keys
```

### 3. Test Microphone

```bash
python3 -c "import pyaudio; p=pyaudio.PyAudio(); print('Mic working!' if p.get_device_count() > 0 else 'No mic found')"
```

### 4. Run Voice Assistant

**Modular Version (Recommended):**
```bash
python3 main.py
```

**POC Version (Original single-file):**
```bash
python3 poc.py
```

Say "Hey Atlas" and then ask a question!

## Architecture

**Modular design for production readiness:**

```
voice-assistant/
├── main.py              # Main entry point (use this!)
├── poc.py               # Original POC (kept for reference)
├── config/              # Configuration and settings
│   ├── settings.py      # All constants, API keys, paths
│   └── agents.py        # Agent definitions and wake words
├── core/                # Core functionality
│   ├── wake_word.py     # Porcupine wake word detection
│   ├── audio.py         # Voice activity detection + recording
│   ├── speech.py        # STT (Whisper) + TTS (ElevenLabs)
│   └── conversation.py  # Conversation history management
├── agents/              # Agent management
│   ├── loader.py        # Load agent prompts from markdown
│   ├── router.py        # Route questions to agents
│   └── claude_client.py # Claude API integration
└── utils/               # Utilities
    └── ui.py            # Status printing and UI helpers
```

**Flow:**
```
Voice Input → Wake Word Detector → Audio Recorder (VAD) →
Speech-to-Text (Whisper) → Agent Router → Claude Client →
Text-to-Speech (ElevenLabs) → Speaker Output
```

**For detailed architecture documentation, see:**
`/Users/kcw/Sites/LifeOS/LifeOS/writing/documentation/voice-assistant-architecture.md`

## Troubleshooting

**pyaudio won't install:**
```bash
brew install portaudio
pip3 install pyaudio
```

**Microphone not working:**
- Check System Preferences → Security & Privacy → Microphone
- Grant Terminal/Python microphone access

**Wake word not detecting:**
- Speak clearly and louder
- Reduce background noise
- Adjust sensitivity in poc.py

## Cost

- Whisper API: ~$0.01 per question
- Claude API: ~$0.05 per question
- Porcupine: Free (up to 3 wake words)
- **Total: ~$5/month for regular use**

## Features

- ✅ Wake word detection (Porcupine - local, privacy-friendly)
- ✅ Voice activity detection (auto-stops when you stop talking)
- ✅ Speech-to-text (OpenAI Whisper API)
- ✅ Agent consultation (Claude API with full Cabinet context)
- ✅ Text-to-speech (ElevenLabs with voice cloning + macOS fallback)
- ✅ Conversation history (remembers last 10 exchanges)
- ✅ Error handling (graceful failures, always recovers)
- ✅ Modular architecture (production-ready)

## Roadmap

### Phase 2: Multi-Agent (Next)
- [ ] Multiple wake words (Banker, Strategist, Sage, Spartan, etc.)
- [ ] Agent-specific voice clones
- [ ] Better wake word → agent routing

### Phase 3: Advanced Features
- [ ] Multi-agent consultation ("Convene the Cabinet")
- [ ] Conversation logging to daily reviews
- [ ] Calendar integration
- [ ] Task creation via voice

### Phase 4: Production Deployment
- [ ] Background service (macOS LaunchDaemon)
- [ ] Dedicated hardware (Raspberry Pi + mic array)
- [ ] Multi-room deployment (M5Stack units)
