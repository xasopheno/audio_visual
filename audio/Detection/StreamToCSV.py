from __future__ import division
import numpy
import pyaudio
from collections import deque, Counter
import aubio
import os.path
import sys
import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
from Midi.NoteToMidi import sendMidi


class StreamToFrequency:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("midi")
        # self.pDetection.set_silence(-40)
        # self.pDetection.set_tolerance(.40)

        self.output_file = open('Detection/output.txt', 'w')

        self.volume_threshold = 1
        # self.acceptable_confidence = 0.05

        self.past_freq = 0
        self.predicted_frequency = 0

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = round(volume, 6) * 10 ** 5
        # print(volume)
        confidence = self.pDetection.get_confidence()

        if volume < self.volume_threshold:
            # or \
                        # volume < self.volume_threshold:
            self.predicted_frequency = 0
        else:
            self.predicted_frequency = prediction

        prediction = round(self.predicted_frequency)
        self.past_freq = prediction

        # self.output_file.write(str(self.predicted_frequency) + '\n')
        # self.output_file.flush()
        # os.fsync(self.output_file.fileno())

        return in_data, pyaudio.paContinue


class Generator:
    def __init__(self):
        self.subdivision = 100/44100
        self.isZero = True
        self.sample_counter = 0
        self.note_counter = 1
        self.last_value = 0
        self.detector = StreamToFrequency()
        self.pred_set = deque(maxlen=9)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=44100,
                                  frames_per_buffer=2048,
                                  input=True,
                                  output=False,
                                  stream_callback=self.detector.callback)

    def generate_set(self):
        while True:
            pred = self.detector.predicted_frequency
            print('pred:', pred)
            value = int(round(pred))
            # self.pred_set.append(value)
            self.play_value(value)

    def play_midi(self, value):
        if value == 0:
            time.sleep(.00001)
        else:
            sendMidi(value, .00001)
        # sendMidi(value - 7, .01)
        # sendMidi(value * 1.5, .001)


    # def play_silence(self):
        # print(0)
        # time.sleep(self.subdivision * 1.0)

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

    def play_value(self, value):
        pass

        # with open("midiOutput.txt", 'a') as myfile:
        #     print(value)
        #     # if value == self.last_value:
            #     self.note_counter += 1
            # else:
            #     stored_value = str(self.last_value)
            #     if self.note_counter < 3000 or self.last_value > 100:
            #         stored_value = str(0)
            #     # print(self.last_value, self.note_counter)
            #     # self.play_midi(self.last_value)
            #     myfile.write(stored_value + ',' + str(self.note_counter) + '\n')
            #     self.note_counter = 1
            #
            #     # print(value == self.last_value)
            #
            # self.last_value = value

if __name__ == '__main__':
    generator = Generator()
    generator.generate_set()
