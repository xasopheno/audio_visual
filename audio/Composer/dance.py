import multiprocessing as mp
import random
import time

import pyaudio
from clear_osc import SineOsc

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

def bass():
    print('func1 start')
    for j in range(40):
        print('func1', j)
        length = 10
        freq = 50
        for i in range(5):
            sine_osc.play_frequencies(stream, length, 1.2, 10000, 10000,
                                      freq,
                                      freq * 2,
                                      freq + 1,
                                      freq + 2,
                                      )

def one(freq, length, vol, subdivision=1, sleep=0):
    print(freq, length, vol, subdivision)
    for i in range(subdivision):
        sine_osc.play_frequencies(stream, (length / subdivision) * .95, vol * random.choice([.4, .5, .6, .7, .8, .9, 1, 1 ,1]), 200, 200,
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

    time.sleep(sleep)


def melody(vol_min, vol_max, range_min, range_max):
    for i in range(22):
        print(i)
        freq = random.uniform(range_min, range_max)
        length = random.uniform(.2, .8)
        vol = random.uniform(vol_min, vol_max)
        subdivision = random.randint(4, 20)
        sleep = random.choice([0,0,.1, .2, .2, .3])
        if i > 12:
            sleep *= 5
            length *= 2
        if i > 17:
            length *=2

        one(freq, length, vol, subdivision=subdivision, sleep=sleep)


if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=bass)
    p1.start()
    time.sleep(2)
    p2 = mp.Process(target=melody, args=(.4, .5, 200, 1200))
    p2.start()
    time.sleep(3)
    p3 = mp.Process(target=melody, args=(.2, .3, 100, 600))
    p3.start()
    p4 = mp.Process(target=melody, args=(.05, .1, 1200, 1700))
    p4.start()
    p5 = mp.Process(target=melody, args=(.03, .08, 1900, 2600))
    p5.start()
    p6 = mp.Process(target=melody, args=(.03, .08, 1900, 2600))
    p6.start()
    p7 = mp.Process(target=melody, args=(.02, .04, 2700, 3300))
    p7.start()

    # p6 = mp.Process(target=func6)
    # p6.start()
