from __future__ import division
import argparse
import numpy
import pyaudio
from collections import deque, Counter
import aubio
import os.path
import asyncio
import sys
import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
# audio_file = current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav'
from Midi.NoteToMidi import sendMidi
# wf = wave.open(audio_file, 'rb')


class StreamToFrequency:
    def __init__(self, show_volume=False):
        self.show_volume=show_volume
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("midi")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.4)

        self.output_file = open('Detection/output.txt', 'w')

        self.volume_threshold = 60
        self.acceptable_confidence = 1

        self.past_freq = 0
        self.predicted_frequency = 0
        self.set = {0}

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = round(volume, 6) * 10 ** 5

        if self.show_volume:
            self.__display_volume(volume)

        if volume < self.volume_threshold:
            self.predicted_frequency = 0
        else:
            self.predicted_frequency = prediction

        prediction = round(self.predicted_frequency)

        self.past_freq = [prediction, volume]

        return in_data, pyaudio.paContinue

    @staticmethod
    def __display_volume(self, volume):
        print(str(volume) + ' ' + "-" * (int(volume / 100)))


class Generator:
    def __init__(self, arguments):
        self.subdivision = 0.07
        self.isZero = True
        self.counter = 0
        self.set = {0}
        self.detector = StreamToFrequency(show_volume=arguments.display_volume)
        self.p = pyaudio.   PyAudio()
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
            self.set = set(prev_lines)
            self.play_set(self.set)


    def play_midi(self, value):
        sendMidi(value, self.subdivision)

    def play_silence(self):
        # print(0)
        time.sleep(self.subdivision * 1.0)


    def play_set(self, bagOfNotes) :
        self.counter += 1
        # print (bagOfNotes)
        if self.counter % 1 == 0:
            start = time.time()
            with open("midiOutput.txt", 'a') as myfile:
                for value in bagOfNotes:
                    if value is not 0 and self.isZero is True:
                        self.isZero = False
                        myfile.write('\n' + str(value) + ' ')
                    elif value is 0 and self.isZero is False:
                        myfile.write('\n' + str(value) + ' ')
                        self.isZero = True
                    else:
                        for value in bagOfNotes:
                            myfile.write(str(value) + ' ')

                    if value is not 0 and 20 < value < 110:
                        self.play_midi(value)
                        end = time.time()
                        # print('value: ', end - start)
                    else:
                        self.play_silence()
                        end = time.time()
                        # print('_zero: ', end - start)


def get_user_options():
    a = argparse.ArgumentParser()
    a.add_argument("--volume",
                   help = "Specify if input volume should be displayed.",
                   dest = "display_volume",
                   required=False,
                   default=False,
                   type=bool,
                   nargs=1)

    a.add_argument("--prediction",
                   help="Specify if midi note prediction should be displayed).",
                   dest = "display_notes",
                   required=False,
                   default=False,
                   type=bool,
                   nargs=1)

    return a.parse_args()

if __name__ == '__main__':
    args = get_user_options()
    print('args: ', args)
    generator = Generator(args)
    generator.generate_set()
