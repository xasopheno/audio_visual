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
            chunk = np.multiply(chunk, volume) /2
            # chunk += np.power(chunk, 2)
            # chunk += np.round(chunk, 10)

            all_tones.append(chunk)

        sum_all_tones = sum(all_tones)

        plt.plot(sum_all_tones)
        plt.show()

        return sum_all_tones.astype(np.float32).tostring()
