from __future__ import division
import numpy
import pyaudio
import aubio
import os.path

import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


class StreamToFrequency:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("Hz")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.85)
        self.threshold = 5

        self.output = open('Detection/output.txt', 'w')
        self.past_freq = 0
        self.pred_freq = 0

        self.last_three_freqs = numpy.zeros(3)

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        cycle_length = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = round(volume, 3) * 100000

        if abs(cycle_length - self.past_freq) < 100 and volume > self.threshold:
            self.pred_freq = cycle_length
        else:
            self.pred_freq = 0

        self.past_freq = cycle_length

        self.output.write(str(self.pred_freq) + '\n')
        self.output.flush()
        os.fsync(self.output.fileno())

        # self.print_frequency()

        return in_data, pyaudio.paContinue

    def stream_reader(self, stream):
        while stream:
            pass
        stream.close()
        self.output.close()

    def print_frequency(self):
        print (self.pred_freq)

detector = StreamToFrequency()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                frames_per_buffer=2048,
                input=True,
                output=False,
                stream_callback=detector.callback)

detector.stream_reader(stream)
