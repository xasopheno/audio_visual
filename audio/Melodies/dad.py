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
    sine_osc.play_frequencies(stream, tempo, .09 / 2, 10000*tempo, 20000*tempo,
                              freq /4 - 2,
                              freq /4 - 2,
                              freq /4 + 2,
                              freq /2,
                              freq /2 - 2,
                              freq /2 + 2,
                              freq /2 + 2,
                              freq /2 * 3,
                              freq /2 * 3,
                              freq,
                              freq * 3/2,
                              freq * 3/2 - 3.2,
                              freq * 3/2 + 3.2,
                              freq * 5/4,
                              freq * 3/2 - 2,
                              freq * 9/4 + 2,
                              freq * 9/2,
                              freq * 30/8,
                              freq * 30/8 - 3.2,
                              freq * 36/8 + 3.2,
                              freq * 20/4,
                              freq * 23/4,
                              freq * 23/4 + 3.2,
                              freq * 33/8,
                              freq * 44/8
                              )

if __name__ == '__main__':
    freq = 131
    idea_2(freq, 3)
    # time.sleep(20)
    freq = freq * 5/6
    idea_2(freq, 2)
    idea_2(freq * 9/8, 2)
    # time.sleep(60)
    idea_2(143, 2)
    # time.sleep(20)
    idea_2(131, 8)
    freq = 196
    idea_2(freq, 3)
    idea_2(freq * 8/9, 1)
    idea_2(freq * 3/4, 1)
    idea_2(131, 2)
    idea_2(120, 2)
    idea_2(140, 2)
    idea_2(155, 1)
    idea_2(138, 1)
    idea_2(131, 2)
    idea_2(131, 2)
    idea_2(131, 6)
    freq = 740
    idea_2(freq, 3)
    freq = 131
    idea_2(freq * 3/2,8)
    idea_2(freq, 4)
    time.sleep(4)
    idea_2(freq * 4/3, 4)
    idea_2(freq,9)

    freq = 740
    idea_2(freq, 3)
    freq = 131
    idea_2(freq * 3/2,8)
    idea_2(freq, 5)
    time.sleep(5.5)
    idea_2(freq * 4/3, 4)
    idea_2(freq,10)

    time.sleep(37)

    freq = 740
    idea_2(freq, 3)
    freq = 131
    idea_2(freq * 3/2, 10)
    idea_2(freq, 8)
    time.sleep(4)
    # idea_2(freq * 4/3, 4)
    # idea_2(freq,10)




    # # time.sleep(10)
    # idea_2(131, 20)
    # # time.sleep(20)
    # idea_2(131, 40)
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
