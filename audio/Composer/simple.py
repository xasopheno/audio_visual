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


def func1():
    print ('func1')
    volume = 1
    length = 3
    freq = 200
    # sine_osc.play_frequencies(stream, length, volume, 200, 200,
    #
    #                           freq * 1/1, # 4*1/4
    #                           freq * 2, # 4*2/4
    #                           freq * 3/2,  # 2*3/4
    #
    #                           freq * 4 * 1/1,  #4*4/4
    #                           freq * 4 * 5/4, # 4*5/4
    #                           freq * 4 * 3/2, # 4*6/4
    #                           freq * 4 * 7/4, # 4*7/4
    #
    #                           freq * 8 * 1/1,  # 4*8/4
    #                           freq * 8 * 9/8, # 4*9/4
    #                           freq * 8 * 5/4, # 4*10/4
    #                           freq * 8 * 11/8, # 4*11/4
    #                           #
    #                           freq * 8 * 3/2,   # 4*12/4
    #                           freq * 8 * 13/8, # 4*13/4
    #                           freq * 8 * 7/4, # 4*14/4
    #                           freq * 8 * 15/8, # 4*15/4
    #
    # #                           freq * 16 * 1/1 # 4*16/4
    # )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 9 / 8,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 5 / 4,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 4 / 3,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 3 / 2,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 5 / 3,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 15 / 8,  # 4*1/4
                  )

    sine_osc.play(stream, length, volume, 200, 200,
                  freq * 1 / 1,
                  freq * 2,  # 4*1/4
                  )



if __name__=='__main__':
    mp.set_start_method('spawn')
    p2 = mp.Process(target=func1)
    p2.start()
