import random
import pyaudio
from comp_osc import SineOsc
import multiprocessing as mp
import time

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

x = 180
freqs = [
        x,
        x * 9/8,
        x * 4/3,
        x * 5/4,

        x * 3/2,
        x * 11/8,
        x * 3/2,
        x * 15/18,

        x * 5/1.5,
        x * 4/6,
        x * 9/4,
        x * 5/4,

        x * 4/1.5,
        x * 6/2,
        x * 15/4,
        x * 6/2,

        x * 4,
        x * 3/2,
        x * 3/2,
        x * 4/3,

        x * 5/4,
        x * 3/2,
        x * 4/3,
        x * 5/4,

        x * 9/8,
        x * 5/8,
        x * 3/4,
        x * 3/8,

        0,
        x * 3/2,
        0,
        x * 3/2 / 2,
        x/2,
        0,
         ]


def func1():
    print ('func1')
    for i in range(2):
        for freq in freqs:
            sine_osc.play_frequencies(stream, .25, 1, 10000, 1000,
                                      freq,
                                      freq * 2,
                                      freq + 2,
                                      )
        time.sleep(1.9)

def func2():
    print ('func2')
    for i in range(2):
        for freq in freqs:
            sine_osc.play_frequencies(stream, .25, 1, 7000, 10000,
                                      freq * 3/2,
                                      freq * 3/2 * 2,
                                      freq * 3/2,
                                      )
        time.sleep(1.9)


#
# def func3():
#     print ('func3')
#     for i in range(5):
#         for i in range(20):
#             sine_osc.play_frequencies(stream, .1, 0, 1000, 2000,
#                                       0)



if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    time.sleep(2)
    p2 = mp.Process(target=func2)
    p2.start()
    # time.sleep(4)
    # p3 = mp.Process(target=func3)
    # p3.start()



# I will pass you multiple series of notes and you will prepare to play them.
# When they are all ready, you will combine them and produce a single audio file.
# Phrases do not need to start at the same time.
# Phrases do not need to have any shared metrics.
# Rhythmic interaction will be described using mathematical relationships.
# I can put a flag in one phrase that signals when a second phrase will start
# I can wait to start a phrase.
# I can put space in a phrase.

