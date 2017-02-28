from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

from .Bassdrum import WaveForm

w = WaveForm()


class Generator:
    def __init__(self):
        pass

    @staticmethod
    def play_frequencies(length, volume, *freqs):
        """Plays a group of frequencies"""
        all_tones = []

        for freq in freqs:
            # attack = 200
            # delay = length

            waveform = w.sine_wave(freq, length)

            chunk = np.concatenate([waveform])

            chunk = np.multiply(chunk, volume)

            # fade_in = np.arange(0., 1., 1./attack)
            # fade_out = np.arange(1., 0., -1./decay)
            #
            # chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            # chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)
            #
            all_tones.append(chunk)

        sum_all_tones = sum(all_tones)

        # plt.plot(sum_all_tones)
        # plt.show()

        return sum_all_tones.astype(np.float32).tostring()
