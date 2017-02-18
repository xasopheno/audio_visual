#!/usr/bin/python
import math
import numpy
import pyaudio
import matplotlib.pyplot as plt


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = (float(frequency) * (math.pi * 2) / rate)
    waveform = numpy.sin(numpy.arange(length) * factor)
    return waveform


def play_tone(stream, frequency, length, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    fade = 250.

    fade_in = numpy.arange(0., 1., 1/fade)
    fade_out = numpy.arange(1., 0., -1/fade)

    chunk = numpy.concatenate(chunks) * 0.25
    chunk[:fade] = numpy.multiply(chunk[:fade], fade_in)
    chunk[-fade:] = numpy.multiply(chunk[-fade:], fade_out)

    rampOut = chunk[-1000:]
    print rampOut.shape

    stream.write(chunk.astype(numpy.float32).tostring())

def doit():
    frequency1 = 700
    frequency2 = 250
    for i in range(2):
        play_tone(stream, frequency1, 2)
        play_tone(stream, frequency2, 2)

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

