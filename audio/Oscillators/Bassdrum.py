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
        noise = np.random.normal(0, 1, 100)
        noise[-20:] = noise[-20:]/2

        fade_out = np.logspace(1., 0., length, endpoint=True)
        waveform[-20:] = np.zeros(20)

        waveform[0:30] = signal.sawtooth(waveform[0:30]) / 10
        waveform[20:120] = waveform[20:120] + noise / 30

        waveform[-length:] = (waveform[-length:] * fade_out) / 10

        attack = 200.
        decay = length

        fade_in = np.arange(0., 1., 1./attack)
        # fade_out = np.arange(1., 0., -1./decay)

        waveform[:attack] = np.multiply(waveform[:attack], fade_in)
        waveform[-decay:] = np.multiply(waveform[-decay:], fade_out)

        waveform[-200:]

        return waveform
