from __future__ import division

import random
from fractions import Fraction
from random import shuffle

import pyaudio

from Oscillators.sine_osc_with_mp3 import SineOscWithMp3

osc = SineOscWithMp3()

"""
"triangles.py"
Given two vector lengths, if the two lengths are in
    the desired ratio, generate two tones at with 
    frequencies corresponding to vector length.
"""

sample_rate = 44100

def check_for_relationship(frequency1, frequency2, relationship, length):
    """Checks for given ratio."""
    """
    Frequency relationships are rounded to two decimal places. 
    Increased accuracy of three decimals places might be
    preferable in the context of video.
    """ 
    print round((frequency1) / (frequency2), 3)
    print frequency1, frequency2, Fraction(relationship)

    if round((frequency1/frequency2), 3) == relationship or round((frequency2/frequency1), 3) == relationship:

        osc.play_frequencies(
                        stream,
                        length,
                        .8,
                        150000,
                        random.choice([20000,10000,5000]),
                        frequency1,
                        frequency2,
                        frequency1 * 11/8,
                        frequency2 * 7/4,
                        frequency1 + 3,
                        frequency1 - 3,
                        frequency2 + 5,
                        frequency2 - 5,
                        frequency1 * 3/2,
                        # # 2 * frequency1 / 3,
                        # abs(frequency1-frequency2),
                        # frequency1+frequency2,
                        # 3 * (frequency1+frequency2)/2/2 + 5
                        )

def generate_test_array():
    """"Randomized test array"""
    freqs = []
    for frequency1 in range(100, 500):
        for frequency2 in range(100, 500):
            freqs.append((frequency1, frequency2))
    shuffle(freqs)
    return freqs

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=sample_rate, output=2)

    test_freqs = generate_test_array()

    for frequency1, frequency2 in test_freqs:
        """
        You may need to round to 3 didgets in check_for_relationships
            to get some ratios to work.  
        """
        # check_for_relationship(frequency1, frequency2, (3/2), 3.2)
        check_for_relationship(frequency1, frequency2, (5/4), 4.2)
        check_for_relationship(frequency1, frequency2, (6/5), 4)
        check_for_relationship(frequency1, frequency2, (7/4), 4.5)
        # check_for_relationship(frequency1, frequency2, (9/8), 3.2)
        check_for_relationship(frequency1, frequency2, (15/8), 4.1)
        # check_for_relationship(frequency1, frequency2, (11/8), 5)

        # time.sleep(.02618)
    p.close
