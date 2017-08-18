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


def patrick(freq, length, vol):
    vol = vol / 2
    sine_osc.play_frequencies(stream, length, vol * .8, 7000, 2000,
                              random.choice([50, 65, 50, 70, 50, 68]),
                              # freq / 3 * 2,
                              freq / 2,
                              freq,
                              freq * 3/2 + 2,
                              random.choice([freq * 7/4, freq * 10/4]),
                              random.choice([freq * 4/3, freq * 9/4]),
                              )


def patrick_2(freq, length, vol):
    vol = vol / 2

    sine_osc.play_frequencies(stream, length, vol, 7000, 1800,
                                  freq,
                                  freq * 3/2
                                  )


def patrick_3(freq, length, vol):
    vol = vol / 2

    sine_osc.play_frequencies(stream, length, vol, 400, 2000,
                              freq,
                              freq * 2,
                              freq /2,
                              freq * 3/2
                              )


def sound():
    vol = .03
    x = random.choice([4, 3, 2, 3, 4, 5, 4, 5]) * 2
    for i in range(x):
        sine_osc.play_frequencies(stream, random.choice([.05, .05, .06, .08]), vol, 400, 400,
                                  160,
                                  800,
                                  1100,
                                  1110,
                                  1125,
                                  1300,
                                  1325,
                                  2000,
                                  2010,
                                  2500,
                                  2505,
                                  2510,
                                  3100,
                                  3200,
                                  4000,
                                  4005,
                                  4500,
                                  4700,
                                  )
        vol += .14

for j in range(20):
    bass = 100

    for i in range(160):
        if bass < 100:
            bass = random.choice([150, 120, 100])
        if bass > 250:
            bass = 50
        vol = random.choice(
            [.2, .3, .4,
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
        bass += rand

    sound()

    for i in range(3):
        patrick_3(bass, random.choice([.16]), 0)

    time.sleep(.16 * 12)

    for i in range(4):
        patrick(bass, random.choice([.16]), 0)

time.sleep(.5)
