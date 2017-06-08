from __future__ import division
from math import pi
import numpy as np
# import matplotlib.pyplot as plt


class SineOsc:

    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        rounded_waveform = np.round(waveform, 1)

        waveform2 = np.power(waveform, 3)
        waveform3 = np.power(rounded_waveform, 4)/4

        return np.add(waveform, np.add(waveform, waveform2))

    def play_frequencies(self, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""
        volume *= .25
        all_tones = []

        for freq in freqs:
            if freq > 1000:
                volume = volume * .80902
            chunks = [self.wave(freq, length, self.sample_rate)]
            chunk = np.concatenate(chunks) * volume

            attack = attack
            decay = decay

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

            all_tones.append(chunk)

        all_tones = sum(all_tones)

        # plt.plot(chunk[])
        # plt.show()

        return all_tones

    def play_multiple_parts(self, stream, *parts):
        all_parts = []
        for part in parts:
            print(part)
            sound = self.play_frequencies(*part)
            all_parts.append(sound)

        all_parts = sum(all_parts)
        print(all_parts)
        stream.write(all_parts.astype(np.float32).tostring())
