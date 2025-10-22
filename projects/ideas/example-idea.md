---
idea_id: "voice-interface-lifeos"
title: "Voice Interface for Morning Brief"
status: "considering"
priority: "medium"
effort: "M"
category: "lifeos-infra"
created: 2025-10-18
updated: 2025-10-18
value_proposition: "Hands-free access to daily brief while making coffee or walking dog"
tags:
  - automation
  - voice
  - morning-routine
  - accessibility
---

# Voice Interface for Morning Brief

## The Idea

Add voice interaction to the morning brief system so users can listen to their daily priorities, calendar, and insights while doing other morning activities (making coffee, getting dressed, walking the dog).

## Why This Matters

**Current Friction:**
- Morning brief requires sitting down and reading on screen
- Mornings are rushed - reading takes 5-10 minutes of focused time
- Mobile reading while multitasking is awkward

**Potential Value:**
- Hands-free consumption while doing morning routine
- Faster information absorption (listening while moving)
- More natural integration into existing habits
- Accessibility win (vision-impaired users)

## How It Could Work

### Approach 1: Simple TTS (Text-to-Speech)
- Generate morning brief markdown as usual
- Use ElevenLabs or OpenAI TTS to convert to audio
- Save as `.mp3` in `reflections/daily/briefs/`
- User plays audio file or auto-plays on phone

**Pros:**
- Simple implementation (API call to TTS service)
- Works offline after generation
- Can speed up/slow down playback

**Cons:**
- One-way communication only
- Requires manual trigger to generate

### Approach 2: Interactive Voice Assistant
- Real-time voice interface using Whisper (STT) + GPT-4 + TTS
- User can ask follow-up questions: "What time is my first meeting?" "Read my top priorities"
- Conversational interaction with Cabinet agents

**Pros:**
- More natural and flexible
- Can handle follow-ups and clarifications
- Feels like talking to Atlas/agents directly

**Cons:**
- More complex implementation
- Requires internet connection
- Higher latency and cost

### Approach 3: Hybrid
- Auto-generate TTS version of brief each morning
- Optional: Voice assistant mode for follow-up questions

## Implementation Sketch (Approach 1 - Simple TTS)

### Tech Stack
- **STT:** OpenAI Whisper API or Deepgram
- **TTS:** ElevenLabs (high quality) or OpenAI TTS (cheaper)
- **Integration:** Extend `morning_brief.py` script

### Pseudocode
```python
# In morning_brief.py

def generate_voice_brief(markdown_content: str, output_path: str):
    """Convert markdown brief to spoken audio."""

    # 1. Strip markdown formatting, keep content
    clean_text = strip_markdown(markdown_content)

    # 2. Optimize for speech (expand abbreviations, add pauses)
    speech_text = optimize_for_speech(clean_text)

    # 3. Call TTS API
    audio = elevenlabs.generate(
        text=speech_text,
        voice="Atlas",  # Custom cloned voice
        model="eleven_multilingual_v2"
    )

    # 4. Save as MP3
    audio.save(output_path)

    return output_path

# In main brief generation
if __name__ == "__main__":
    markdown_brief = generate_morning_brief()

    # Save markdown
    save_markdown(markdown_brief, "reflections/daily/briefs/2025-10-18.md")

    # Generate audio version
    audio_path = "reflections/daily/briefs/2025-10-18.mp3"
    generate_voice_brief(markdown_brief, audio_path)

    # Send notification with link to audio
    notify("Morning brief ready - listen now")
```

### Effort Estimate
- **Research & setup:** 2 hours (test TTS services, pick one)
- **Implementation:** 4 hours (extend Python script, markdown parsing, audio generation)
- **Voice customization:** 2 hours (clone voice for Atlas, test quality)
- **Testing & polish:** 2 hours (test on different content, edge cases)
- **Total:** ~10 hours (spread over 2-3 days)

## Open Questions

1. **Voice choice?**
   - Use generic TTS voice or clone a specific voice for Atlas?
   - Should different Cabinet agents have different voices?
   - ElevenLabs allows custom voice cloning - worth the cost?

2. **Delivery mechanism?**
   - Save as file and play manually?
   - Auto-play via iOS Shortcuts when alarm goes off?
   - Send to smart speaker (Alexa, Google Home)?

3. **Content optimization?**
   - Should we rewrite content specifically for speech?
   - How to handle lists, tables, code snippets?
   - Add natural pauses and emphasis?

4. **Privacy concerns?**
   - Audio files contain personal info - encryption needed?
   - TTS services may log content - local TTS better?
   - Calendar events with names/emails mentioned?

5. **Cost?**
   - ElevenLabs: ~$0.30 per 1000 characters (~$0.10 per brief)
   - OpenAI TTS: ~$0.015 per 1000 characters (~$0.05 per brief)
   - Worth the cost for daily use? (~$3-10/month)

## Success Criteria

**Minimum Viable Feature:**
- [ ] Morning brief auto-generates audio version
- [ ] Audio quality is clear and natural (not robotic)
- [ ] User can listen while doing other tasks
- [ ] Playback time is 3-5 minutes max

**Stretch Goals:**
- [ ] Custom voice for Atlas persona
- [ ] Auto-play on iPhone when alarm goes off
- [ ] Speed control (1.25x, 1.5x playback)
- [ ] Skip to sections ("skip to calendar")

## Why Not Do This?

**Reasons to reject/pause:**
- Morning brief text is already fast to scan (30 seconds)
- Voice adds complexity without major time savings
- Privacy risk if audio files not secured
- Cost could add up over time
- Reading allows selective focus, voice forces linear consumption

**Alternative solutions:**
- Just read the brief faster (skim mode)
- Use iOS built-in text-to-speech (free, works offline)
- Display brief on smart display instead (visual + voice)

## Next Steps If Pursuing

1. **Spike (2 hours):** Test ElevenLabs vs OpenAI TTS quality with sample brief
2. **Prototype (4 hours):** Extend Python script to generate audio
3. **User testing (1 week):** Use personally for 7 days, gather feedback
4. **Decide:** Ship, iterate, or shelve based on actual value

---

**Status:** Considering - needs user testing spike to validate value
**Related Ideas:** Voice assistant mode (#12), Smart speaker integration (#34)
**References:**
- ElevenLabs API docs: https://elevenlabs.io/docs
- OpenAI TTS docs: https://platform.openai.com/docs/guides/text-to-speech
