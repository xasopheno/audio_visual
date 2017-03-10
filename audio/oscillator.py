from __future__ import division
from math import pi
import numpy as np
import cv2
import numpy.fft as fft
import matplotlib.pyplot as plt

class Oscillator:

    def __init__(self):
        self.sample_rate = 44100
        self.frame = 1

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        waveform = np.round(waveform)

        waveform2 = np.power(waveform, 4)

        return waveform2
        # return np.add(waveform, waveform2)

    def print_image(self, img):
        file_name = './images/' + str('%04d') % self.frame + '.png'
        self.frame += 1
        cv2.imwrite(file_name, img)
        print 'I made ', str(file_name)

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
