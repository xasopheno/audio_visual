from __future__ import division
import argparse
import numpy
import pyaudio
import aubio
import os.path
import sys
import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
# audio_file = current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav'
from Midi.NoteToMidi import sendMidi
# wf = wave.open(audio_file, 'rb')
import math


class StreamToFrequency:
    def __init__(self, show_volume=False):
        self.show_volume=show_volume
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("midi")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.4)

        self.output_file = open('Detection/output.txt', 'w')

        self.volume_threshold = 6
        self.acceptable_confidence = 1

        self.predicted_values = {'note': 0, 'volume': 0}

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = self.scale_velocity(volume)



        if self.show_volume:
            self.__display_volume(volume)

        self.predicted_values["volume"] = volume

        # if volume < self.volume_threshold:
        #     self.predicted_values["note"] = 0
        # else:
        self.predicted_values["note"] = prediction

        return in_data, pyaudio.paContinue

    @staticmethod
    def __display_volume(volume):
        print(str(volume) + ' ' + "-" * (int(volume / 100)))

    @staticmethod
    def scale_velocity(volume):
        volume = round(volume, 6) * 10 ** 3
        volume = math.log(volume)
        volume *= 15
        if volume > 127:
            volume = 127
        if volume < 0:
            volume = 0

        return volume


class Generator:
    def __init__(self, arguments):
        self.arguments = arguments
        self.subdivision = 0.1
        self.isZero = True
        self.counter = 0
        self.last_note = 0
        self.volume_array = [0]
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
        while True:
            pred = self.detector.predicted_values

            pred['count'] = self.counter
            pred['note'] = int(round(pred["note"]))
            pred['volume'] = int(round(pred["volume"]))

            if self.arguments.display_prediction:
               print(pred)
            self.play_set(pred)

    def avg_volume(self):
        length = len(self.volume_array)
        total = sum(self.volume_array)
        avg = total/length
        return avg

    def play_midi(self, value, volume):
        if value == 0:
            time.sleep(self.subdivision * 1.0)
        for i in range(2):
            sendMidi(value, self.subdivision /5, volume)

    def play_set(self, predicted_values):
        note = predicted_values["note"]
        volume = predicted_values["volume"]

        self.play_midi(note, volume)

        # with open("midiOutput.txt", 'a') as myfile:
        if note == self.last_note:
            self.counter += 1
            self.volume_array.append(volume)
        else:
            predicted_values["volume"] = self.avg_volume()
            print(note, self.counter)

            self.volume_array = [0]
            self.counter = 1

        self.last_note = note

def get_user_options():
    a = argparse.ArgumentParser()
    a.add_argument("--volume",
                   help = "Specify if input volume should be displayed.",
                   dest = "display_volume",
                   required=False,
                   default=False,
                   type=bool,
                   nargs=1)

    a.add_argument("--values",
                   help="Specify if prediction values should be displayed).",
                   dest = "display_prediction",
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
