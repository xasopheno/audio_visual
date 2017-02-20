from __future__ import division
import pyaudio
from random import shuffle
from fractions import Fraction

from oscillator import play_frequencies

"""
"triangles.py"
Given two vector lengths, if the two lengths are in
    the desired ratio, generate two tones at with 
    frequencies corresponding to vector length. 
    Currently set up to detect Perfect 5ths or the ratio 3/2
Vector lengths should probably be scaled to 
    the range(30, 2000)
A time.sleep() function is slowing down the execution 
    of this script for viewability. 
Using PyAudio for sound. I'm still having a problem with 
    pops due to concantenated audio. Perhaps you can figure
    something out. 
    http://stackoverflow.com/questions/36438850/how-to-remove-pops-from-concatented-sound-data-in-pyaudio
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

        play_frequencies(
                        stream,
                        length,
                        .1,
                        10000,
                        1000,
                        frequency1,
                        frequency2,
                        frequency1 + 5,
                        frequency1 - 5,
                        frequency2 + 3,
                        frequency2 - 3,
                        # # 2 * frequency1 / 3,
                        abs(frequency1-frequency2),
                        frequency1+frequency2,
                        3 * (frequency1+frequency2)/2/2 + 5
                        )

def generate_test_array():
    """"Randomized test array"""
    freqs = []
    for frequency1 in range(250, 400):
        for frequency2 in range(250, 400):
            freqs.append((frequency1, frequency2))
    shuffle(freqs)
    return freqs

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=sample_rate, output=1)

    test_freqs = generate_test_array()

    for frequency1, frequency2 in test_freqs:
        """
        You may need to round to 3 didgets in check_for_relationships
            to get some ratios to work.  
        """
        # check_for_relationship(frequency1, frequency2, (3/2), 3.2)
        # check_for_relationship(frequency1, frequency2, (5/4), 5)
        # check_for_relationship(frequency1, frequency2, (6/5), 5)
        check_for_relationship(frequency1, frequency2, (7/4), 5)
        check_for_relationship(frequency1, frequency2, (9/8), 5)
        check_for_relationship(frequency1, frequency2, (15/8), 5)
        # check_for_relationship(frequency1, frequency2, (11/8), 5)

    p.close
