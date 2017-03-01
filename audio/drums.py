import pyaudio
import random
from Oscillators.Generator import Generator
import time


osc = Generator()


def bass_drum():
    frequency = random.choice([24, 25.5, 27., 28.5, 30, 26, 34, 38, 50, 54, 44, 48])

    waveform = osc.play_frequencies(
        random.choice([.55]) / 1.3,
        random.choice([1, 1, 1.25, .75]),
        frequency,
        frequency - random.choice([.1, .3]),
        frequency + .1,
        frequency,
        frequency,
        frequency,
        )

    stream.write(waveform)


def snare():
    frequency = random.choice([80, 100, 115, 120, 82, 102, 116, 119])

    waveform = osc.play_frequencies(
        random.choice([.373, .361, .37]) / 1.3,
        frequency,
        frequency + .1,
        frequency, - 5,
        frequency, -100,
        )

    stream.write(waveform)


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

for i in range(10000):
    bass_drum()
    snare()
time.sleep(1)




