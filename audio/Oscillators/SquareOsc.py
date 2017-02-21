from SineOsc import SineOsc
import numpy as np
from math import pi


class SquareOsc(SineOsc):
    def __init__(self):
        self.sample_rate = 44100
        self.waveform = None
        self.length = None
        self.frequency = None
        self.form = None
        self.factor = None
        self.square = 100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        self.length = int(length * rate)
        self.factor = float(frequency) * (pi * 2) / self.sample_rate
        self.form = np.arange(self.length) * self.factor
        self.waveform = np.sin(self.form)

        for i in range(3, self.square, 2):
            self.waveform += np.sin(i*self.form)/i
        # waveform = np.round(waveform)
        # waveform2 = np.power(waveform, 3)
        # return waveform2

        return self.waveform


