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
    for i in range(15):
        sine_osc.play(stream, .1, 1, 1000, 1000,
                      200, 300)
        sine_osc.play(stream, .1, 1, 1000, 1000,
                      240, 340)
        sine_osc.play(stream, .1, 1, 1000, 1000,
                      200, 300)
        sine_osc.play(stream, .2, 1, 1000, 1000,
                      240, 340)
        sine_osc.play(stream, .7, 1, 1000, 1000,
                      240, 340)
        sine_osc.play(stream, .3, 1, 1000, 1000,
                      260, 360)
        sine_osc.play(stream, .8, 1, 1000, 1000,
                      0)



def func2():
    print ('func2')
    for i in range(12):
        sine_osc.play(stream, 1, 1.5, 1000, 30000,
                      100, 150, 50, 50)
        sine_osc.play(stream, 1, 1.5, 1000, 30000,
                      100, 150, 50, 50)
        sine_osc.play(stream, 1, 1.5, 1000, 30000,
                      100, 150, 50, 50)
        sine_osc.play(stream, 1, 1.5, 1000, 30000,
                      100 * 7 / 8, 150 * 7 / 8, 50 * 7 / 8, 50 * 7 / 8)


def func3():
    print ('func3')
    for i in range(5):
        for i in range(15):
            sine_osc.play(stream, .1, 0, 1000, 2000,
                          0)
            sine_osc.play(stream, .2, 1, 5000, 5000,
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
