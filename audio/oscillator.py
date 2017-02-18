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

    for freq in freqs:
        chunks = []
        chunks.append(sine(freq, length, 44100))
        chunk = numpy.concatenate(chunks) * volume

        fade = 10000.

        fade_in = numpy.arange(0., 1., 1/fade)
        fade_out = numpy.arange(1., 0., -1/fade)

        chunk[:fade] = numpy.multiply(chunk[:fade], fade_in)
        chunk[-fade:] = numpy.multiply(chunk[-fade:], fade_out)

        allTones.append(chunk)

    chunk = sum(allTones)

    stream.write(chunk.astype(numpy.float32).tostring())

