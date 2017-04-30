import random
import time
import pyaudio
from Oscillators.sine_osc_cleek import SineOsc

sine_osc = SineOsc()
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def cleek(freq, length, vol):
    sine_osc.play_frequencies(stream,
                              length,
                              vol * .2,
                              2000,
                              2000,
                              random.choice([freq / 2 + 20, freq / 2, -30, freq / 2 + 100, freq / 2]),
                              # freq,
                              # freq,
                              # freq * 22/8,
                              # freq * 15/8,
                              # freq * 27/8,
                              random.choice([freq * 3, freq * 15/4, freq * 36/8]),
                              )

frequency = 200
for i in range(100):
    cleek(
        frequency,
        random.choice([.15, .2, .15, .5, .15, .3, 1]),
        random.choice([1, 1, 0, 0, 0])
    )
    frequency += random.choice([10, -10, 30, -30, 10, 25, -25])

time.sleep(.5)
