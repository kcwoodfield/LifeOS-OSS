"""
Wake word detection using Porcupine
Listens for agent wake words and returns which agent was invoked
"""
import sys
import struct
import pyaudio
import pvporcupine
from config.settings import PORCUPINE_ACCESS_KEY, WAKE_WORDS_DIR
from config.agents import DEFAULT_AGENT
from utils import print_status


class WakeWordDetector:
    """Detects wake words using Porcupine"""

    def __init__(self):
        self.porcupine = None
        self.pa = None
        self.audio_stream = None

    def listen(self):
        """Listen for wake word and return detected agent name"""
        try:
            # Initialize Porcupine with custom "Atlas" wake word
            atlas_wake_word_path = str(WAKE_WORDS_DIR / "atlas.ppn")

            self.porcupine = pvporcupine.create(
                access_key=PORCUPINE_ACCESS_KEY,
                keyword_paths=[atlas_wake_word_path]
            )

            self.pa = pyaudio.PyAudio()
            self.audio_stream = self.pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length
            )

            print_status("Listening for 'Hey Atlas'...", "👂")

            while True:
                pcm = self.audio_stream.read(
                    self.porcupine.frame_length,
                    exception_on_overflow=False
                )
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

                keyword_index = self.porcupine.process(pcm)

                if keyword_index >= 0:
                    print_status("Wake word detected!", "✅")
                    return DEFAULT_AGENT  # For now, always return Atlas

        except KeyboardInterrupt:
            print_status("Exiting...", "👋")
            sys.exit(0)
        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up audio resources"""
        if self.audio_stream:
            self.audio_stream.close()
        if self.pa:
            self.pa.terminate()
        if self.porcupine:
            self.porcupine.delete()
