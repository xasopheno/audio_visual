from __future__ import division
import numpy
import pyaudio
from collections import deque, Counter
import aubio
import os.path
import asyncio
import websockets
import sys
from websocket import create_connection
import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
# audio_file = current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav'
from Midi.NoteToMidi import sendMidi
# wf = wave.open(audio_file, 'rb')


class StreamToData:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 256, 44100)
        self.pDetection.set_unit("midi")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.5)

        self.output_file = open('Detection/output.txt', 'w')

        self.volume_threshold = 100
        self.acceptable_confidence = 0.61

        self.past_freq = 0
        self.predicted_frequency = 0
        self.set = {0}


    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = round(volume, 6) * 10 ** 5

        confidence = self.pDetection.get_confidence()

        # if volume < self.volume_threshold:
        #     self.predicted_frequency = 0
        # else:
        self.predicted_frequency = prediction

        prediction = round(self.predicted_frequency)
        print(prediction)
        self.past_freq = prediction

        # self.output_file.write(str(self.predicted_frequency) + '\n')
        # self.output_file.flush()
        # os.fsync(self.output_file.fileno())

        return in_data, pyaudio.paContinue


class Generator:
    def __init__(self):
        self.subdivision = 0.01
        self.isZero = True
        self.counter = 0
        self.current_value = 0
        self.detector = StreamToData()
        self.p = pyaudio.   PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=44100,
                                  frames_per_buffer=2048,
                                  input=True,
                                  output=False,
                                  stream_callback=self.detector.callback)

    def generate_set(self):
        prev_lines = 0
        while True:
            pred = self.detector.predicted_frequency
            prev_lines = int(round(pred))
            self.current_value = prev_lines
            self.play_current_value()

    def play_midi(self, value):
        sendMidi(value, .001)

    def play_silence(self):
        # print(0)
        time.sleep(self.subdivision * 1.0)

    def play_current_value(self):
        self.counter += 1
        print (self.current_value)
        if self.counter % 100 == 0:
            with open("midiOutput.txt", 'a') as myfile:
                if self.current_value > 90:
                    self.current_value = 0
                if self.current_value is not 0 and self.isZero is True:
                    self.isZero = False
                    myfile.write(str(self.current_value) + ' ')
                elif self.current_value is 0 and self.isZero is False:
                    myfile.write(str(self.current_value) + ' ')
                    self.isZero = True
                else:
                    myfile.write(str(self.current_value) + ' ')

                if self.current_value is not 0:
                    self.play_midi(self.current_value)
                    end = time.time()
                    # print('value: ', end - start)
                else:
                    self.play_silence()
                    end = time.time()
                    # print('_zero: ', end - start)

if __name__ == '__main__':
    generator = Generator()
    generator.generate_set()

