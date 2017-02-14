#!/usr/bin/python
import math
import numpy
import pyaudio
from os import system
import random
import time

global PHASE
PHASE = 0

def sine(frequency, length, rate):
    global PHASE
    length = int(length * rate)
    factor = (float(frequency) * (math.pi * 2) / rate)
    waveform = numpy.sin(numpy.arange(length) * factor)
    return waveform

def play_tone(stream, frequency, length, rate=44100):
    global PHASE
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25
    print 'start ', chunk[0:1]
    print 'end ', chunk[-1:]
    PHASE = chunk[-1:]

    stream.write(chunk.astype(numpy.float32).tostring()) 

def doit():
    global PHASE
    frequency = 100
    for i in range (1000000):
        play_tone(stream, frequency, 1)
        change = -100
        print frequency
        if frequency < 200:
            frequency = 200
        else:
            frequency = frequency + change

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)


doit()



#     

# import numpy as np
# from scipy.io.wavfile import write

# data = np.random.uniform(-100,100,444100) # 44100 random samples between -1 and 1
# scaled = np.int16(data/np.max(np.abs(data)) * 32767)
# write('test.wav', 44100, scaled)

