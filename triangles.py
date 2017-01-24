from __future__ import division
import os
from os import system
from math import pi
import numpy
import pyaudio
from random import shuffle, randint
import time
from fractions import Fraction

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

def sine(frequency, length, rate):
    "produces sine accross np array"
    """
    frequency: frequency in hertz
    length: length of tone in seconds,
    rate: sample rate
    """
    length = int(length * rate)
    factor = float(frequency) * (pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)

def play_frequencies(stream, length, volume, *freqs):
    "Plays a group of frequencies"
    """
    stream: PyAudio stream
    length: tone length in seconds
    volume: 0.5 is good starting place
    *freq: any number of frequencies

    example: 
    play_frequencies(stream, 2, 300, 400, 500)
    will play the tones 300hz, 400hz, 500hz simultaneously 
        for two seconds. A major triad. 
    """
    allTones = []
    x = 1
    for freq in freqs:
        chunks = []
        chunks.append(sine(freq, length, 44100)) 
        chunks = numpy.concatenate(chunks) * volume
        allTones.append(chunks)
    chunk = sum(allTones)

    stream.write(chunk.astype(numpy.float32).tostring())

def check_for_relationship(frequency1, frequency2, relationship, duration):
    "Checks for given ratio."
    """
    Frequency relationships are rounded to two decimal places. 
    Increased accuracy of three decimals places might be
    preferable in the context of video.
    """ 
    print round((frequency1) / (frequency2), 3)
    if round((frequency1/frequency2), 3) == relationship or round((frequency2/frequency1), 3) == relationship:
        print frequency1, frequency2, abs(frequency1-frequency2), frequency1+frequency2, Fraction(relationship)
        play_frequencies(
                        stream, 
                        duration, 
                        .085, 
                        frequency1, 
                        frequency2, 
                        abs(frequency1-frequency2),
                        (frequency1+frequency2)/2,
                        )

def generate_test_array():
    "Randomized test array"
    freqs = []
    for frequency1 in range(300, 800):
        for frequency2 in range (300, 800):
            freqs.append((frequency1, frequency2))
    shuffle(freqs)
    return freqs

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=sample_rate, output=1)

    test_freqs = generate_test_array()

    for frequency1, frequency2 in test_freqs:
        # time.sleep(.001)
        """
        You may need to round to 3 didgets in check_for_relationships
            to get some ratios to work.  
        """
        # check_for_relationship(frequency1, frequency2, (3/2), 3.2)
        check_for_relationship(frequency1, frequency2, (5/4), 1.6)
        check_for_relationship(frequency1, frequency2, (7/6), 3.2)
        check_for_relationship(frequency1, frequency2, (7/4), 1.6)
        # check_for_relationship(frequency1, frequency2, (9/8), 3.2)
        check_for_relationship(frequency1, frequency2, (15/8), 3.2)
        check_for_relationship(frequency1, frequency2, (11/8), 3.2)
    # cmd = 'python triangles.py'
    # os.system(cmd)    

p.close
