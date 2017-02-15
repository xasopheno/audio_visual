#!/usr/bin/python
import math
import numpy
import pyaudio
import matplotlib.pyplot as plt

global PHASE
PHASE = 0

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = (float(frequency) * (math.pi * 2) / rate)
    waveform = numpy.sin(numpy.arange(length) * factor)
    return waveform

def play_tone(stream, frequency, length, rate=44100):
    global PHASE
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25
    plt.plot(chunk)
    plt.show()
    print 'start ', chunk[0:1]
    print 'end ', chunk[-1:]
    PHASE = chunk[-1:]

    stream.write(chunk.astype(numpy.float32).tostring()) 

def doit():
    frequency1 = 700
    frequency2 = 250
    for i in range (1000000):
        play_tone(stream, frequency1, 1)
        play_tone(stream, frequency2, 1)

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

