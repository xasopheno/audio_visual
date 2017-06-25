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


def func1():
    print ('func1')
    sweepRange = 100
    start = 600
    freq = random.choice([start, start, start, start, start, start, start * 9/8,])
    length = .025
    for i in range(sweepRange):
        sine_osc.play_frequencies(stream, length, .25, 200, 200,
                                  freq,
                                  freq,
                                  freq * 2
                                  )
        freq += 3

        if sweepRange - i < 6:
            length += .1

    for i in range(2):
        sine_osc.play_frequencies(stream, .3, .5, 200, 200,
                                  freq,
                                  freq,
                                  freq * 2,
                                  )
    freq = freq * 8/9
    for i in range(2):
        sine_osc.play_frequencies(stream, .2, .5, 2000, 200,
                                  freq,
                                  freq,
                                  freq * 2,
                                  )
    freq = freq * 8/9
    for i in range(2):
        sine_osc.play_frequencies(stream, .2, .5, 200, 2000,
                                  freq,
                                  freq,
                                  freq * 2,
                                  )
    freq = freq * 24/25
    for i in range(2):
        sine_osc.play_frequencies(stream, .2, .5, 500, 2000,
                                  freq,
                                  freq,
                                  freq * 2,
                                  )

    freq = freq * 25/24
    sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                                  )



    freq = freq * 25/24
    sine_osc.play_frequencies(stream, .3, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 8/9
    sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 7/6
    sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 6/7
    sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 9/10
    for i in range(2):
        sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                                  freq,
                                  freq,
                                  freq * 2,
                                  )
    freq = freq * 24/25
    for i in range(2):
        sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                                  freq,
                                  freq,
                                  freq * 2,
                                  )

    freq = freq * 8/11
    sine_osc.play_frequencies(stream, .2, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 7/6
    sine_osc.play_frequencies(stream, .3, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 7/6
    sine_osc.play_frequencies(stream, .35, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )


    freq = freq * 8/9
    sine_osc.play_frequencies(stream, .3, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    sine_osc.play_frequencies(stream, .4, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 8/9
    sine_osc.play_frequencies(stream, .4, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    sine_osc.play_frequencies(stream, .45, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    freq = freq * 8/9
    sine_osc.play_frequencies(stream, .8, .8, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )

    sine_osc.play_frequencies(stream, .9, .5, 2000, 3000,
                              freq,
                              freq,
                              freq * 2,
                              )
# def func2():
#     print ('func2')
#     freq = 300
#     freq = random.choice([freq])
#     for i in range(10):
#         sine_osc.play_frequencies(stream, 3, .75, 1000, 30000,
#                                   freq * 2/3,
#                                   freq / 3
#                                   )
#
#         sine_osc.play_frequencies(stream, 1, .5, 2000, 30000,
#                                   freq * 3/2,
#                                   freq * 4/3
#                                   )
#         sine_osc.play_frequencies(stream, 2, .5, 5000, 20000,
#                                   freq * 7/4,
#                                   freq * 5/4
#                                   )
#
#         sine_osc.play_frequencies(stream, 1, .75, 10000, 10000,
#                                   freq * 2/3,
#                                   freq / 3
#                                   )
#         sine_osc.play_frequencies(stream, 2, .5, 20000, 10000,
#                                   freq * 5/4
#                                   )
#
#
# def func3():
#     print ('func3')
#     for i in range(11):
#         sine_osc.play_frequencies(stream, 12, .6, 1000, 50000,
#                                   50,
#                                   48,
#                                   )


if __name__=='__main__':
    # mp.set_start_method('spawn')
    # p1 = mp.Process(target=func1)
    # p1.start()
    time.sleep(10)
    for i in range(4):
        print (i)
        time.sleep(20)
        func1()

    # I will pass you multiple series of notes and you will prepare to play them.
    # When they are all ready, you will combine them and produce a single audio file.
    # Phrases do not need to start at the same time.
    # Phrases do not need to have any shared metrics.
    # Rhythmic interaction will be described using mathematical relationships.
    # I can put a flag in one phrase that signals when a second phrase will start
    # I can wait to start a phrase.
    # I can put space in a phrase.
