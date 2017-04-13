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


def pretty(freq):
    sine_osc.play_frequencies(stream, 3, .5, 200, 200,
                              freq,
                              # freq + 3.2,
                              # freq + 2,
                              freq * 3/2,
                              freq * 9/8,
                              freq * 11/8,
                              )


pretty(400)
