from __future__ import division
from math import pi
import numpy as np
import random
# import matplotlib.pyplot as plt

class SineOsc:

    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        rounded_waveform = np.round(waveform, 0)

        waveform2 = np.power(waveform, 3)
        # waveform3 = np.power(rounded_waveform, 4)/4

        # waveform4 = waveform

        return rounded_waveform


    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""
        all_tones = []
        volume = volume

        for freq in freqs:
            wave = [self.wave(freq, length, self.sample_rate)]
            waveform = (np.concatenate(wave) * volume / 6)

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            waveform[:attack] = np.multiply(waveform[:attack], fade_in)
            waveform[-decay:] = np.multiply(waveform[-decay:], fade_out)

            all_tones.append(waveform)

        all_tones = sum(all_tones)

        # plt.plot(chunk[])
        # plt.show()

        return stream.write(all_tones.astype(np.float32).tostring())
