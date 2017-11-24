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
def func2():
    print ('func2')
    volume = .5
    length = .5
    freq = 440
    for i in range(20):
        for i in range(7):
            sine_osc.play_frequencies(stream, length, volume, 200, 200,
                                      random.choice([freq/4, freq * 3/2/ 4, freq * 4/3 /4]),
                                      freq,
                                      freq * 3/2,
                                      freq * 15/8,
                                      random.choice([freq * 11/8, freq * 5/3, freq * 2]),
                                      random.choice([freq * 9/8, freq * 8/5, freq * 3]),
                                      random.choice([freq/4, freq * 3/2/ 4, freq * 4/3 /4]),
                                    )


            freq += 40
            length -= .076

        length = .5
        freq = 440

def func3():
    print ('func2')
    volume = .1
    length = 3
    freq = 1400
    for i in range(5):
        for i in range(4):
            for j in range(40):
                sine_osc.play_frequencies(stream, length/40, volume, 200, 200,
                                          freq,
                                          freq * 3/2,
                                          freq * 15/8,
                                          # random.choice([freq * 11/8, freq * 5/3, freq * 2]),
                                          # random.choice([freq * 9/8, freq * 8/5, freq * 3]),
                                          # random.choice([freq/4, freq * 3/2/ 4, freq * 4/3 /4]),
                                          )
                freq -= 5


            freq += 240


def func1():
    print ('func2')
    volume = .1
    length = 3
    freq = 1400
    for i in range(5):
        for i in range(4):
            for j in range(40):
                sine_osc.play_frequencies(stream, length/40, volume, 200, 200,
                                          freq,
                                          freq * 3/2,
                                          freq * 15/8,
                                          # random.choice([freq * 11/8, freq * 5/3, freq * 2]),
                                          # random.choice([freq * 9/8, freq * 8/5, freq * 3]),
                                          # random.choice([freq/4, freq * 3/2/ 4, freq * 4/3 /4]),
                                          )
                freq -= 5


            freq += 240

if __name__=='__main__':
    mp.set_start_method('spawn')
    # p1 = mp.Process(target=func2)
    # p1.start()
    p2 = mp.Process(target=func1)
    p2.start()
