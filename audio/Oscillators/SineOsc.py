from __future__ import division
from math import pi
import numpy as np


class SineOsc:
    def __init__(self):
        self.sample_rate = 44100
        self.waveform = None
        self.length = None
        self.frequency = None
        self.form = None
        self.factor = None

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        self.length = int(length * rate)
        self.factor = float(frequency) * (pi * 2) / self.sample_rate
        self.form = np.arange(self.length) * self.factor
        self.waveform = np.sin(self.form)
        # waveform = np.round(waveform)
        # waveform2 = np.power(self.waveform, 3)
        # self.waveform = abs(self.waveform)

        # return waveform2
        return self.waveform

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""

        allTones = []

        for freq in freqs:
            chunks = []
            chunks.append(self.wave(freq, length, self.sample_rate))
            chunk = np.concatenate(chunks) * volume

            attack = attack
            decay = decay

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

            allTones.append(chunk)

        chunk = sum(allTones)

        stream.write(chunk.astype(np.float32).tostring())
