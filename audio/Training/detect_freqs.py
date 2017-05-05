from __future__ import division
import numpy
import math
import audioop

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Detection.Detector import Detector
from Oscillators.sine_osc import SineOsc
from Normalizing.StreamGenerator import *
from Filters.butter_bandpass_filter import butter_bandpass_filter

RATE = 44100
RECORD_SECONDS = 5
CHUNKSIZE = 1024
THRESHOLD = 1000

osc = SineOsc()
detector = Detector()

sg = StreamGenerator()
stream = sg.input_stream_generator()
stream2 = sg.output_stream_generator()

frequencies = [0]
past_freq = 0

last_three_freqs = numpy.zeros(1)

print('listening...')
for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)
    vol = math.sqrt(abs(audioop.avg(data, 4)))

    frame = numpy.fromstring(data, dtype=numpy.int16)
    # frame = butter_bandpass_filter(frame, 50, 2200, RATE, order=5)

    # cycle_length = Detector.aubio_detector(frame)
    cycle_length, volume = detector.aubio_detector(stream.read(CHUNKSIZE))

    if abs(cycle_length - past_freq) < 100 and vol > THRESHOLD:
        pred_freq = cycle_length
    else:
        pred_freq = 0

    past_freq = cycle_length

    last_three_freqs = numpy.roll(last_three_freqs, 1)
    last_three_freqs[0] = pred_freq

    avg_freq = numpy.average(last_three_freqs[numpy.nonzero(last_three_freqs)])

    if pred_freq == 0 or frequencies[-1] == 0:
        if pred_freq != 0:
            pred_freq = int(round(pred_freq))
        frequencies.append(pred_freq)
        print ('')
    else:
        rounded = int(round(avg_freq))
        frequencies.append(rounded)
        print (rounded, int(volume * 1500) * '-')


if __name__ == '__main__':
    past_freq = 0
    for freq in frequencies:

        osc.play_frequencies(stream2, CHUNKSIZE/RATE, .1, 70, 70,
                             freq,
                             )
        if freq == 0:
            print ('')
        else:
            print (int(round(freq)))
        past_freq = freq
    frequencies = numpy.asarray(frequencies)
    print frequencies

# close stream
stream.stop_stream()
stream.close()
