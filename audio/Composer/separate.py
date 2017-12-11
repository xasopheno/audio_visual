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

myFreq = 311


def func1():
    print ('func1')
    freq = myFreq
    for i in range(10):
        sine_osc.play(stream, 3, 1, 10000, 15000,
                      freq
                      )

        sine_osc.play(stream, 2, 1, 5000, 5000,
                      freq * 5 / 3
                      )

        sine_osc.play(stream, 2, 1, 1000, 2000,
                      freq * 5 / 3
                      )

#
        sine_osc.play(stream, 3, 1, 10000, 15000,
                      freq,
                      freq * 2
                      )
        sine_osc.play(stream, 2, 1, 5000, 10000,
                      freq * 8 / 9,
                      freq * 5 / 3
                      )

        sine_osc.play(stream, 2, 1, 5000, 5000,
                      freq * 5 / 3,
                      freq * 2,
                      )


def func2():
    print ('func2')
    freq = myFreq
    freq = random.choice([freq])
    for i in range(8):
        sine_osc.play(stream, 3, .75, 1000, 20000,
                      freq * 2 / 3,
                      freq / 3
                      )

        sine_osc.play(stream, 1, .5, 2000, 20000,
                      freq * 3 / 2,
                      freq * 4 / 3
                      )
        sine_osc.play(stream, 2, .5, 5000, 20000,
                      freq * 7 / 4,
                      freq * 5 / 4
                      )

        sine_osc.play(stream, 1, .75, 10000, 10000,
                      freq * 2 / 3,
                      freq / 3
                      )
        sine_osc.play(stream, 2, .5, 20000, 10000,
                      freq * 5 / 4
                      )


def func3():
    print ('func3')
    for i in range(11):
        sine_osc.play(stream, 12, .6, 1000, 1000,
                      myFreq / 6,
                      myFreq / 6 + 2,
                      )


if __name__=='__main__':
    mp.set_start_method('spawn')
    p3 = mp.Process(target=func3)
    p3.start()
    p1 = mp.Process(target=func1)
    p1.start()
    p2 = mp.Process(target=func2)
    time.sleep(2)
    p2.start()




    # I will pass you multiple series of notes and you will prepare to play them.
    # When they are all ready, you will combine them and produce a single audio file.
    # Phrases do not need to start at the same time.
    # Phrases do not need to have any shared metrics.
    # Rhythmic interaction will be described using mathematical relationships.
    # I can put a flag in one phrase that signals when a second phrase will start
    # I can wait to start a phrase.
    # I can put space in a phrase.
