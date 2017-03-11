from __future__ import division
from math import pi
import numpy as np
import matplotlib.pyplot as plt

class Oscillator:

    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""


        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        rounded_waveform = np.round(waveform, 0)

        waveform2 = np.power(waveform, 3)
        waveform3 = np.power(rounded_waveform, 4)/4


        # return waveform
        # waveform = np.add(rounded_waveform, waveform)
        return np.add(waveform, waveform2, waveform3)

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""

        allTones = []

        for freq in freqs:
            if freq > 1000:
                volume = volume * .80902
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
        # plt.plot(chunk[1200:3000])
        # plt.show()


        stream.write(chunk.astype(np.float32).tostring())
