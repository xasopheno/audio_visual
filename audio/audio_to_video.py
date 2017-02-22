from __future__ import division
from math import pi
import numpy as np
import cv2
import numpy.fft as fft
import matplotlib.pyplot as plt
from scipy.io.wavfile import write


class GenerateVideo:

    def __init__(self):
        self.sample_rate = 44100
        self.frame = 1

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        # waveform = np.round(waveform)

        waveform2 = np.power(waveform, 3)

        # return waveform2
        return np.add(waveform, waveform2)

    def print_image(self, img):
        file_name = './images/' + str('%04d') % self.frame + '.png'
        self.frame += 1
        cv2.imwrite(file_name, img)
        print 'I made ', str(file_name)

    def print_audio(self, chunk):
        scaled = np.int16(chunk/np.max(np.abs(chunk)) * 32767)
        write('test.wav', 44100, scaled)


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

        self.print_audio(chunk)

        data = chunk
        temporal_window = 3 #seconds

        T = 44100 * 60/(temporal_window) #Cycles per minute

        a = np.abs(fft.rfft(data, n=data.size))[1:]
        freqs = fft.rfftfreq(data.size, d=1./T)[1:]
        freqs = np.divide(1, freqs)

        max_freq = freqs[np.argmax(a)]

        print "Peak found at %s second period (%s minutes)" % (format(max_freq, '.12f' ), format(max_freq*60, '.12f'))

        period_in_samples = (max_freq * 60 * 44100) / 3
        print period_in_samples
        leftover = 1920 - period_in_samples

        for i in range(0, 89):
            print 0 + (period_in_samples * i)
            print period_in_samples * (period_in_samples * i)

            image = np.array([chunk[(0 + (period_in_samples * i)):(period_in_samples + leftover + (period_in_samples * i))], ] * 1080)
            image *= (255.0/image.max())
            self.print_image(image)

