import random
import pyaudio
from comp_osc import SineOsc

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


one = [2, 1, 200, 200, 400]
two = [2, .1, 200, 200, 840]

three = [2, .1, 200, 200, 500]
four = [2, .5, 200, 200, 900]

sine_osc.play_multiple_parts(stream, one, two)
sine_osc.play_multiple_parts(stream, three, four)

# I will pass you multiple series of notes and you will prepare to play them.
# When they are all ready, you will combine them and produce a single audio file.
# Phrases do not need to start at the same time.
# Phrases do not need to have any shared metrics.
# Rhythmic interaction will be described using mathematical relationships.
# I can put a flag in one phrase that signals when a second phrase will start
# I can wait to start a phrase.
# I can put space in a phrase.

