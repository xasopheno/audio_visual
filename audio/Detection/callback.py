from __future__ import division
import numpy
import pyaudio
import time

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import aubio


class StreamToFrequency:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("Hz")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.85)
        self.frequency = 0

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        pitch = self.pDetection(samples)[0]
        self.frequency = pitch
        self.print_frequency()
        return in_data, pyaudio.paContinue

    @staticmethod
    def stream_reader(stream):
        time.sleep(10)
        stream.close()

    def print_frequency(self):
        print (self.frequency)


detector = StreamToFrequency()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=48000,
                frames_per_buffer=2048,
                input=True,
                output=False,
                stream_callback=detector.callback)

detector.stream_reader(stream)
