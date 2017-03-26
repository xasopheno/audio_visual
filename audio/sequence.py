import time
import pyaudio
from Oscillators.sine_osc import SineOsc
from bassline import bassline
from slow import slow
from pretty import pretty, pretty2, cascade, super_cascade, pretty4
from pretty_styx import river_styx

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                frames_per_buffer=6615)

bassline()
bassline()
pretty(390, .5)

time.sleep(.5)

bassline()
bassline()
bassline()
bassline()

time.sleep(.1)

pretty(390, .5)

pretty(400, .1)
pretty(410, .08)
pretty(415, .05)
pretty(425, .03)
cascade()
cascade()

super_cascade()

for i in range(700, 850):
    sine_osc.play_frequencies(
        stream,
        .01,
        .29,
        200,
        200,
        i
    )

time.sleep(.1)

bassline()
bassline()

pretty(250, .02)
pretty(300, .02)
pretty(200, .02)
pretty(150, .01)

bassline()

pretty(500, .01)
pretty2(340, 1.3)

pretty4(336)
pretty4(310)

river_styx(336)
river_styx(310)

slow()
slow()

river_styx(336)

pretty4(310)
pretty4(336)
pretty4(310)
pretty4(336)
