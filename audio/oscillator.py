from __future__ import division
from math import pi
import numpy as np

class Oscillator:

    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""


        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        form = np.arange(length) * factor

        waveform = np.sin(form)

        for i in range(3, 25, 2):
            waveform += np.sin(i*form)/i

        # waveform = np.round(waveform)

        waveform2 = np.power(waveform, 3)

        # return waveform2
        return np.add(waveform, waveform2)

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
