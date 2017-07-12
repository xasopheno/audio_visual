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
    freq = 10000
    for i in range(10000000000):
        sine_osc.play_frequencies(stream, .05, random.choice([.90, 1, 1, 1, 1.05]) /3, 50, 50,
                                  freq,
                                  freq + 1,
                                  )
        freq += 50


def func2():
    print ('func2')
    freq = 10000
    for i in range(10000000000):
        sine_osc.play_frequencies(stream, .07, random.choice([.90, 1, 1, 1, 1.05]) /3, 50, 50,
                                  freq,
                                  # freq + 2
                                  )
        freq += 25

def func3():
    print ('func3')
    freq = 10000
    for i in range(10000000000):
        sine_osc.play_frequencies(stream, .09, random.choice([.90, 1, 1, 1, 1.05]) / 3, 50, 50,
                                  freq,
                                  # freq + 3,
                                  )
        freq += 60




if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    p2 = mp.Process(target=func2)
    time.sleep(1)
    p2.start()
    time.sleep(1)
    p3 = mp.Process(target=func3)
    p3.start()
