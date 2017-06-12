import random
import pyaudio
from comp_osc import SineOsc
import multiprocessing as mp
import time

sine_osc = SineOsc()

p = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

stream2 = p2.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def func1():
    print ('func1')
    for i in range(20):
        sine_osc.play_frequencies(stream, .1, 1, 1000, 1000,
                                  200, 300)
        sine_osc.play_frequencies(stream, .1, 1, 1000, 1000,
                                  240, 340)
        sine_osc.play_frequencies(stream, .1, 1, 1000, 1000,
                                  200, 300)
        sine_osc.play_frequencies(stream, .2, 1, 1000, 1000,
                                  240, 340)
        sine_osc.play_frequencies(stream, .7, 1, 1000, 1000,
                                  240, 340)
        sine_osc.play_frequencies(stream, .3, 1, 1000, 1000,
                                  260, 360)
        sine_osc.play_frequencies(stream, .8, 1, 1000, 1000,
                                  0)



def func2():
    print ('func2')
    for i in range(10):
        sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                  100, 150, 50, 50)
        sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                  100, 150, 50, 50)
        sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                  100, 150, 50, 50)
        sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                  100 * 7/8, 150* 7/8, 50* 7/8, 50* 7/8)


def func3():
    print ('func3')
    for i in range(5):
        for i in range(20):
            sine_osc.play_frequencies(stream, .1, 0, 1000, 2000,
                                      0)
            sine_osc.play_frequencies(stream, .2, .2, 5000, 5000,
                                      1400)
        time.sleep(4)



if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    p2 = mp.Process(target=func2)
    time.sleep(4)
    p2.start()
    time.sleep(4)
    p3 = mp.Process(target=func3)
    p3.start()



# I will pass you multiple series of notes and you will prepare to play them.
# When they are all ready, you will combine them and produce a single audio file.
# Phrases do not need to start at the same time.
# Phrases do not need to have any shared metrics.
# Rhythmic interaction will be described using mathematical relationships.
# I can put a flag in one phrase that signals when a second phrase will start
# I can wait to start a phrase.
# I can put space in a phrase.

