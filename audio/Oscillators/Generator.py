from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import random

# from .Bassdrum import WaveForm
from .Snare import WaveForm

w = WaveForm()

class Generator:
    def __init__(self):
        pass

    @staticmethod
    def play_frequencies(length, *freqs):
        """Plays a group of frequencies"""
        all_tones = []

        for freq in freqs:
            waveform = w.sine_wave(freq, length)
            chunk = np.concatenate([waveform])

            all_tones.append(chunk)

        sum_all_tones = sum(all_tones)

        sum_all_tones = sum_all_tones / [random.choice([1.1, 1.12, 1.13, 1.3, 1.25, 1.2, 1.1, 1.4])]
        #
        # plt.plot(sum_all_tones)
        # plt.show()

        return sum_all_tones.astype(np.float32).tostring()
