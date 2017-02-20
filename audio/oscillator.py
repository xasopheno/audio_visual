from __future__ import division
from math import pi
import numpy as np

def wave(frequency, length, rate):
    """produces sine across np array"""

    length = int(length * rate)
    factor = float(frequency) * (pi * 2) / rate
    waveform = np.sin(np.arange(length) * factor)

    # waveform = np.round(waveform)

    waveform2 = np.power(waveform, 3)

    # return waveform2
    return np.add(waveform, waveform2)

def play_frequencies(stream, length, volume, *freqs):
    """Plays a group of frequencies"""

    allTones = []

    for freq in freqs:
        chunks = []
        chunks.append(wave(freq, length, 44100))
        chunk = np.concatenate(chunks) * volume

        attack = 150000.
        decay = 10000.

        fade_in = np.arange(0., 1., 1/attack)
        fade_out = np.arange(1., 0., -1/decay)

        chunk[:attack] = np.multiply(chunk[:attack], fade_in)
        chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

        allTones.append(chunk)

    chunk = sum(allTones)

    stream.write(chunk.astype(np.float32).tostring())


# propertysOfATone = [
#         length: 1,
#         volume: 10,
#         attack: 1000,
#         decay:
#     ]
