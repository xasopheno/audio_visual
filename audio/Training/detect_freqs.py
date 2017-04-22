from __future__ import division

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import numpy
import math
import audioop

from Detection.Detector import Detector

from numpy import argmax, diff
from matplotlib.mlab import find
from scipy.signal import fftconvolve

from Oscillators.sine_osc import SineOsc
from Filters.butter_bandpass_filter import butter_bandpass_filter

from parabolic import parabolic
from Normalizing.StreamGenerator import *

RATE = 44100
RECORD_SECONDS = 5
CHUNKSIZE = 1024

osc = SineOsc()
detector = Detector()

sg = StreamGenerator()
stream = sg.input_stream_generator()
stream2 = sg.output_stream_generator()

frequencies = []
frames = []
past_freq = 0

last_ten_freqs = numpy.zeros(3)

print('recording...')
for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)
    vol = math.sqrt(abs(audioop.avg(data, 4)))

    frame = numpy.fromstring(data, dtype=numpy.int16)
    frame = butter_bandpass_filter(frame, 100, 2000, RATE, order=5)
    # frames.append(frame)

    # cycle_length = Detector.aubio_detector(frame)
    cycle_length, volume = detector.aubio_detector(stream.read(1024))

    if abs(cycle_length - past_freq) < 80 and vol > 100:
        pred_freq = cycle_length
    else:
        pred_freq = 0
    past_freq = cycle_length
    # print cycle_length

    last_ten_freqs = numpy.roll(last_ten_freqs, 1)
    last_ten_freqs[0] = pred_freq

    avg_freq = numpy.average(last_ten_freqs[numpy.nonzero(last_ten_freqs)])

    if pred_freq == 0:
        frequencies.append(pred_freq)
        print ('')
    else:
        frequencies.append(avg_freq)
        # print(int((volume * 10)) * '-')
        # print ( (volume) * 10 )
        print ( int((volume) * 1085) * '-' )
    # print frequencies[-1]



# numpydata = numpy.hstack(frames)

# wav.write('out.wav', RATE, numpydata)

past_freq = 0
for freq in frequencies:
    # if abs(freq - past_freq > 400):
    #     freq = 0
    osc.play_frequencies(stream2, CHUNKSIZE/RATE, 1, 100, 100, freq,
                         # freq / 2,
                         freq,
                         # freq,
                         # freq * 3/2,
                         # freq * 2,
                         # freq * 7/4
                         )

    if freq == 0:
        print ('')
    else:
        print (int(round(freq)))
    past_freq = freq

# close stream
stream.stop_stream()
stream.close()
p.terminate()
