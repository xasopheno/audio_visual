import random
import pyaudio
from clear_osc import SineOsc
import multiprocessing as mp
import time

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


Root = 120

def bassi():
    freq = Root
    print ('bass')
    length = 1.5
    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq,
                                  )

    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 9/8,
                                  )

    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 5/4,
                                  )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 4/3,
                              )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 9/8,
                              )

    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq,
                              )

    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 3/2,
                                  )

    # ______________________________________

def viola():
    freq = Root * 2
    print ('viola')
    length = 1.5

    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 5/4,
                                  )

    for i in range(2):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 9/8,
                                  )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 15/8 /2,
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq
                              )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq
                              )

    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 9/8
                              )

    sine_osc.play_frequencies(stream, length * .5, 1, 10000, 1000,
                              freq * 5/4
                              )

    sine_osc.play_frequencies(stream, length * .5, 1, 10000, 1000,
                              freq * 3/2
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 3/2
                              )

# ______________________________________

def violino2():
    freq = Root * 3
    print ('violino2')
    length = 1.5
    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 3/2,
                                  )

    for i in range(3):
        sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                                  freq * 4/3,
                                  )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 5/4,
                              )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 5/3,
                              )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 4/3,
                              )

    sine_osc.play_frequencies(stream, length / 2, 1, 10000, 1000,
                              freq * 3/2,
                              )


    sine_osc.play_frequencies(stream, length / 2, 1, 10000, 1000,
                              freq * 2,
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                               freq * 15/8,
                              )

    # ______________________________________

def violino1():
    freq = Root * 4
    print ('violino1')
    length = 1.5
    sine_osc.play_frequencies(stream, length * 4, 1, 10000, 1000,
                              freq,
                              )

    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 15/8 /2,
                              )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 5/3 /2,
                              )

    sine_osc.play_frequencies(stream, length * .25, 1, 10000, 1000,
                              freq * 3/2 /2,
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 3/2 /2,
                              )


    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 5/3 /2,
                              )

    sine_osc.play_frequencies(stream, length, 1, 10000, 1000,
                              freq * 15/8 /2,
                              )

    sine_osc.play_frequencies(stream, length * .25, 1, 10000, 1000,
                              freq
                              )

    sine_osc.play_frequencies(stream, length * .25, 1, 10000, 1000,
                              freq * 9/8
                              )

    sine_osc.play_frequencies(stream, length * .5, 1, 10000, 1000,
                              freq * 5/4
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 9/8
                              )

    # ______________________________________

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 5/3
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 3/2
                              )

    sine_osc.play_frequencies(stream, length * 3, 1, 10000, 1000,
                              freq * 9/8
                              )

if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=bassi)
    p1.start()
    p2 = mp.Process(target=viola)
    p2.start()
    # p3 = mp.Process(target=violino2())
    # p3.start()
    p4 = mp.Process(target=violino1())
    p4.start()
