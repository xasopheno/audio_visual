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
        noise = np.random.normal(0, 1, 30)

        fade_out = np.logspace(1., 0., 19200, endpoint=True)
        # waveform[0:20] = np.zeros(20)

        waveform[0:30] = signal.sawtooth(waveform[0:30]) / 30
        waveform[50:80] = waveform[50:80] + noise / 50

        waveform[-19200:] = waveform[-19200:] * fade_out
        return waveform
