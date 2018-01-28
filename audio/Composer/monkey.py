import random
import pyaudio
from clear_osc import SineOsc
import multiprocessing as mp
import time
import argparse
import random
from pythonosc import osc_bundle_builder
from pythonosc import osc_message_builder
from pythonosc import udp_client

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.162.21",
                    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8000,
                    help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)


sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

x = 145
freqs = [
    x,
    x * 9/8,
    x * 4/3,
    x * 5/4,

    x * 3/2,
    x * 11/8,
    x * 3/2,
    x * 15/18,

    x * 5/1.5,
    x * 4/6,
    x * 9/4,
    x * 5/4,

    x * 4/1.5,
    x * 6/2,
    x * 15/4,
    x * 6/2,

    x * 4,
    x * 3/2,
    x * 3/2,
    x * 4/3,

    x * 5/4,
    x * 3/2,
    x * 4/3,
    x * 5/4,
    #
    x * 9/8,
    x * 3/2,
    x * 3/2,
    x * 4/3,

    x * 11/8,
    x * 10/4,
    x * 10/4,
    x * 9/4,

    x * 7/4,
    x * 3/2,
    x * 3/2,
    x * 5/3,

    x * 11/8,
    0,
    x * 12/5,
    x * 12/5,

    x * 3/2,
    x * 3/2,
    x * 4/3,
    x * 13/8,
    x * 13/8,
    x * 5/2,
    x * 7/2,
    x * 9/2,
    x * 10/3,
    ]

freqs2 = [
    x * 11/8,
    x * 11/8,
    0,
    x * 12/5,
    x * 12/5,

    x * 3/2,
    x * 3/2,
    x * 4/3,
    x * 13/8,
    x * 13/8,
    x * 5/2,
    x * 7/2,
    x * 9/2,
    x * 10/3,
    ]

timesThroughBach = 2
length = 20

def func1():
    print ('func1')
    for i in range(timesThroughBach):
        for freq in freqs:
            print(freq)

            client.send_message("/coordinates", [float(freq), float(freq), float(freq)])
            sine_osc.play_frequencies(stream, .25, 1, 8000, 1000,
                                      freq,
                                      freq * 2,
                                      freq + 2,
                                      )


#         if i == timesThroughBach - 1:
#             time.sleep(.25)
#         time.sleep(1.9)
#
#     for i in range(length):
#         for freq in freqs2:
#             client.send_message("/func1", freq)
#             sine_osc.play_frequencies(stream, .25, 1, 8000, 1000,
#                                       freq,
#                                       freq * 2,
#                                       freq + 2,
#                                       )
#
# def func2():
#     print ('func2')
#     for i in range(timesThroughBach):
#         for freq in freqs:
#             sine_osc.play_frequencies(stream, .25, 1, 1000, 10000,
#                                       freq * 3/2,
#                                       freq * 3/2 * 2,
#                                       freq * 3/2,
#                                       freq / 2,
#                                       )
#
#         time.sleep(1.9)
#
#     for i in range(length):
#         for freq in freqs2:
#             sine_osc.play_frequencies(stream, .25, 1, 1000, 10000,
#                                       freq * 3/2,
#                                       freq * 3/2 * 2,
#                                       freq * 3/2,
#                                       freq / 2,
#                                       )


if __name__=='__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=func1)
    p1.start()
    # time.sleep(2)
    # p2 = mp.Process(target=func2)
    # p2.start()
    # time.sleep(4)
    # p3 = mp.Process(target=func3)
    # p3.start()
