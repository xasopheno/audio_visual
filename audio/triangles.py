from __future__ import division
import pyaudio
import random
from random import shuffle
from fractions import Fraction
import numpy as np

from Oscillators.Generator import Generator

osc2 = Generator()


def check_for_relationship(frequency1, frequency2, relationship, length):
    """Checks for given ratio."""
    """
    Frequency relationships are rounded to two decimal places. 
    Increased accuracy of three decimals places might be
    preferable in the context of video.
    """ 
    print(round(frequency1 / frequency2, 3))
    print (frequency1, frequency2, Fraction(relationship))

    if round((frequency1/frequency2), 3) == relationship or round((frequency2/frequency1), 3) == relationship:

        waveform = osc2.play_frequencies(
            length,
            .5/15,
            100,
            110000,
            frequency1,
            frequency2,
            frequency1 + 5,
            frequency1 - 5,
            frequency2 + 3,
            frequency2 - 3,
            abs(frequency1-frequency2),
            frequency1+frequency2,
            3 * (frequency1+frequency2)/2/2 + 5
        )

        stream.write(waveform)


def generate_test_array():
    """"Randomized test array"""
    freqs = []
    for vector1 in range(250, 400):
        for vector2 in range(250, 400):
            freqs.append((vector1, vector2))
    shuffle(freqs)
    return freqs

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=48000, output=1)

    test_freqs = generate_test_array()

    for frequency1, frequency2 in test_freqs:
        """
        You may need to round to 3 didgets in check_for_relationships
            to get some ratios to work.  
        """
        # check_for_relationship(frequency1, frequency2, (3/2), 3.2)
        # check_for_relationship(frequency1, frequency2, (5/4), 5)
        # check_for_relationship(frequency1, frequency2, (6/5), 5)
        check_for_relationship(frequency1, frequency2, (7/4), 3)
        check_for_relationship(frequency1, frequency2, (9/8), 3)
        check_for_relationship(frequency1, frequency2, (15/8), 3)
        # check_for_relationship(frequency1, frequency2, (11/8), 5)

    p.close
