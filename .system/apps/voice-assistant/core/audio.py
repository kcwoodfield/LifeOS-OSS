"""
Audio recording with voice activity detection
Captures user speech and saves to WAV file
"""
import time
import wave
import collections
import pyaudio
import webrtcvad
from config.settings import (
    CHUNK, SAMPLE_RATE, CHANNELS, TEMP_AUDIO_FILE,
    MAX_RECORDING_TIME, VAD_AGGRESSIVENESS,
    VAD_RING_BUFFER_SIZE, VAD_SILENCE_THRESHOLD
)
from utils import print_status


class AudioRecorder:
    """Records audio with voice activity detection"""

    def __init__(self):
        self.vad = webrtcvad.Vad(VAD_AGGRESSIVENESS)

    def record(self):
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

        frames = []
        voiced_frames = []
        ring_buffer = collections.deque(maxlen=VAD_RING_BUFFER_SIZE)
        triggered = False
        num_unvoiced = 0
        start_time = time.time()

        while True:
            # Check if we've exceeded max recording time
            if time.time() - start_time > MAX_RECORDING_TIME:
                print_status("Max recording time reached", "⏱️")
                break

            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)

            # Detect speech in this frame
            is_speech = self.vad.is_speech(data, SAMPLE_RATE)

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

                # Stop if we have enough silence
                if num_unvoiced > VAD_SILENCE_THRESHOLD:
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
        self._save_wav(voiced_frames, pa)

        return TEMP_AUDIO_FILE

    def _save_wav(self, frames, pa):
        """Save audio frames to WAV file"""
        wf = wave.open(TEMP_AUDIO_FILE, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
