import random
import pyaudio
from Oscillators.sine_osc import SineOsc

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def pretty(freq, tempo):
    sine_osc.play_frequencies(stream, tempo, .09, 200, 200,
                         freq - 5, freq + 4)
    sine_osc.play_frequencies(stream, tempo*2, .04, 200, 200,
                         freq * 15/8,
                         freq * 9/8,
                         freq,)
    sine_osc.play_frequencies(stream, tempo*3, .05, 200, 200,
                         freq * 3/2,
                         freq /2 * 6/7,
                         )
    sine_osc.play_frequencies(stream, tempo*2, .05, 200, 200,
                         freq/3, freq * 5/4,
                         )
    sine_osc.play_frequencies(stream, tempo*3, .051, 200, 200,
                         freq * 9/8,
                         freq/4,
                         freq * 9/8 + 1,
                         )


def cascade():
    print('cascade')
    for i in range(0, 4):
        pretty(420, .02)
    for i in range(0, 4):
        pretty(400, .02)

    for i in range(0, 4):
        pretty(420, .02)
    for i in range(0, 4):
        pretty(400, .02)

    for i in range(0, 4):
        pretty(440, .02)
    for i in range(0, 4):
        pretty(440, .02)

    for i in range(0, 4):
        pretty(500, .02)
    for i in range(0, 2):
        pretty(490, .02)
    for i in range(0, 4):
        pretty(450, .02)


def pretty2(freq, tempo):
    print('pretty3')
    sine_osc.play_frequencies(stream, tempo, .09, 200, 200,
                              freq - 5, freq + 4)
    sine_osc.play_frequencies(stream, tempo * 2, .12, 200, 200,
                              freq * 15 / 8,
                              freq * 9 / 8,
                              freq, )
    sine_osc.play_frequencies(stream, tempo * 3, .08, 200, 200,
                              freq * 3 / 2,
                              freq / 2 * 6 / 7,
                              )
    sine_osc.play_frequencies(stream, tempo * 2, .08, 200, 200,
                              freq / 3, freq * 5 / 4,
                              )


def pretty3(freq):
    print('pretty3')
    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,
                              freq * 9 / 8,
                              freq / 4,
                              freq * 9 / 8 + 1,
                              )
    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,
                              freq * 21 / 17,
                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )
    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,

                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )
    sine_osc.play_frequencies(stream, 1.5, .051, 200, 2000,
                              freq * 26 / 17,
                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )
    sine_osc.play_frequencies(stream, random.choice([.5, .8]), .051, 200, 2000,
                              freq * 31 / 17,
                              freq * 13 / 8,
                              freq * 13 / 8 + 1,
                              freq * 11 / 8,
                              freq * 11 / 8 + 1,
                              freq * 3 / 2 / 4,
                              )


def pretty4(freq):
    print('pretty4')

    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,
                              freq * 9 / 8,
                              freq / 4,
                              freq * 9 / 8 + 1,
                              )
    pretty(300, .005)
    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,
                              freq * 21 / 17,
                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )

    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,

                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )
    pretty(300, .005)
    sine_osc.play_frequencies(stream, 1.5, .051, 200, 2000,
                              freq * 26 / 17,
                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )

    sine_osc.play_frequencies(stream, random.choice([.5, .8]), .051, 200, 2000,
                              freq * 31 / 17,
                              freq * 13 / 8,
                              freq * 13 / 8 + 1,
                              freq * 11 / 8,
                              freq * 11 / 8 + 1,
                              freq * 3 / 2 / 4,
                              )
    pretty(500, .05)

def pretty5(freq, highest):
    print('pretty4')

    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,
                              freq * 9 / 8,
                              freq / 4,
                              freq * 9 / 8 + 1,
                              highest
                              )
    pretty(300, .005)
    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,
                              freq * 21 / 17,
                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              highest
                              )

    sine_osc.play_frequencies(stream, 3, .051, 200, 2000,

                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              highest
                              )
    pretty(300, .005)
    sine_osc.play_frequencies(stream, 1.5, .051, 200, 2000,
                              freq * 26 / 17,
                              freq * 9 / 8,
                              freq * 9 / 8 + 1,
                              freq / 4,
                              )

    sine_osc.play_frequencies(stream, random.choice([.5, .8]), .051, 200, 2000,
                              freq * 31 / 17,
                              freq * 13 / 8,
                              freq * 13 / 8 + 1,
                              freq * 11 / 8,
                              freq * 11 / 8 + 1,
                              freq * 3 / 2 / 4,
                              )
    pretty(500, .05)


def super_cascade():
    for i in range(0, 4):
        pretty(450, .02)
    for i in range(0, 1):
        pretty(300, .02)
    for i in range(0, 1):
        pretty(250, .02)
    for i in range(0, 4):
        pretty(450, .02)

    for i in range(0, 1):
        pretty(250, .02)
    for i in range(0, 1):
        pretty(300, .02)
    for i in range(0, 4):
        pretty(450, .02)

    for i in range(0, 1):
        pretty(500, .02)
    for i in range(0, 4):
        pretty(650, .02)
    for i in range(0, 1):
        pretty(700, .02)
    for i in range(0, 4):
        pretty(850, .02)

cascade()
