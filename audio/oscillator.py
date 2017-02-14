from __future__ import division
from math import pi
import numpy

def sine(frequency, length, rate):
    """produces sine accross np array"""

    length = int(length * rate)
    factor = float(frequency) * (pi * 2) / rate
    waveform = numpy.sin(numpy.arange(length) * factor)
    # waveform = numpy.round(waveform, 1)
    return waveform

def play_frequencies(stream, length, volume, *freqs):
    """Plays a group of frequencies"""

    allTones = []
    x = 1
    for freq in freqs:
        chunks = []
        chunks.append(sine(freq, length, 44100))
        chunks = numpy.concatenate(chunks) * volume
        allTones.append(chunks)
    chunk = sum(allTones)

    stream.write(chunk.astype(numpy.float32).tostring())
