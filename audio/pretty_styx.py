
import pyaudio
import random
import time
from oscillator import Oscillator
from filehandler import mp3_to_np


osc = Oscillator()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                frames_per_buffer=6615)


def pretty(freq, tempo):
    osc.play_frequencies(stream, tempo, .09, 200, 200,
                         freq - 5, freq + 4)
    osc.play_frequencies(stream, tempo*2, .04, 200, 200,
                         freq * 15/8,
                         freq * 9/8,
                         freq,)
    osc.play_frequencies(stream, tempo*3, .05, 200, 200,
                         freq * 3/2,
                         freq /2 * 6/7,
                         )
    osc.play_frequencies(stream, tempo*2, .05, 200, 200,
                         freq/3, freq * 5/4,
                         )
    osc.play_frequencies(stream, tempo*3, .051, 200, 200,
                         freq * 9/8,
                         freq/4,
                         freq * 9/8 + 1,
                         )


def pretty4(freq):
    print('pretty4')

    osc.play_frequencies(stream, 3, .051, 200, 2000,
                         freq * 9/8,
                         freq/4,
                         freq * 9/8 + 1,
                         )
    pretty(300, .005)
    osc.play_frequencies(stream, 3, .051, 200, 2000,
                         freq * 21/17,
                         freq * 9/8,
                         freq * 9/8 + 1,
                         freq/4,
                         )

    osc.play_frequencies(stream, 3, .051, 200, 2000,

                         freq * 9/8,
                         freq * 9/8 + 1,
                         freq/4,
                         )
    pretty(300, .005)
    osc.play_frequencies(stream, 1.5, .051, 200, 2000,
                         freq * 26/17,
                         freq * 9/8,
                         freq * 9/8 + 1,
                         freq/4,
                         )

    osc.play_frequencies(stream, random.choice([.5, .8]), .051, 200, 2000,
                         freq * 31/17,
                         freq * 13/8,
                         freq * 13/8 + 1,
                         freq * 11/8,
                         freq * 11/8 + 1,
                         freq * 3/2 / 4,
                         )
    pretty(500, .05)

for i in range(50):
    pretty4(336)
    pretty4(310)

