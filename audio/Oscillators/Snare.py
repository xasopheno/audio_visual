from __future__ import division
import numpy as np
from scipy import signal
from scipy.ndimage.interpolation import shift

import random


class WaveForm:
    def __init__(self):
        self.sample_rate = 48000

    def sine_wave(self, frequency, length):
        late_flag = True

        """produces sine across np array"""

        length = int(length * self.sample_rate)
        factor = float(frequency) * (np.pi * 2) / self.sample_rate
        form = np.arange(length) * factor
        waveform = np.sin(form)

        noise_length = random.choice([1000, 900, 750, 1000, 1100, 500])

        noise = np.random.normal(0, 1, noise_length)
        noise[-20:] = noise[-20:]/100

        fade_log = np.logspace(1., 0., length, endpoint=True) / 120
        # waveform[-20:] = np.zeros(20)

        waveform[0:50] = signal.sawtooth(waveform[0:50]) / random.choice([1500, 1300, 1800])
        waveform[20:noise_length + 20] = waveform[20:noise_length + 20] + noise / random.choice([100, 200, 300])

        # attack = random.choice([200, 330, 150, 180, 200, 250, 300])
        attack = 200
        decay = length

        fade_in = np.arange(0., 1., 1./attack)

        waveform[:attack] = np.multiply(waveform[:attack], fade_in)
        waveform[-decay:] = np.multiply(waveform[-decay:], fade_log)

        fade_out = np.arange(1., 0., -1./200)
        waveform[-200:] = np.multiply(waveform[-200:], fade_out)

        rand = random.randint(1, 10)

        if rand == 1:
            return np.zeros(len(waveform))

        waveform = waveform

        self.make_late(waveform)
        return waveform


    @staticmethod
    def make_late(waveform):
        shift(waveform, 1000, mode='constant', cval=0.0)
