from __future__ import division
import numpy as np
from scipy import signal


class WaveForm:
    def __init__(self):
        self.sample_rate = 48000

    def sine_wave(self, frequency, length):
        """produces sine across np array"""

        length = int(length * self.sample_rate)
        factor = float(frequency) * (np.pi * 2) / self.sample_rate
        form = np.arange(length) * factor
        waveform = np.sin(form)
        waveform += np.power(waveform, 3)

        return waveform

    def square_wave(self, frequency, length):
        length = int(length * self.sample_rate)
        factor = float(frequency) * (np.pi * 2) / self.sample_rate
        form = np.arange(length) * factor

        pulse_width = np.sin(form)

        return signal.square(form, duty=(pulse_width + 1)/2)

    @staticmethod
    def gibbs_square(waveform, gibbs_value):
        for i in range(1, gibbs_value, 2):
            waveform += np.sin(waveform)/i

        return waveform
