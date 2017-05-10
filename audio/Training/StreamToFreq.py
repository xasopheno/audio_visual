from __future__ import division
import numpy
import math
import audioop

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Detection.Detector import Detector
from Oscillators.sine_osc import SineOsc
from Normalizing.StreamGenerator import *


class StreamToFreq:
    def __init__(self):
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.CHUNKSIZE = 2048
        self.THRESHOLD = 1000

        self.osc = SineOsc()
        self.detector = Detector()

        self.sg = StreamGenerator()
        self.stream = self.sg.input_stream_generator()
        self.stream2 = self.sg.output_stream_generator()

        self.frequencies = [0]
        self.past_freq = 0
        self.last_three_freqs = numpy.zeros(3)

    def detectorit(self):
        print('listening...')

        for i in range(0, int(self.RATE / self.CHUNKSIZE * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNKSIZE)
            vol = math.sqrt(abs(audioop.avg(data, 4)))

            cycle_length, volume = self.detector.aubio_detector(self.stream.read(self.CHUNKSIZE))

            if abs(cycle_length - self.past_freq) < 100 and vol > self.THRESHOLD:
                pred_freq = cycle_length
            else:
                pred_freq = 0

            self.past_freq = cycle_length

            self.last_three_freqs = numpy.roll(self.last_three_freqs, 1)
            self.last_three_freqs[0] = pred_freq

            avg_freq = numpy.average(self.last_three_freqs[numpy.nonzero(self.last_three_freqs)])

            if pred_freq == 0 or self.frequencies[-1] == 0:
                if pred_freq != 0:
                    pred_freq = int(round(pred_freq))
                self.frequencies.append(pred_freq)
                print ('')
            else:
                rounded = int(round(avg_freq))
                self.frequencies.append(rounded)
                print (rounded, int(volume * 1500) * '-')

    def play_frequencies(self):
        for freq in self.frequencies:
            self.osc.play_frequencies(self.stream2, self.CHUNKSIZE/self.RATE, .1, 70, 70,
                                      freq,
                                     )
            if freq == 0:
                print ('')
            else:
                print (int(round(freq)))
            self.past_freq = freq
        frequencies = numpy.asarray(self.frequencies)
        print frequencies

        # close stream
        self.stream.stop_stream()
        self.stream.close()
        self.stream2.stop_stream()
        self.stream2.close()

if __name__ == "__main__":
    detect = StreamToFreq()

    detect.detectorit()
    detect.play_frequencies()
