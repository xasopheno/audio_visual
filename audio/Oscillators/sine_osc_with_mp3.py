from __future__ import division
from math import pi
import numpy as np
import random
import matplotlib.pyplot as plt
from mp3_to_np import mp3_to_np


class SineOscWithMp3:
    def __init__(self):
        self.sample_rate = 44100
        self.sound_data = mp3_to_np('./styx.mp3')

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        start = random.randint(10000, len(self.sound_data[1]) - length)
        sound = self.sound_data[1][start:start + length]
        sound = sound[:, ::2] / random.choice([3000, 3000, 3000, 5000])
        waveform2 = np.power(waveform, 3)

        return np.add(waveform, sound.flatten()) + waveform2

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""
        volume *= .25
        allTones = []

        for freq in freqs:
            chunks = [self.wave(freq, length, self.sample_rate)]
            chunk = np.concatenate(chunks) * volume

            attack = attack
            decay = decay

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

            allTones.append(chunk)

        chunk = sum(allTones)

        # plt.plot(chunk[])
        # plt.show()

        stream.write(chunk.astype(np.float32).tostring())
