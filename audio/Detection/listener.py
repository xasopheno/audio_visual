import time
import os.path
import sys
import random
from collections import deque
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
commands = open('Detection/commands.txt', 'w')

past_freq = 0
prev_lines = deque(maxlen=10)


def follow():
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.025)
            continue
        line = float(line.strip('\n'))
        if line != 0 and abs(line - past_freq) > 25:
            prev_lines.append(line)
        yield line, prev_lines

for line, prev_lines in follow():
    print prev_lines

    if 550 < line and len(prev_lines) > 1:
        commands.write(str(list(prev_lines)) + '\n')
        commands.flush()
        os.fsync(commands.fileno())
        prev_lines = deque(maxlen=10)
        time.sleep(.5)
    f.seek(0, os.SEEK_END)
    past_freq = line

# while True:
#     line = f.readline()
#     if not line:
#         time.sleep(0.025)
#         continue
#     line = line.strip('\n')
#     line = float(line)
#     print line
#     # if 1300 < line < 1400:
#     # if abs(line - past_freq > 100):
#     if line == 0:
#         vol = 0
#         # line = 100
#     else:
#         vol = .5
#     osc.play_frequencies(stream, .02, vol, 80, 80,
#                          line,
#                          line * 3/2
#                          # # line +2,
#                          # # line -2,
#                          # # line / 2 * 3/2,
#                          # line / 4,
#                          )
#     # if 1000 < line < 1100:
#     #     if abs(line - past_freq > 100):
#     #         osc.play_frequencies(stream, 1, .5, 40000, 40000,
#     #                              # line / 4,
#     #                              # line /4 + 1,
#     #                              line + 100,
#     #                              # line * 11/8,
#     #                              # line * 6/5,
#     #                              # line * 4/3,
#     #                              )
#     past_freq = line
#
