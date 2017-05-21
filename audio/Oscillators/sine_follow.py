from __future__ import division
from math import pi, sin
import numpy as np
# import matplotlib.pyplot as plt


class SineOsc:

    def __init__(self):
        self.sample_rate = 44100
        self.phase = 1

    def wave(self, frequency, length, rate):
        """produces sine across np array"""
        numbs = []
        number_of_frames = int(length * rate)
        phaseInc = 2 * pi * frequency / self.sample_rate


        for x in xrange(number_of_frames):
            y = sin(self.phase)
            self.phase += phaseInc
            numbs.append(y)
        # factor = float(frequency) * (pi * 2) / rate
        # waveform = np.sin(np.arange(length) * factor)

            waveform = np.array(numbs)
            print len(waveform)
        return waveform

    def play_frequencies(self, stream, length, volume,  *freqs):
        """Plays a group of frequencies"""
        volume *= .25
        all_tones = []

        for freq in freqs:
            waveform = [self.wave(freq, length, self.sample_rate)]
            waveform = np.concatenate(waveform) * volume

            # attack = attack
            # decay = decay
            #
            # fade_in = np.arange(0., 1., 1./attack)
            # fade_out = np.arange(1., 0., -1./decay)
            #
            # chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            # chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

            all_tones.append(waveform)

        chunk = sum(all_tones)

        # plt.plot(chunk[])
        # plt.show()

        stream.write(chunk.astype(np.float32).tostring())
