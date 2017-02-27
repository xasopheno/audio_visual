import pyaudio
import random
from Oscillators.Generator import Generator
import time

osc = Generator()

def bass_drum():
    frequency = 50
    volume = .25
    for i in range(100):
        frequency = random.choice([45, 47, 50, 52, 53])

        waveform = osc.play_frequencies(
            .4,
            random.choice([1, 1.5, .5]),
            400,
            15000,
            frequency,
        )

        stream.write(waveform)
        time.sleep(.5)

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

bass_drum()




