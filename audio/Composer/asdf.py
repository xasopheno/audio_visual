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
            sine_osc.play(stream, length, 1.2, 10000, 10000,
                          freq,
                          freq * 2,
                          freq + 1,
                          freq + 2,
                          )

def one(freq, length, vol, subdivision=1, sleep=0):
    print(freq, length, vol, subdivision)
    for i in range(subdivision):
        sine_osc.play(stream, (length / subdivision) * .95, vol * random.choice([.4, .5, .6, .7, .8, .9, 1, 1 , 1]), 200, 200,
                      freq / 16,
                      freq / 16,
                      freq / 16 + 3,
                      freq / 8,
                      freq / 8,
                      freq / 4,
                      freq / 4,
                      freq / 4 + 5,
                      freq / 2 - 5,
                      freq / 2 + 3,
                      freq - 2,
                      freq * 2 + 2,
                      # freq * 4,
                      # random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 11/8]),
                      # random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 3/2 / 2]),
                      # random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 5/4 / 2]),
                      # random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 5/4 / 2]),
                      # random.choice([freq * 5/4, freq * 8/7, freq * 9/8, freq * 3/4, freq * 3/2, freq * 5/4 / 2]),
                      # random.choice([freq * 5/4 * 2, freq * 8/7 * 2, freq * 9/8 * 2, freq * 3/4 * 2, freq * 3/2 * 2, freq * 5/4 * 2]),
                      # random.choice([freq * 5/4 * 2, freq * 8/7 * 2, freq * 9/8 * 2, freq * 3/4 * 2, freq * 3/2 * 2, freq * 5/4 * 2]),
                      )

    time.sleep(sleep)


def melody(vol_min, vol_max, range_min, range_max):
        for i in range(1000):
            freqs = [1200, 1140, 1000, 980]
            for freq in freqs:
                freq = random.uniform(range_min, range_max)
                length = .8
                vol = random.uniform(vol_min, vol_max)
                subdivision = random.randint(2, 5)
                sleep = random.choice([0,0,.1, .2, .2, .3])
                one(freq, length, vol, subdivision=subdivision, sleep=0)

if __name__=='__main__':
    mp.set_start_method('spawn')
    p2 = mp.Process(target=melody, args=(.4, .5, 200, 600))
    p2.start()
    p3 = mp.Process(target=melody, args=(.3, .4, 600, 900))
    p3.start()


# p6 = mp.Process(target=func6)
    # p6.start()
