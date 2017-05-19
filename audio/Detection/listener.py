import time
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


from Oscillators.sine_osc import SineOsc
from Normalizing.StreamGenerator import *


RATE = 44100
CHUNKSIZE = 1024

osc = SineOsc()
sg = StreamGenerator()
stream = sg.output_stream_generator()

f = open('Detection/output.txt', 'r')
f.seek(0, os.SEEK_END)

past_freq = 0

while True:
    line = f.readline()
    if not line:
        time.sleep(0.025)
        continue
    line = line.strip('\n')
    line = float(line)
    print line
    # if 1300 < line < 1400:
    # if abs(line - past_freq > 100):
    if line == 0:
        vol = 0
        line = 100
    else:
        vol = .5
    osc.play_frequencies(stream, .02, vol, 80, 80,
                         line
                         # # line +2,
                         # # line -2,
                         # # line / 2 * 3/2,
                         # line / 4,
                         )
    # if 1000 < line < 1100:
    #     if abs(line - past_freq > 100):
    #         osc.play_frequencies(stream, 1, .5, 40000, 40000,
    #                              # line / 4,
    #                              # line /4 + 1,
    #                              line + 100,
    #                              # line * 11/8,
    #                              # line * 6/5,
    #                              # line * 4/3,
    #                              )
    past_freq = line

