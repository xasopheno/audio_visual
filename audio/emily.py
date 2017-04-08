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


def idea(freq, tempo):
    sine_osc.play_frequencies(stream, tempo, .09, 30000, 200,
                              freq,
                              freq * 3/2,
                              freq * 3/2 + 3,
                              freq * 3/2,
                              freq * 3/2 -3,
                              )
    sine_osc.play_frequencies(stream, tempo, .09, 10000, 200,
                              freq,
                              freq * 3/2,
                              freq * 3/2 + 3,
                              freq * 3/2 -3,
                              freq)
    sine_osc.play_frequencies(stream, tempo * 2, .09, 10000, 20000,
                              freq,
                              freq * 3/2,
                              freq * 3/2 + 3,
                              freq * 5/4,
                              freq * 3/2 - 2,
                              freq * 9/4 + 2
                              )


def idea_2(freq, tempo):

    sine_osc.play_frequencies(stream, tempo * 6, .03, 10000, 20000,
                              freq /2,
                              freq /2 - 2,
                              freq /2 + 2,
                              freq,
                              freq * 3/2,
                              freq * 3/2 - 3.3,
                              freq * 3/2 + 3.3,
                              freq * 5/4,
                              freq * 3/2 - 2,
                              freq * 9/4 + 2,
                              freq * 9/2,
                              freq * 30/8,
                              freq * 30/8 - 3.2,
                              freq * 36/8 + 3.2,
                              freq * 20/4,
                              freq * 23/4,
                              freq * 23/4 + 2,
                              freq * 33/8,
                              )

freq = 200
for i in range(5):
    freq += random.choice([-3, -6, + 4])
    idea_2(freq, 2)


# idea(140, 4)
# idea(160, 4)
# idea(120, 4)
# idea(160, 4)
