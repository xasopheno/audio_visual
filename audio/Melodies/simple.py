import random
import pyaudio
from sine_osc import SineOsc
import time

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )
#
# for j in range (10):
#     freq = 400
#     freq = random.choice([freq, freq * 3/2, freq * 2])
#     for i in range(2):
#         for repetition in range(4):
#             sine_osc.play_frequencies(stream, .1, 4, 200, 200,
#                                       freq / 4,
#                                       freq * 3/2 /2,
#                                       freq / 2,
#                                       freq,
#                                       freq * 3/2,
#                                       freq * 5/4,
#                                       freq * 15/8,
#                                       )
#
#             freq = freq * 9/8
#         freq = freq * 9/8 /2

freq = 80
for x in range(13 * 4):
    sine_osc.play_frequencies(stream, 4, 10, 10000, 20000,
                              freq,
                              freq,
                              freq * 2,
                              freq * 2 * 3/2,
                              freq * 4,
                              freq * 4 * 5/4,
                              freq * 4 * 5/4 + 3,
                              freq * 4 * 11/8,
                              freq * 4 * 11/8 + 2,
                              freq * 4 * 9/8,
                              freq * 5,
                              freq * 5 * 6/5,
                              random.choice([freq * 6, freq * 6 * 9/8, freq * 6 * 6/5, freq * 6 * 3/2])
                              )

    freq += random.choice([10, -10, 5, -5, 3, -3])
    time.sleep(.1)
    if x % 10 == 0 and x > 0:
        time.sleep(8)

time.sleep(.1)
