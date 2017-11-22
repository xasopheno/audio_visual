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
    volume = .15
    length = .005
    time.sleep(5.5)
    start = 43000
    for i in range(1):
        print(i)
        for i in range(start, 46260, 5):
            print(i)
            sine_osc.play_frequencies(stream, length, volume, 200, 200,
                                      i * 3/2,
                                      i * 3/2 * 2,
                                      i * 3/2,
                                      i / 2,
                                      )
            length += .0001

def func1():
    length = 1.2
    volume = .25
    freq = 783 /2
    print ('func1')
    sine_osc.play_frequencies(stream, length * 1.2, volume * .8, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              )
    freq = freq * 8/5/2
    sine_osc.play_frequencies(stream, length * 2, volume * 1.1, 4000, 6000,
                              freq / 4,
                              freq /2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              )

    time.sleep(.1)

    freq = freq * 25/24
    sine_osc.play_frequencies(stream, length * .75, volume, 7000, 1000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4,
                              )

    freq = freq * 9/8
    sine_osc.play_frequencies(stream, length * .75, volume, 4000, 3000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 15,
                              )

    freq = freq * 25/24 /2
    sine_osc.play_frequencies(stream, length * .2, volume * .5, 3000, 1000,
                              freq / 4,
                              freq / 2,
                              freq * 3/2/2,
                              freq,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4,
                              )

    freq = freq * 6/5 * 2
    sine_osc.play_frequencies(stream, length * 2, volume * 1.3, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 3/2 + 10 * 4,
                              freq * 22/8 - 4
                              )

    freq = freq * 9/5 /2
    sine_osc.play_frequencies(stream, length * .5, volume * .9, 5000, 1000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2 + 5,
                              freq * 5/4,
                              freq * 2,
                              freq + 2,
                              )

    freq = freq * 15/8 /2
    sine_osc.play_frequencies(stream, length * .95, volume * .8, 4000, 8000,
                              freq / 4,
                              freq /2 + 2,
                              freq / 2,
                              freq,
                              freq * 5/4,
                              freq * 7/4,
                              freq * 3/2 + 4,
                              freq * 2,
                              freq * 2+ 3,
                              )

    time.sleep(1)
    # ___________________________________

    freq = freq * 45/32 /2
    sine_osc.play_frequencies(stream, length * 1.4, volume * 1.2, 4000, 1000,
                              freq /4,
                              freq /2 + 3,
                              freq /2,
                              freq,
                              freq + 5,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4
                              )


    freq = freq * 45/32
    sine_osc.play_frequencies(stream, length * 1.7, volume * 1.2, 8000, 5000,
                              freq /4,
                              freq /2,
                              freq /2 + 2,
                              freq,
                              freq + 9,
                              freq - 5,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4,
                              )

    time.sleep(1)

    freq = freq * 3/2 /2
    sine_osc.play_frequencies(stream, length * .5, volume * .9, 3000, 1000,
                              freq,
                              freq,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5,
                              freq * 7/6,
                              freq * 8/5
                              )

    freq = freq * 45/32
    sine_osc.play_frequencies(stream, length * .5, volume, 3000, 3000,
                              freq,
                              freq,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5,
                              freq * 7/6,
                              freq * 8/5
                              )

    freq = freq * 5/3 /2 + 10
    sine_osc.play_frequencies(stream, length * 1, volume * .95, 3000, 3000,
                              freq,
                              freq,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5,
                              freq * 7/6 + 3,
                              freq * 8/5 + 2,
                              freq * 9/8,
                              freq * 11/8
                              )

    freq = freq * 8/5 /2
    sine_osc.play_frequencies(stream, length * .4, volume * .8, 3000, 3000,
                              freq,
                              freq,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5,
                              freq * 7/6,
                              freq * 8/5
                              )

    freq = freq * 5/3 /2
    sine_osc.play_frequencies(stream, length * .25, volume * .7, 6000, 2000,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5,
                              freq * 7/6,
                              freq * 8/5
                              )

    freq = freq * 9/8
    sine_osc.play_frequencies(stream, length * .3, volume, 3000, 5000,
                              freq /4,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              )

    freq = freq * 6/5
    sine_osc.play_frequencies(stream, length, volume, 4000, 5000,
                          freq /4,
                          freq /2 + 6,
                          freq,
                          freq * 2,
                          freq + 2,
                          )

    time.sleep(.2)

    freq = freq * 9/8
    print(freq)
    freq = 350.73
    sine_osc.play_frequencies(stream, length * .5, volume, 4000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              )

    freq = freq * 3/2/2
    sine_osc.play_frequencies(stream, length * .3, volume, 2000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              )

    sine_osc.play_frequencies(stream, length * 1.5, volume, 2000, 10000,
                              freq /2,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5 + 3,
                              freq * 5/4 - 2,
                              )


    time.sleep(2)

    # Second half _________
    freq = freq * 5/4 / 2
    sine_osc.play_frequencies(stream, length * .5, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 3,
                              )

    freq = freq * 4/3
    sine_osc.play_frequencies(stream, length * .75, volume * 1.1, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 3,
                              )


    freq = freq * 8/5
    sine_osc.play_frequencies(stream, length * 2, volume * 1.2, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 3,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    time.sleep(2)
    # _________________________
    freq = freq * 3/2
    sine_osc.play_frequencies(stream, length * .2, volume * .7, 4000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 7/6,
                              freq * 4,
                              )

    freq = freq * 4/3 /2
    sine_osc.play_frequencies(stream, length * 1.5, volume * 1, 4000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 4,
                              )

    time.sleep(1)
    freq = freq * 25/24
    sine_osc.play_frequencies(stream, length * .75, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 3,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    freq = freq * 8/5 /2
    sine_osc.play_frequencies(stream, length * .75, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 3,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    freq = freq * 5/4
    sine_osc.play_frequencies(stream, length * .3, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 3,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )


    freq = freq * 9/5 /2
    sine_osc.play_frequencies(stream, length * 1.5, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 3,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    freq = freq * 45/32 /2
    sine_osc.play_frequencies(stream, length * .6, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 3,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    freq = freq * 9/5
    sine_osc.play_frequencies(stream, length * 3, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 4,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 3/2 * 3,
                              freq * 3/2 * 3 - 7,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    time.sleep(1)
    # _________________________

    freq = freq * 15/8 /2
    sine_osc.play_frequencies(stream, length * .5, volume, 4000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              )

    freq = freq * 3/2 /2
    sine_osc.play_frequencies(stream, length * 1, volume, 4000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              )

    freq = freq * 9/5 / 2
    sine_osc.play_frequencies(stream, length * .7, volume, 4000, 1000,
                              freq,
                              freq * 2,
                              freq + 2,
                              )

    time.sleep(.2)
    # _________________________

    freq = freq * 25/24
    sine_osc.play_frequencies(stream, length * .7, volume, 4000, 1000,
                              freq /2,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5 + 3,
                              freq * 5/4 - 2,
                              )


    freq = freq * 9/8
    sine_osc.play_frequencies(stream, length * 1.5, volume, 4000, 1000,
                              freq /2,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5 + 3,
                              freq * 5/4 - 2,
                              )
    #___________________________
    time.sleep(2)

    freq = freq * 25/24
    sine_osc.play_frequencies(stream, length * .5, volume, 4000, 1000,
                              freq /4,
                              freq /2,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5 + 3,
                              freq * 5/4 - 2,
                              )

    freq = freq * 9/8
    sine_osc.play_frequencies(stream, length * .5, volume, 4000, 1000,
                              freq /4,
                              freq /2,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5 + 3,
                              freq * 5/4 - 2,
                              )

    freq = freq * 9/8
    sine_osc.play_frequencies(stream, length * .8, volume, 4000, 1000,
                              freq /4,
                              freq /2,
                              freq /2 + 6,
                              freq,
                              freq * 2,
                              freq + 2,
                              freq * 6/5 + 3,
                              freq * 5/4 - 2,
                              )




    freq = freq * 5/3 / 4
    sine_osc.play_frequencies(stream, length * .8, volume, 4000, 1000,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 4,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 3/2 * 3,
                              freq * 3/2 * 3 - 7,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )

    freq = freq * 15/8
    sine_osc.play_frequencies(stream, length * .8, volume, 4000, 1000,
                              freq / 4,
                              freq / 4,
                              freq / 2,
                              freq / 2 + 4,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 3/2 * 3,
                              freq * 3/2 * 3 - 7,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )


    freq = freq * 4/3 /2
    sine_osc.play_frequencies(stream, length * 3, volume, 4000, 1000,
                              freq / 4,
                              freq / 4 + 3,
                              freq / 2,
                              freq / 2 + 4,
                              freq,
                              freq * 3/2,
                              freq * 2,
                              freq + 2,
                              freq * 3/2 * 3 - 7,
                              freq * 4 + 2,
                              freq * 4 - 5,
                              )


    print('improvising')
    # ___________________________

    time.sleep(5)
    p2 = mp.Process(target=func2)
    p2.start()
    freq = freq + 11
    freq = freq * 15/8
    sine_osc.play_frequencies(stream, length * 5, volume * .6, 9000, 30000,
                              freq /16,
                              freq / 4,
                              freq / 4,
                              freq / 2,
                              freq /8 + 2,
                              freq /8 - 3,
                              freq * 5/4 / 2,
                              freq * 9/8 * 3,
                              freq * 11/8 * 2,
                              )

    sine_osc.play_frequencies(stream, length * 4, volume * .65, 9000, 30000,
                              freq /16,
                              freq / 4,
                              freq / 4,
                              freq / 2,
                              freq /8 + 2,
                              freq /8 - 3,
                              freq * 5/4 / 2 - 5,
                              freq * 9/8 * 3 - 3,
                              freq * 11/8 * 2 - 4,
                              )

    freq = freq + 20
    sine_osc.play_frequencies(stream, length * 4, volume * .7, 9000, 30000,
                              freq /16,
                              freq / 4,
                              freq / 4,
                              freq / 2,
                              freq /8 + 2,
                              freq /8 - 3,
                              freq * 5/4 / 2 - 17,
                              freq * 9/8 * 3 - 11,
                              freq * 11/8 * 2 - 15,
                              )

    freq = freq + 25
    sine_osc.play_frequencies(stream, length * 10, volume * .8, 9000, 20000,
                              freq /16,
                              freq / 4,
                              freq / 4,
                              freq / 2,
                              freq /8 + 2,
                              freq /8 - 3,
                              freq * 5/4 / 2 - 50,
                              freq * 9/8 * 3 - 29,
                              freq * 11/8 * 2 - 30,
                              )





if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    # time.sleep(2)
    # p2 = mp.Process(target=func2)
    # p2.start()
    # time.sleep(4)
    # p3 = mp.Process(target=func3)
    # p3.start()



# I will pass you multiple series of notes and you will prepare to play them.
# When they are all ready, you will combine them and produce a single audio file.
# Phrases do not need to start at the same time.
# Phrases do not need to have any shared metrics.
# Rhythmic interaction will be described using mathematical relationships.
# I can put a flag in one phrase that signals when a second phrase will start
# I can wait to start a phrase.
# I can put space in a phrase.

