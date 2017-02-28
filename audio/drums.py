import pyaudio
import random
from Oscillators.Generator import Generator
import time


osc = Generator()

def bass_drum():
    for i in range(10):
        frequency = random.choice([31.75, 32, 31, 31.5, 30.75])

        waveform = osc.play_frequencies(
            random.choice([.6, .6, .6]),
            random.choice([1, 1, 1.25, .75]),
            frequency,
            frequency + .1,
            )

        stream.write(waveform)
if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

bass_drum()




