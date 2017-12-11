import random
import pyaudio
from clear_osc import SineOsc
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

def func2():
    print('func2')
    freq = 120
    length = 1.5
    sine_osc.play(stream, length * 4, 1, 10000, 1000,
                  freq * 3,
                  )

    sine_osc.play(stream, length, 2, 10000, 1000,
                  freq * 16 / 9 / 2 * 3
                  )

    sine_osc.play(stream, length * .75, 2, 10000, 1000,
                  freq * 5 / 3 / 2 * 3
                  )

    sine_osc.play(stream, length * .25, 2, 10000, 1000,
                  freq * 3 / 2 / 2 * 3
                  )

    sine_osc.play(stream, length * 3, 2, 10000, 1000,
                  freq * 3 / 2 / 2 * 3
                  )

    sine_osc.play(stream, length * 3, 2, 10000, 1000,
                  freq * 3 / 2 / 2 * 3
                  )


    sine_osc.play(stream, length * 3, 2, 10000, 1000,
                  freq * 3 / 2 / 2 * 3
                  )


    #
    # sine_osc.play_frequencies(stream, length, 2, 10000, 1000,
    #                           freq * 16/9 /2
    #                           )

    #
    # freq = freq * 16/9 /2
    # sine_osc.play_frequencies(stream, length * .75, 2, 10000, 1000,
    #                           freq * 3,
    #                           )
    #
    # sine_osc.play_frequencies(stream, length * 3, 2, 10000, 1000,
    #                           freq * 3,
    #                           )

def func1():
    print ('func1')
    freq = 120
    length = 1.5
    for i in range(3):
        sine_osc.play(stream, length, 1, 10000, 1000,
                      freq,
                      freq * 3 / 2,
                      # freq * 2 * 5/4,
                      # freq * 2 * 3/2,
                      )

    freq = freq * 9/8
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 4 / 3,
                      freq * 4 / 3 * 2,
                      # freq * 2 * 6/5
                      # freq * 2 * 3/2
                      )


    freq = freq * 9/8
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 5 / 4,
                      # freq * 4/3 * 2,
                      )

    # _______________________________

    freq = freq * 25/24
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 3 / 2,
                  # freq * 2,
                  # freq * 2 * 5/4,
                  )

    freq = freq * 5/3 / 2
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 4 / 3,
                  )

    freq = freq * 16/9 / 2
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 3 / 2,
                  )


    # ________________________4

    freq = freq * 3/2
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 5 / 4,
                      )

    freq = freq * 16/9 /2
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 3 / 2, )


    freq = freq * 15/8 /2
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 8 / 5
                      )
    #
    freq = freq * 16/9 /2
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 4 / 3
                      )

    freq = freq * 16/9 /2
    for i in range(3):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 3 / 2
                      )

    # __________________________________

    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 2
                  )

    freq = freq * 9/8
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 2
                  )

    freq = freq * 9/8
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 2
                  )

    freq = freq * 25/24
    for i in range(2):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 2
                      )

    freq = freq * 9/8
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq,
                  freq * 5 / 3
                  )


    freq = freq * 9/8
    for i in range(2):
        sine_osc.play(stream, length, 1, 1000, 1000,
                      freq,
                      freq * 5 / 3
                      )


    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq / 2,
                  freq,
                  )

    freq = freq * 15/8 /2
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq / 2,
                  freq,
                  )


    freq = freq * 25/24 * 2
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq / 2,
                  freq,
                  )


    freq = freq * 15/8 /2
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq / 2,
                  freq,
                  )


    freq = freq * 25/24
    sine_osc.play(stream, length, 1, 1000, 1000,
                  freq / 2,
                  freq,
                  )

    # ____________________________________

    freq = freq * 9/8 /2
    sine_osc.play(stream, length / 2, 1.1, 1000, 1000,
                  freq,
                  freq * 3 / 2,
                  )

    sine_osc.play(stream, length / 2, 1.1, 1000, 1000,
                  freq * 5 / 3,
                  )


    freq = freq * 9/8
    sine_osc.play(stream, length * 1.15, 1.2, 1000, 1000,
                  freq,
                  freq * 3 / 2,
                  )


    sine_osc.play(stream, length * 1.15, 1.2, 1000, 1000,
                  freq / 2,
                  freq,
                  )


    # _________________________
    freq = freq * 4/3 /2
    sine_osc.play(stream, length * 2, 1, 1000, 1000,
                  freq / 2,
                  freq,
                  freq * 5 / 4,
                  freq * 3 / 2,
                  freq * 2,
                  )


if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    # p2 = mp.Process(target=func2)
    # p2.start()
