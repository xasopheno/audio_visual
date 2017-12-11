import multiprocessing as mp
import random
import time

import pyaudio
from clear_osc import SineOsc

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

def func1():
    print('func1 start')
    for j in range(40):
        print('func1', j)
        length = .25
        freq = 50
        if j == 9 or j == 20:
            time.sleep(1.25)
        for i in range(5):
            sine_osc.play(stream, length, 1, 8000, 1000,
                          freq,
                          freq * 2,
                          freq + 1,
                          freq + 2,
                          )
        freq += 10
        time.sleep(1)
    time.sleep(4)
    p6 = mp.Process(target=func6)
    p6.start()



def func2():
    print('func2')
    for j in range(40):
        print('func2', j)
        if j == 9 or j == 20:
            time.sleep(1.25)
        length = .25
        freq = 51
        for i in range(5):
            sine_osc.play(stream, length, 1, 8000, 1000,
                          freq,
                          freq * 2,
                          freq + 1,
                          )
        freq += 10
        time.sleep(1)

def func3():
    print('func3')
    time.sleep(5)
    for j in range(5):
        length = .07
        freq = random.choice([200, 250, 190, 210, 330, 200, 200, 250, 200, 200, 200])
        for i in range(random.randrange(8, 20, 1)):
            volume = random.choice([.4, .5, .6, .3, .4, .5, .5, .5, .5]) / 1.5
            sine_osc.play(stream, length, volume, 200, 200,
                          freq,
                          freq * 2,
                          freq + 1,
                          )
            freq += random.choice([10, -13, 17, 15, 4, -18])

        time.sleep(random.choice([.5, .7, 1, 1, .8,]) * 2)

    for j in range(22):
        if j == 10:
            time.sleep(2)
        length = .07
        freq = random.choice([200, 250, 190, 210, 330, 200, 200, 250, 200, 200, 200])
        for i in range(random.randrange(9, 25, 1)):
            volume = random.choice([.4, .5, .6, .3, .4, .5, .5, .5, .5]) / 2
            sine_osc.play(stream, length, volume, 200, 200,
                          freq / 2,
                          freq,
                          freq * 2,
                          freq + 1,
                          freq * 3 / 5,
                          freq * 2 + 2,
                          freq * 9 / 8,
                          freq * 2 - 4,
                          freq * 3,
                          )
            freq += random.choice([10, -13, 17, 15, 4, -18, 40, -40,])

        time.sleep(random.choice([.5, .7, 1, 1.2, 1.5, .3, 1, 1, .8, .5, .1]) * 2)


def func4():
    print('func4')
    time.sleep(3)
    for j in range(12):
        length = 5
        freq = random.choice([1000, 1040, 1080])
        volume = .07
        sine_osc.play(stream, length, volume, 40000, 40000,
                      freq / 2 - 3,
                      freq - 3,
                      freq + 3,
                      freq - 4,
                      freq + 5,
                      )

        # time.sleep(random.choice([.5, .7, 1, 1, .8,]) * 5)

    for j in range(14):
        time.sleep(8)
        print('func4', j)
        length = 9
        freq = random.choice([1000, 1040, 1080])
        volume = .11
        sine_osc.play(stream, length, volume, 60000, 70000,
                      freq * 3 / 2,
                      freq * 5 / 4 * 2,
                      freq * 5 / 4,
                      freq * 2,
                      freq * 9 / 8,
                      freq * 15 / 8,
                      freq * 11 / 8
                      )

        time.sleep(random.choice([.5, .7, 1, 1, .8,]) * 2)

def func5():
    print('func5')
    time.sleep(3)
    for j in range(12):
        length = 5
        freq = random.choice([1000, 1040, 1080])
        volume = .04
        sine_osc.play(stream, length, volume, 70000, 60000,
                      freq / 2 - 3,
                      freq - 3,
                      freq + 3,
                      freq - 4,
                      freq + 5,
                      )
        freq += random.choice([10, -13, 17, 15, 4, -18])

    for j in range(14):
        time.sleep(8)
        print('func5', j)
        length = 10
        freq = random.choice([1000, 1040, 1080]) - 8
        volume = .11
        sine_osc.play(stream, length, volume, 100000, 70000,
                      freq / 2 - 3,
                      freq - 3,
                      freq + 3,
                      freq * 3 / 2 / 2,
                      freq * 3 / 2,
                      freq * 5 / 4 * 2,
                      freq * 5 / 4,
                      freq * 2,
                      freq * 9 / 8,
                      freq * 15 / 8,
                      freq * 11 / 8,
                      )

        time.sleep(random.choice([.5, .7, 1, 1, .8,]) * 2)


def func6():
    time.sleep(20)
    for i in range(8):
        time.sleep(.6)
        for i in range(5):
            length = 0.1
            volume = .4
            freq = random.choice([600, 650, 680, 690])
            sine_osc.play(stream, length, volume, 1000, 4000,
                          freq,
                          freq + 2,
                          freq,
                          freq * 3 / 2,
                          freq * 2,
                          freq * 2,
                          )
            freq += random.choice([19, 14, 25, 16, 23, -5, -34, -26, -16])

    for j in range(30):
        length = .6
        freq = random.choice([50, 51, 52, 53, 54, 55, 49, 48])
        volume = .76
        sine_osc.play(stream, length, volume, 1000, 10000,
                      freq,
                      freq + 2,
                      freq,
                      freq * 3 / 2,
                      freq * 2,
                      freq * 2,
                      )
        for i in range(5):
            length = 0.1
            volume = .3
            freq = random.choice([600, 650, 680, 690])
            sine_osc.play(stream, length, volume, 1000, 4000,
                          freq + 2,
                          freq,
                          freq * 3 / 2,
                          freq * 2,
                          freq * 2,
                          freq * 3 - random.choice([2, 4, 6, 7, 8, 10])
                          )
            freq += random.choice([19, 14, 25, 16, 23, -5, -34, -26, -16])

    p1 = mp.Process(target=func1)
    p1.start()
    time.sleep(.9)
    p2 = mp.Process(target=func2)
    p2.start()
    time.sleep(6)
    p3 = mp.Process(target=func3)
    p3.start()


def func7():
    pass

if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    p4 = mp.Process(target=func4)
    p4.start()
    p5 = mp.Process(target=func5)
    p5.start()
    time.sleep(.9)
    p2 = mp.Process(target=func2)
    p2.start()
    time.sleep(4)
    p3 = mp.Process(target=func3)
    p3.start()
    # p6 = mp.Process(target=func6)
    # p6.start()
