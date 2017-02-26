from __future__ import division
from math import pi
import numpy as np


class SineWave:
    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length):
        """produces sine across np array"""

        length = int(length * self.sample_rate)
        factor = float(frequency) * (pi * 2) / self.sample_rate
        form = np.arange(length) * factor
        waveform = np.sin(form)

        return waveform
