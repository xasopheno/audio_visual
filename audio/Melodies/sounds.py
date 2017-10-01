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


# sine_osc.play_frequencies(stream, 2, 1, 200, 200,
#                           400,
#                           )
#
