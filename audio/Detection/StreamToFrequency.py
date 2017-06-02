from __future__ import division
import numpy
import pyaudio
import aubio
import os.path
import wave

import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
audio_file = current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav'

wf = wave.open(audio_file, 'rb')


class StreamToFrequency:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("Hz")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.85)
        self.threshold = 500

        self.output = open('Detection/output.txt', 'w')
        self.past_freq = 0
        self.pred_freq = 0
        self.wf = wave.open(audio_file, 'rb')

        self.last_three_freqs = numpy.zeros(3)

    def callback(self, in_data, frame_count, time_info, status):

        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        cycle_length = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = round(volume, 6) * 100000

        confidence = self.pDetection.get_confidence()
        if abs(cycle_length - self.past_freq) < 100 and volume > self.threshold:
            self.pred_freq = cycle_length
        else:
            self.pred_freq = 0

        # if confidence < .4:
        #     self.pred_freq = 0

        print (self.pred_freq, round(confidence, 3))

        self.past_freq = cycle_length

        self.output.write(str(self.pred_freq) + '\n')
        self.output.flush()
        os.fsync(self.output.fileno())

        return in_data, pyaudio.paContinue

    def stream_reader(self, stream):
        while stream:
            pass
        stream.close()
        self.output.close()

    def print_frequency(self):
        print (self.pred_freq)

if __name__ == '__main__':
    detector = StreamToFrequency()
    p = pyaudio.PyAudio()

    print (p.get_device_info_by_index(1)["name"])

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    frames_per_buffer=2048,
                    input=True,
                    # output=True,
                    stream_callback=detector.callback)

    detector.stream_reader(stream)
