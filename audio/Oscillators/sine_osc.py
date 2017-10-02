from __future__ import division
from math import pi
import numpy as np
# from Filters.butter_bandpass_filter import butter_bandpass_filter
import random
import matplotlib.pyplot as plt


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
        waveform3 = np.power(rounded_waveform, 4)

        # return np.add(waveform, np.add(waveform, waveform2))
        # pre_filtered = np.add(waveform, waveform3)
        # pre_filtered = np.add(pre_filtered, waveform2)

        # filtered = butter_bandpass_filter(pre_filtered, frequency, 2000, 44100, order=5)

        # return pre_filtered
        onetwo = np.add(waveform, waveform2)

        return np.add(onetwo, waveform3)

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""
        volume *= .25
        all_tones = []

        for freq in freqs:
            if freq > 1000:
                volume = volume * .80902
            chunks = [self.wave(freq, length, self.sample_rate)]

            if freq > 3000:
                volume *= .92
            # chunks = butter_bandpass_filter(chunks, freq, random.choice([3000, 4000]), 44100, order=5)
            #
            chunk = np.concatenate(chunks) * volume

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            first_noise = np.random.normal(0, .0045, len(chunk[:attack]))
            second_noise = np.random.normal(0, .0045, len(chunk[-decay:]))

            in_noise = np.multiply(first_noise, np.flipud(fade_in))
            out_noise = np.multiply(second_noise, np.flipud(fade_out))

            chunk[:attack] = np.add(chunk[:attack], in_noise)
            chunk[-decay:] = np.add(chunk[-decay:], out_noise)

            chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

            all_tones.append(chunk)

        chunk = sum(all_tones)
        #
        # plt.plot(chunk)
        # plt.show()

        stream.write(chunk.astype(np.float32).tostring())
