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


def func1():
    print ('func1')
    for j in range(4):
        for i in range(4, 50, 3):
            print(i)
            sine_osc.play_frequencies(stream, .1, 1, 1000, 1000,
                                      200 +i, 300+i)
            sine_osc.play_frequencies(stream, .1, 1, 1000, 1000,
                                      240+i, 340+i)
            sine_osc.play_frequencies(stream, .1, 1, 1000, 1000,
                                      200+i, 300+i)
            sine_osc.play_frequencies(stream, .2, 1, 1000, 1000,
                                      240+i, 340+i)
            sine_osc.play_frequencies(stream, .7, 1, 1000, 1000,
                                      240+i, 340+i)
            sine_osc.play_frequencies(stream, .3, 1, 1000, 1000,
                                      260+i, 360+i)
            sine_osc.play_frequencies(stream, .8, 1, 1000, 1000,
                                      0)



def func2():
    print ('func2')
    for i in range(4):
        freq1, freq2, freq3, freq4 = 100, 150, 50, 49
        for i in range(4):
            for i in range(2):
                sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                          freq1, freq2, freq3, freq4)
                sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                          freq1, freq2, freq3, freq4)
                sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                          freq1, freq2, freq3, freq4)
                sine_osc.play_frequencies(stream, 1, 1.5, 1000, 30000,
                                          freq1 * 7/8, freq2 * 7/8, freq3 * 7/8, freq4 * 7/8)

            freq1, freq2, freq3, freq4 = freq1 * 7/8, freq2 * 7/8, freq3 * 7/8, freq4 * 7/8

def func3():
    print ('func3')
    for i in range(10):
        for i in range(15):
            sine_osc.play_frequencies(stream, .1, 0, 1000, 2000,
                                      0)

            sine_osc.play_frequencies(stream, .2, 1, 5000, 5000,
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
