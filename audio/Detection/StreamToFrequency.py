from __future__ import division
import numpy
import pyaudio
from collections import deque, Counter
import aubio
import os.path
import asyncio
import websockets
import sys
import random
from websocket import create_connection
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
# audio_file = current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav'
# from Midi.NoteToMidi import sendMidi
# wf = wave.open(audio_file, 'rb')
from Oscillators.sine_osc import SineOsc






class StreamToFrequency:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("Hz")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.95)

        self.output_file = open('Detection/output.txt', 'w')

        self.volume_threshold = 300
        self.acceptable_confidence = 0.3

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

        if confidence < self.acceptable_confidence or volume < self.volume_threshold:
            self.predicted_frequency = 0
        else:
            self.predicted_frequency = prediction

        prediction = round(self.predicted_frequency)
        # print(prediction)
        self.past_freq = prediction

        # self.output_file.write(str(self.predicted_frequency) + '\n')
        # self.output_file.flush()
        # os.fsync(self.output_file.fileno())

        return in_data, pyaudio.paContinue


class Generator:
    def __init__(self):
        self.set = {0}
        self.detector = StreamToFrequency()
        self.p = pyaudio.PyAudio()
        self.sine_osc = SineOsc()

        self.play = pyaudio.PyAudio()
        self.play_stream = self.play.open(format=pyaudio.paFloat32,
                                          channels=1,
                                          rate=44100,
                                          output=1,
                                          )

        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=44100,
                                  frames_per_buffer=2048,
                                  input=True,
                                  output=False,
                                  stream_callback=self.detector.callback)

    def generate_set(self):
        prev_lines = deque(maxlen=1)
        while True:
            pred = self.detector.predicted_frequency
            prev_lines.append(int(round(pred)))
            # print (prev_lines)
            # print (set(prev_lines))
            self.set = set(prev_lines)
            self.play_set(self.set)

    def play_set(self, bagOfNotes):
        print(bagOfNotes)
        for value in bagOfNotes:
            if value < 2000:
                self.sine_osc.play(self.play_stream, .015, .5, 100, 100,
                                   # value * 3/4,
                                               # value / 2 + 2,
                                               # value,
                                               # value + 3,
                                               value * 5 / 4,
                                   value * 3 / 2,
                                   value * 9 / 4,
                                   value * 4,
                                   # value * 4 - 3,
                                   )

                # for value in bagOfNotes:
                #     if value != 0:
                #         sendMidi(value, .07)
                #         sendMidi(value + 7, .07)
                #         sendMidi(value + 12, .07)
                # sendMidi(value + 4, .001)
                #     # sendMidi(value, .01)
                #     # sendMidi(value, .01)
                #     # sendMidi(value + 11, .001)
                #     # sendMidi(value - 10, 0.001)
                #     # sendMidi(value, .001)
                #     # sendMidi(value + 6, .001)
                #     # sendMidi(value, .001)

                # def arpeggiate_set(self, bagOfNotes):

if __name__ == '__main__':
    generator = Generator()
    generator.generate_set()
