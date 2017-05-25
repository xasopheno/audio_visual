import time
import os.path
import sys
import ast
import random
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Oscillators.sine_osc import SineOsc
from Normalizing.StreamGenerator import *


class Musician:
    def __init__(self):
        self.RATE = 44100
        self.CHUNKSIZE = 1024

        self.osc = SineOsc()
        self.sg = StreamGenerator()
        self.stream = self.sg.output_stream_generator()

        self.f = open('Detection/commands.txt', 'r')
        self.f.seek(0, os.SEEK_END)

        self.play = 0
        self.freq_array = []

    def follow(self):
        while True:
            line = self.f.readline()
            if not line:
                self.player(self.freq_array)
                time.sleep(0.025)
                continue
            line = line.strip('\n')
            self.freq_array = ast.literal_eval(line)

    def player(self, freqs):
        for freq in freqs:
            if freq < 1000:
                print freq
                self.osc.play_frequencies(self.stream, .2, 1, 500, 500,
                                          freq / 2,
                                          freq,
                                          freq * 3/2,
                                          freq * 3/4,

                                     )
            # self.f.seek(0, os.SEEK_END)


musician = Musician()
musician.follow()
