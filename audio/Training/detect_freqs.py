from __future__ import division

import numpy
from numpy import argmax, log
from numpy.fft import rfft
from scipy.signal import kaiser
import math
import audioop

from Oscillators.sine_osc import SineOsc
from Filters.butter_bandpass_filter import butter_bandpass_filter
from parabolic import parabolic
from Normalizing.StreamGenerator import *

RATE = 44100
RECORD_SECONDS = 5
CHUNKSIZE = 1024

osc = SineOsc()

sg = StreamGenerator()
stream = sg.input_stream_generator()
stream2 = sg.output_stream_generator()


def get_cycle_length(signal, fs):
    """Estimate frequency from peak of FFT
    Pros: Accurate, usually even more so than zero crossing counter
    (1000.000004 Hz for 1000 Hz, for instance).  Due to parabolic
    interpolation being a very good fit for windowed log FFT peaks?
    https://ccrma.stanford.edu/~jos/sasp/Quadratic_Interpolation_Spectral_Peaks.html
    Accuracy also increases with signal length
    Cons: Doesn't find the right value if harmonics are stronger than
    fundamental, which is common.
    """
    N = len(signal)

    # Compute Fourier transform of windowed signal
    windowed = signal * kaiser(N, 100)
    f = rfft(windowed)
    # Find the peak and interpolate to get a more accurate peak
    i_peak = argmax(abs(f))  # Just use this value for less-accurate result
    i_interp = parabolic(log(abs(f)), i_peak)[0]

    # Convert to equivalent frequency
    return round(fs * i_interp / N, 0)

frequencies = []
frames = []
past_freq = 0

for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)
    vol = math.sqrt(abs(audioop.avg(data, 4)))

    frame = numpy.fromstring(data, dtype=numpy.int16)
    frame = butter_bandpass_filter(frame, 100, 2000, RATE, order=5)
    # frames.append(frame)

    cycle_length = get_cycle_length(frame, RATE)

    if vol > 4500:
        print vol

    # print cycle_length

    if abs(cycle_length - past_freq) < 50 and vol > 4500:
        frequencies.append(cycle_length)
    else:
        frequencies.append(0)
    past_freq = cycle_length

# numpydata = numpy.hstack(frames)
#
# wav.write('out.wav', RATE, numpydata)
#

for freq in frequencies:

    osc.play_frequencies(stream2, CHUNKSIZE/RATE, 1, 100, 100, freq,
                         freq / 2,
                         freq * 3/2,
                         freq * 2,
                         freq * 7/4)
    print freq


# close stream
stream.stop_stream()
stream.close()
p.terminate()
