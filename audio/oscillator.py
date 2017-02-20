from __future__ import division
from math import pi
import numpy as np
import matplotlib.pyplot as plt


def wave(frequency, length, rate):
    """produces sine across np array"""

    length = int(length * rate)
    factor = float(frequency) * (pi * 2) / rate
    waveform = np.sin(np.arange(length) * factor)

    waveform = np.round(waveform)

    waveform2 = np.power(waveform, 3)

    # return waveform
    return np.add(waveform, waveform2)


def play_frequencies(stream, length, volume, attack, decay, *freqs):
    """Plays a group of frequencies"""

    all_tones = []

    for freq in freqs:
        waveform = [wave(freq, length, 44100)]
        chunk = np.concatenate(waveform) * volume

        attack = attack
        decay = decay

        fade_in = np.arange(0., 1., 1./attack)
        fade_out = np.arange(1., 0., -1./decay)

        chunk[:attack] = np.multiply(chunk[:attack], fade_in)
        chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

        all_tones.append(chunk)

    all_tones = sum(all_tones)

    plt.plot(all_tones)
    plt.show()

    stream.write(all_tones.astype(np.float32).tostring())


# propertysOfATone = [
#         length: 1,
#         volume: 10,
#         attack: 1000,
#         decay:
#     ]
