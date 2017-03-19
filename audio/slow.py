import pyaudio
import random
import time
from oscillator import Oscillator

osc = Oscillator()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                frames_per_buffer=6615)


def pretty(frequency, tempo):
    freq = random.choice([frequency, frequency +1, frequency+2, frequency+3, frequency+4, frequency+5])
    osc.play_frequencies(stream, .35, .1, 200, 200,
                         freq * 11/8,
                         freq/2,
                         freq/4)
    osc.play_frequencies(stream, .1, .05, 200, 200,
                         freq,
                         freq/2 * 3)
    osc.play_frequencies(stream, .1, .05, 200, 200,
                         freq,
                         freq * 11/8)
    osc.play_frequencies(stream, .1, .05, 200, 200,
                         freq,
                         freq * 5/4)
    osc.play_frequencies(stream, .1, .05, 200, 200,
                         freq,
                         freq * 9/8)
    osc.play_frequencies(stream, .1, .05, 200, 200,
                         freq,
                         freq * 15/8 /2)


def thechord():
    freq = random.choice([300])
    osc.play_frequencies(stream, .33, .1, 10000, 2000,
                         freq,
                         freq * 15/8 /2,
                         freq * 26 /13,
                         freq / 4,
                         freq / 3 + 4,
                         random.choice([800, 810, 812]),
                         random.choice([803, 814, 816]),
                         random.choice([320, 315, 325]))


def slow():
    for i in range(3):
        for i in range(1):
            pretty(300, 0)
            thechord()
            thechord()
            pretty(300, 0)
            thechord()
            thechord()
            thechord()

# low notes
# for i in range(1000):
#     freq = random.choice([60, 61, 62, 63, 64, 65, 66, 67, ])
#     osc.play_frequencies(stream, 5, .3, 200, 200,
#                          freq * 3/2,
#                          freq/2,
#                          freq/2 +3,)
