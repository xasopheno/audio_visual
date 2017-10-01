import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import random
import time
import pyaudio
from Oscillators.sine_osc import SineOsc

sine_osc = SineOsc()
sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def one(freq, length, vol):
    sine_osc.play_frequencies(stream, length, vol, 4000, 2000,
                              freq / 4,
                              freq / 4 + 5,
                              freq / 2 - 5,
                              freq / 2 + 3,
                              freq - 2,
                              freq * 2 + 2,
                              freq * 4,
                              random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 11/8]),
                              random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 3/2 / 2]),
                              random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 5/4 / 2]),
                              random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 5/4 / 2]),
                              random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 5/4 / 2]),
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
    tempo = .8
    vol = .5
    freq = 400
    one(freq, tempo * 1.1, vol)
    one(freq * 9/8, tempo * 2, vol)
    one(freq, tempo, vol)
    one(freq * 4/3, tempo * 2, vol)
    one(freq * 5/3, tempo * 2, vol)
    one(freq * 3/2, tempo, vol)
    one(freq * 5/4, tempo * 5, vol)
    time.sleep(tempo * 2)

    one(freq * 2, tempo * 3, vol)
    one(freq * 4/3, tempo * 1, vol)
    one(freq * 15/8, tempo * 2, vol)
    one(freq * 5/3, tempo * 2, vol)
    one(freq * 3/2, tempo * 3, vol)
    time.sleep(tempo * 1)

    time.sleep(tempo * 1)
    one(freq * 5/3, tempo * 1, vol)
    one(freq * 5/4, tempo * .65, vol)
    one(freq * 9/8, tempo * .3, vol)
    one(freq * 1, tempo * .6, vol)
    one(freq * 5/4, tempo * .37, vol)

    one(freq * 4/3, tempo * 1.5, vol)
    one(freq * 1, tempo * .5, vol)
    one(freq * 5/3, tempo * 1.5, vol)
    one(freq * 3/2, tempo * .28, vol)
    one(freq * 4/3, tempo * .22, vol)
    one(freq * 5/3, tempo * 1.5, vol)
    one(freq * 3/2, tempo * .27, vol)
    one(freq * 4/3, tempo * .23, vol)
    one(freq * 7/6, tempo * .5, vol)
    one(freq * 1, tempo * 1.5, vol)

    one(freq * 5/3, tempo * 1, vol)
    one(freq * 3/2, tempo * .5, vol)
    one(freq * 4/3, tempo * .5, vol)
    one(freq * 5/4, tempo * 1, vol)
    one(freq * 1, tempo * 4, vol)

    one(freq * 1, tempo * .5, vol)
    one(freq * 9/8, tempo * .5, vol)
    one(freq * 5/4, tempo * 1, vol)
    one(freq * 3/2, tempo * 1, vol)
    one(freq * 5/4, tempo * .5, vol)
    one(freq * 9/8, tempo * .5, vol)
    one(freq * 1, tempo * .5, vol)
    one(freq * 5/3 /2, tempo * .5, vol)
    one(freq * 3/2 /2, tempo * 1, vol)
    one(freq * 4/3, tempo * 1, vol)
    one(freq * 5/4, tempo * 1, vol)
    one(freq * 9/8, tempo * 1, vol)
    one(freq * 1, tempo * 4, vol)

    one(freq * 0, tempo * 4, vol)
