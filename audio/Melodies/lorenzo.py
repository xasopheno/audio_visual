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


def one(freq, length, vol, subdivision=1):
    for i in range(subdivision):
        sine_osc.play_frequencies(stream, (length / subdivision) * .95, vol * random.choice([.4, .5, .6, .7, .8, .9, 1, 1 ,1]), 1000, 1000,
                                  freq / 4,
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
                                  random.choice([freq * 5/4 * 2, freq * 8/7 * 2, freq * 9/8 * 2, freq * 3/4 * 2, freq * 3/2 * 2, freq * 5/4 * 2]),
                                  random.choice([freq * 5/4 * 2, freq * 8/7 * 2, freq * 9/8 * 2, freq * 3/4 * 2, freq * 3/2 * 2, freq * 5/4 * 2]),
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
    freq = 392
    one(freq, tempo * 0.8, vol, 10)
    one(freq * 9/8, tempo * 2.2, vol, 20)
    one(freq, tempo, vol, 8)
    one(freq * 4/3, tempo * 2, vol, 20)
    one(freq * 5/3, tempo * 2, vol, 20)
    one(freq * 3/2, tempo, vol, 15)
    one(freq * 5/4, tempo * 5, vol, 50)
    time.sleep(tempo * 2)

    one(freq * 2, tempo * 3, vol, 20)
    one(freq * 4/3, tempo * 1, vol, 8)
    one(freq * 15/8, tempo * 2, vol, 20)
    one(freq * 5/3, tempo * 2, vol, 20)
    one(freq * 3/2, tempo * 3, vol, 20)
    time.sleep(tempo * 1)

    time.sleep(tempo * 1)
    one(freq * 5/3, tempo * 1, vol, 8)
    one(freq * 5/4, tempo * .65, vol, 6)
    one(freq * 9/8, tempo * .3, vol)
    one(freq * 1, tempo * .6, vol, 6)
    one(freq * 5/4, tempo * .37, vol, 6)

    one(freq * 4/3, tempo * 1.5, vol, 14)
    one(freq * 1, tempo * .5, vol, 5)
    one(freq * 5/3, tempo * 1.5, vol, 13)
    one(freq * 3/2, tempo * .28, vol)
    one(freq * 4/3, tempo * .22, vol, 5)
    one(freq * 5/3, tempo * 1.5, vol, 17)
    one(freq * 3/2, tempo * .27, vol, 5)
    one(freq * 4/3, tempo * .23, vol, 5)
    one(freq * 7/6, tempo * .5, vol, 9)
    one(freq * 1, tempo * 1.5, vol, 18)

    one(freq * 5/3, tempo * 1, vol, 13)
    one(freq * 3/2, tempo * .5, vol, 6)
    one(freq * 4/3, tempo * .5, vol, 14)
    one(freq * 5/4, tempo * .75, vol, 9)
    time.sleep(.25)
    one(freq * 1, tempo * 4, vol, 35)

    one(freq * 1, tempo * .5, vol, 10)
    one(freq * 9/8, tempo * .5, vol, 12)
    one(freq * 5/4, tempo * 1, vol, 16)
    one(freq * 3/2, tempo * 1, vol, 15)
    one(freq * 5/4, tempo * .5, vol, 6)
    one(freq * 9/8, tempo * .5, vol, 7)
    one(freq * 1, tempo * .5, vol, 8)
    one(freq * 5/3 /2, tempo * .5, vol, 9)
    one(freq * 3/2 /2, tempo * 1, vol, 10)
    one(freq * 4/3, tempo * 1, vol, 15)
    one(freq * 5/4, tempo * 1, vol, 10)
    one(freq * 9/8, tempo * 1, vol, 8)

    freq = freq - (freq * 9/8)
    freq = freq * 3/2

    one(freq * 1, tempo * 4, vol, 11)
    one(freq * 4/3, tempo * 5, vol, 14)
    one(freq * 3/2, tempo * 4, vol, 13)
    one(freq * 1, tempo * 4, vol, 11)
    print('a')
    one(freq * 1, tempo * 6, vol, 14)
    one(freq * 4/3, tempo * 5, vol, 14)
    one(freq * 1, tempo * 7, vol, 23)

    print('b')
    one(freq * 4/3, tempo * 7, vol, 18)
    one(freq * 1, tempo * 9, vol, 24)

    print('c')
    one(freq * 4/3, tempo * 7, vol, 18)
    one(freq * 4/3, tempo * 7, vol, 22)
    one(freq * 1, tempo * 6, vol, 23)
    one(freq * 1, tempo * 4, vol, 19)
    print('d')
    one(freq * 3/2, tempo * 4, vol, 13)
    one(freq * 3/2, tempo * 4, vol, 13)

    one(freq * 1, tempo * 5, vol, 11)

    one(freq * 0, tempo * 5, vol)



# one(freq * 1, tempo * 5, vol, 15)
# one(freq * 4/3, tempo * 3, vol, 14)
# one(freq * 3/2, tempo * 3, vol, 11)
#
# one(freq * 1, tempo * 4, vol, 14)
# one(freq * 4/3, tempo * 3, vol, 14)
# one(freq * 3/2, tempo * 3, vol, 13)
#
# one(freq * 1, tempo * 5, vol, 11)
# one(freq * 4/3, tempo * 3, vol, 14)
# one(freq * 3/2, tempo * 3, vol, 13)
#
# one(freq * 1, tempo * 5, vol, 11)
#
# one(freq * 0, tempo * 5, vol)
