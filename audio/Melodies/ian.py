import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import random
import time
import pyaudio
from Oscillators.sine_osc_patrick import SineOscPatrick

sine_osc = SineOscPatrick()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def one(freq, length, vol):
    sine_osc.play_frequencies(stream, length, vol, 8000, 5000,
                              random.choice([freq/3, freq * 1/2]),
                              freq / 2,
                              freq,
                              freq * 3/2 + 2,
                              random.choice([freq * 10/4]),
                              )


def three(freq, length, vol):
    sine_osc.play_frequencies(stream, length, vol, 2000, 2000,
                              random.choice([50, 65, 50, 70, 50, 68]),
                              freq / 2,
                              freq,
                              freq * 3,
                              )

def two(freq, length, vol):
    for j in range(2):
        one(freq, length, vol)
    for j in range(2):
        one(freq * 2, length, vol)
    melody = random.choice([120, 130, 140, 150])
    for j in range(6):
        one(melody, .2, vol)
        melody += random.choice([-2, -3])

if __name__ == '__main__':
    for k in range(4):
        freq = 100
        vol = 0
        for j in range(180):
            if j < 30:
                vol += .06
            three(freq, .05, vol)
            if j > 120:
                vol -= .03
            freq += random.choice([-10, 12, -9, 13, -8, 14])

        for i in range(6):
            two(206, 1, 1)

    time.sleep(.5)
