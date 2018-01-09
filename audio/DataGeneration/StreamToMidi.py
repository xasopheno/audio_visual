import os.path
import argparse
import numpy
import pyaudio
import math
import aubio
import shutil
import sys
import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
from Midi.MidiPlayer import MidiPlayer

class StreamToFrequency:
    def __init__(self, show_volume=False, store=None):
        self.terminal_width = self.get_screen_width()
        self.store = store
        self.show_volume=show_volume
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("midi")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.4)

        self.output_file = open('Detection/output.txt', 'w')

        self.volume_threshold = 6
        self.acceptable_confidence = 1

    def get_screen_width(self):
        width = shutil.get_terminal_size((80, 20)).columns
        return width

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = int(self.pDetection(samples)[0])

        volume = numpy.sum(samples ** 2) / len(samples)

        self.store.note = prediction
        self.store.volume = volume

        if self.show_volume:
            self.__display_volume(volume)

        return in_data, pyaudio.paContinue

    def __display_volume(self, volume):
        width = self.terminal_width
        bar = ' ' + "-" * (int(volume * 100))
        if len(bar) > width - 20:
            bar = ' ' + "-" * (width - 20)
        print(str(volume) + bar)

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


class Store:
    def __init__(self):
        self.__note = 0
        self.__volume = 0
        self.length = 1

        self.volume_array = []

    @property
    def note(self):
        return self.__note

    @property
    def volume(self):
        return self.__volume

    @note.setter
    def note(self, note):
        note = int(note)
        self.__note = note

    @volume.setter
    def volume(self, volume):
        volume = self.scale_volume(volume)
        volume = int(volume)
        self.volume_array.append(volume)
        self.__volume = volume

    @property
    def values(self):
        return {
            "note": self.note,
            "volume": self.avg_volume(),
            "length": self.length,
        }

    def inc_length(self):
        self.length += 1

    @staticmethod
    def scale_volume(volume):
        volume = round(volume, 6) * 10 ** 3
        volume = math.log(volume)
        volume *= 15
        if volume > 127:
            volume = 127
        if volume < 0:
            volume = 0

        return volume

    def reset(self):
        self.length = 1
        self.volume_array = []

    def avg_volume(self):
        length = len(self.volume_array)
        total = sum(self.volume_array)
        avg = total/length if length else 0
        return int(avg)


class Generator:
    def __init__(self, args=None, store=None):
        self.arguments = args
        self.subdivision = 0.1
        self.isZero = True
        self.counter = 1
        self.past_pred = 0
        self.show_prediction = args.display_prediction

        self.volume_array = []

        self.detector = StreamToFrequency(store=store, show_volume=args.display_volume)
        self.store = store
        self.player = MidiPlayer(synth='Volca')

        self.p = pyaudio.   PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=44100,
                                  frames_per_buffer=2048,
                                  input=True,
                                  output=False,
                                  stream_callback=self.detector.callback)

    def get_store_values(self):
        while True:
            pred = self.store.values

            if self.store.note == self.past_pred:
                self.store.inc_length()
            else:
                self.store.reset()

            self.past_pred = self.store.note

            self.play_value(pred)

    def play_midi(self, value, volume):
        if value == 0:
            time.sleep(self.subdivision * 1.0)
        else:
            for i in range(2):
                self.player.play(value, self.subdivision /3, volume)

    def play_value(self, predicted_values):
        note = predicted_values["note"]
        volume = predicted_values["volume"]

        if self.show_prediction:
            print(predicted_values)

        self.play_midi(note, volume)


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

    store = Store()
    generator = Generator(args=args, store=store)

    generator.get_store_values()
