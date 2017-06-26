from __future__ import division
from math import pi
import numpy as np
import random
import os
import scipy.io.wavfile as wav


class SineOsc:
    def __init__(self):
        self.sample_rate = 44100 / 2
        self.sound_data = self.mp3_to_np('./NickyAudio2.mp3')

    def wave(self, frequency, length, rate):
            """produces sine across np array"""

            length_seconds = length

            length = int(length * 2 * rate)
            factor = float(frequency/2) * (pi * 2) / rate
            waveform = \
                random.choice([np.sin(np.arange(length) * factor),
                               np.sin(np.arange(length) * factor * .999),
                               np.sin(np.arange(length) * factor * 1.01)
                               ])

            rounded_waveform = np.round(waveform, 1)

            waveform2 = np.power(waveform, 3)
            waveform3 = np.power(rounded_waveform, 4)/4

            waveform4 = waveform

            for x in np.nditer(waveform4, op_flags=['readwrite']):
                x[...] = random.choice([
                    random.choice([x, x, x, x, x, x, x, x, x, x, x/2]),
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                ])

            start = random.randint(10000, len(self.sound_data[1]) - length)
            if length_seconds < 10:
                sound = self.sound_data[1][start:start + length] * random.choice([1/3000, 0, 0, 0, 0, 0])
            else:
                sound = self.sound_data[1][start:start + length] * random.choice([1/8500])

            return np.add(np.add(waveform, sound.flatten()), np.add(waveform2, waveform4 / 100))


    def mp3_to_np(self, file_name):
        fname = file_name
        temp = 'temp.wav'
        cmd = 'lame --decode {0} {1}'.format(fname, temp)
        os.system(cmd)
        data = wav.read(temp)
        return data

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""
        all_tones = []

        for freq in freqs:
            wave = [self.wave(freq, length, self.sample_rate)]
            waveform = (np.concatenate(wave) * volume)

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            waveform[:attack] = np.multiply(waveform[:attack], fade_in)
            waveform[-decay:] = np.multiply(waveform[-decay:], fade_out)

            all_tones.append(waveform)

        all_tones = sum(all_tones)

        # plt.plot(chunk[])
        # plt.show()

        return stream.write(all_tones.astype(np.float32).tostring())

    def play_multiple_parts(self, stream, *parts):
        all_parts = []
        for part in parts:
            print(part)
            sound = self.play_frequencies(*part)
            all_parts.append(sound)

        all_parts = sum(all_parts)
        print(all_parts)
        stream.write(all_parts.astype(np.float32).tostring())
