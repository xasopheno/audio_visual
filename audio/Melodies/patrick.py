import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import random
import time
import pyaudio
from Oscillators.sine_osc import SineOsc

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def patrick(freq, length, vol):
    sine_osc.play_frequencies(stream, length, vol, 5000, 2000,
                              random.choice([50, 65, 50, 70, 50, 68]),
                              # freq / 3 * 2,
                              freq / 2,
                              freq,
                              freq * 3/2 + 2,
                              random.choice([freq * 7/4, freq * 10/4]),
                              random.choice([freq * 4/3, freq * 9/4]),
                              )


def patrick_2(freq, length, vol):
    sine_osc.play_frequencies(stream, length, vol, 2000, 2000,
                              freq,
                              freq * 3/2
                              )


for j in range(2):

    for i in range(80):
        vol = random.choice([.5, .3, 0, .4, .5, .5, .5, 0, 0])
        freq = random.randint(300, 360)
        patrick(freq, random.choice([.3, .6]), vol / 2)

    bass = 200
    for i in range(200):
        if bass < 50:
            bass = 150
        if bass > 250:
            bass = 50
        vol = random.choice(
            [ .2, .2, .3, .4,
             .5, .5, .5,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) * 3
        x = random.choice(
            [1, 1,
             2, 2, 2,
             3, 3, 3, 3])
        if x == 1:
            patrick(bass, random.choice([.16]), vol / 2)
        elif x == 2 :
            patrick_3(50, .16, vol * .2)
        else:
            patrick_2(random.choice([70, 60]), .16, vol)

        rand = random.choice(
            [1, 10, 25, 30,
             -1, -20, -30, -50, -50, -60, -80, -110])
        vol = random.choice([.5, .3, .4, .5, .5, .5, 0, 0])
        patrick_2(bass, random.choice([.16]), vol)
        rand = random.choice([4, 5, 8, 30, -20, -30, -50,])
        bass += rand

# for k in range(50):
#     bass = 200
#     for i in range(20):
#         if bass < 50:
#             bass = 150
#         if bass > 250:
#             bass = 50
#         vol = random.choice([.5, .3, .4, .5, .5, .5, 0, 0])
#         patrick_2(bass, random.choice([.16]), vol)
#         rand = random.choice([4, 5, 8, 30, -20, -30, -50,])
#         bass += rand
#
#     for i in range(8):
#         vol = random.choice([.5, .3, 0, .4, .5, .5, .5, 0, 0])
#         freq = random.randint(300, 360)
#         patrick(freq, random.choice([.3, .6]), vol /2)
#
#     bass = 200


time.sleep(.5)
