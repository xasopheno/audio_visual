import pyaudio
import random
from Oscillators.Generator import Generator
import time


osc = Generator()


class Drummer:
    def __init__(self):
        self.tempo = 1.2

    def bass_drum(self):
        frequency = random.choice([24, 25.5, 27., 28.5, 30, 26, 34, 38, 50, 54, 44, 48])
        waveform = osc.play_frequencies(
                random.choice([.55,]) / self.tempo,
                random.choice([1, 1, 1.25, .75]),
                frequency,
                frequency - random.choice([.1, .3]),
                frequency + .1,
                frequency,
                frequency,
                frequency,
                )

        stream.write(waveform)

    def snare(self):
        frequency = random.choice([80, 100, 115, 120, 82, 102, 116, 119])
        waveform = osc.play_frequencies(
            random.choice([.37, .37, .37, .37, .371, .369]) / self.tempo,
            frequency,
            frequency + .1,
            frequency, - 5,
            frequency, -100,
            )

        stream.write(waveform)


class Drummer2:
    def __init__(self):
        self.tempo = 1.2

    def bass_drum(self):
        frequency = random.choice([34, 38, 50, 54, 44, 48 ])
        waveform = osc.play_frequencies(
            random.choice([.55,]) / self.tempo,
            random.choice([1, 1, 1.25, .75]),
            frequency,
            frequency - random.choice([.1, .3]),
            frequency + .1,
            frequency,
            frequency,
            frequency,
            )

        stream.write(waveform)

    def snare(self):
        frequency = random.choice([128, 128, 152])
        waveform = osc.play_frequencies(
            random.choice([.37]) / self.tempo,
            frequency,
            frequency + .1,
            frequency + .1,
            frequency * 2/3,
            )

        stream.write(waveform)

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

drummer = Drummer()
drummer2 = Drummer2()

for i in range(100):
    for i in range(22):
        drummer.bass_drum()
        drummer.snare()
    for i in range(3):
        drummer2.bass_drum()
        drummer2.snare()

time.sleep(1)




