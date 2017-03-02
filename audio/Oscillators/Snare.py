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

        noise = self.generate_noise()
        noise_length = len(noise)

        waveform[0:50] = signal.sawtooth(waveform[0:50]) / random.choice([1500, 1700, 1900])
        waveform[20:noise_length + 20] = waveform[20:noise_length + 20] + noise / random.choice([100, 200, 300])

        attack = random.choice([200, 330, 200, 250])
        decay = length - 25

        fade_in = np.arange(0., 1., 1./attack)
        fade_log = self.fade_log(decay, 20)

        waveform[:attack] = np.multiply(waveform[:attack], fade_in)
        waveform[-decay:] = np.multiply(waveform[-decay:], fade_log)

        fade_out = np.arange(1., 0., -1./200)
        waveform[-200:] = np.multiply(waveform[-200:], fade_out)


        rand = random.randint(1, 10)
        if rand == 1:
            return np.zeros(len(waveform))

        rand = random.randint(1, 20)
        if rand == 2:
            return self.make_late(waveform, 1000)

        return waveform

    @staticmethod
    def generate_noise():
        noise_length = random.choice([1000, 900, 750, 1000, 1100, 500])
        noise = np.random.normal(0, 1, noise_length)
        noise[-20:] = noise[-20:]/100
        return noise

    @staticmethod
    def fade_log(length, reduce_by):
        return np.logspace(1., 0., length, endpoint=True) / reduce_by

    @staticmethod
    def make_late(arr, num):
        arr=np.roll(arr, num)
        if num > 0:
            np.put(arr, range(len(arr)+ num, len(arr)), np.zeros(1))
        elif num > 0:
            np.put(arr, range(num), np.zeros(1))
        return arr

