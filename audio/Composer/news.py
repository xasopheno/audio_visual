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
    for k in range(2):
        for j in range(3):
            for i in range(80):
                rand = random.choice([0, 0, 0, 0, 0, 1, 1, 1])

                freq1 = random.randrange(50, 54, 1)
                freq2 = freq1 * 5/8

                if rand == 1:
                    freq2 = freq2 * random.choice([5 * 5/4, 6 * 3/4, 6 * 9/8, 5 * 11/8])

                sine_osc.play_frequencies(stream, .22, random.choice([.90, 1, 1, 1, 1.05]) / 4, 1000, 1000,
                                          freq1,
                                          )
                sine_osc.play_frequencies(stream, .09, .4, 1000, 1000,
                                          freq2 * 5/8,
                                          )

            for freq in range(10 * 120, 10 * 127):
                sine_osc.play_frequencies(stream, .11, .2, 100, 100,
                                          freq,
                                          freq / 2,
                                          freq * 11/8,
                                          freq * 3/4,
                                          freq / 8,
                                          freq / 16,
                                          freq / 32,
                                          )

        time.sleep(120)

def func2():
    print ('func2')
    for i in range(12):
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
    # p2 = mp.Process(target=func2)
    # time.sleep(4)
    # p2.start()
    # time.sleep(4)
    # p3 = mp.Process(target=func3)
    # p3.start()
