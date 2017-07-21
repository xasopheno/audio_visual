import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import time
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
    sine_osc.play_frequencies(stream, tempo, .7, 800, 200,
                              freq,
                              freq,
                              freq * 3/2,
                              freq * 3/2,
                              freq * 3/2,
                              freq * 3/2 + 3,
                              freq * 3/2 - 3,
                              freq * 3/2 + 2,
                              freq * 3/2 - 2,
                              # freq * 3/2 + 9,
                              # freq * 3/2 - 9
                              # )
                              )


def idea_2(freq, tempo):
    sine_osc.play_frequencies(stream, tempo, .09, 500000, 800000,
                              # freq /4 - 2,
                              # freq /4 - 2,
                              # freq /4 + 2,
                              freq /2,
                              freq /2 - 2,
                              freq /2 + 2,
                              freq /2 + 2,
                              freq /2 * 3,
                              freq /2 * 3,
                              # freq,
                              # # freq * 3/2,
                              # freq * 3/2 - 3.2,
                              # freq * 3/2 + 3.2,
                              # freq * 5/4,
                              # freq * 3/2 - 2,
                              # freq * 9/4 + 2,
                              # freq * 9/2,
                              # freq * 30/8,
                              # freq * 30/8 - 3.2,
                              # freq * 36/8 + 3.2,
                              # freq * 20/4,
                              # freq * 23/4,
                              # freq * 23/4 + 3.2,
                              # freq * 33/8,
                              # freq * 44/8
                              )

if __name__ == '__main__':
    # time.sleep(50)
    idea_2(131, 10)
    # time.sleep(20)
    idea_2(131, 10)
    # time.sleep(60)
    idea_2(143, 10)
    # time.sleep(20)
    idea_2(131, 10)
    # time.sleep(20)
    idea_2(196, 50)
    # time.sleep(10)
    idea_2(131, 45)
    # time.sleep(20)
    idea_2(131, 40)
    # time.sleep(.5)

# for i in range(4):
#     freq = 190
#     for i in range(3):
#         freq += random.choice([-6, -10, -20, -30, 20])
#         freq2 = 190
#         for i in range(13):
#             idea(freq2, .045)
#             freq2 += 14
#         idea(freq, 1.2)
#     for i in range(22):
#         idea(freq2, .03)
#         freq2 -= 13.9
#     for i in range(30):
#         idea(freq2, .022)
#         freq2 += 3
#     for i in range(18):
#         idea(freq2, .02)
#         freq2 -= 3
#     for i in range(20):
#         idea(freq2, .02)
#         freq2 += 3
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 -= 4
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 += 3
#     for i in range(5):
#         idea(freq2, .02)
#         freq2 -= 4
#     for i in range(5):
#         idea(freq2, .02)
#         freq2 += 5
#     for i in range(4):
#         idea(freq2, .02)
#         freq2 -= 4
#     for i in range(4):
#         idea(freq2, .02)
#         freq2 += 4
#
#     for i in range(20):
#         idea(freq2, .02)
#         freq2 -= 1
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 -= 2
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 += 2
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 -= 2
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 += 9
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 -= 7
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 += 8
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 -= 7
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 += 8
#     for i in range(10):
#         idea(freq2, .02)
#         freq2 -= 7
#     for i in range(10):
#         idea(freq2, .02)
#     freq2 += 12

# idea_2(190, 8)
# idea_2(180, 8)
# idea_2(170, 8)
# idea_2(160, 8)
