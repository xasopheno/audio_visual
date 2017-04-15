from __future__ import division

import numpy
import math
import audioop
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

sg = StreamGenerator()
stream = sg.input_stream_generator()
stream2 = sg.output_stream_generator()


def get_cycle_length(sig, fs):
    """Estimate frequency using autocorrelation

        Pros: Best method for finding the true fundamental of any repeating wave,
        even with strong harmonics or completely missing fundamental

        Cons: Not as accurate, currently has trouble with finding the true peak

        """
    # Calculate circular autocorrelation (same thing as convolution, but with
    # one input reversed in time), and throw away the negative lags
    corr = fftconvolve(sig, sig[::-1], mode='full')
    corr = corr[len(corr)//2:]

    # Find the first low point
    d = diff(corr)
    start = find(d > 0)[0]

    # Find the next peak after the low point (other than 0 lag).  This bit is
    # not reliable for long signals, due to the desired peak occurring between
    # samples, and other peaks appearing higher.
    # Should use a weighting function to de-emphasize the peaks at longer lags.
    # Also could zero-pad before doing circular autocorrelation.
    peak = argmax(corr[start:]) + start
    px, py = parabolic(corr, peak)

    return int(round(fs / px, 0))

frequencies = []
frames = []
past_freq = 0

last_ten_freqs = numpy.zeros(10)

for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)
    vol = math.sqrt(abs(audioop.avg(data, 4)))

    frame = numpy.fromstring(data, dtype=numpy.int16)
    frame = butter_bandpass_filter(frame, 100, 2000, RATE, order=5)
    # frames.append(frame)

    cycle_length = get_cycle_length(frame, RATE)

    if abs(cycle_length - past_freq) < 80 and vol > 4000:
        pred_freq = cycle_length
        print '-'
    else:
        pred_freq = 0
    past_freq = cycle_length
    # print cycle_length

    last_ten_freqs = numpy.roll(last_ten_freqs, 1)
    last_ten_freqs[0] = pred_freq

    avg_freq = numpy.average(last_ten_freqs[numpy.nonzero(last_ten_freqs)])

    if pred_freq == 0:
        frequencies.append(pred_freq)
    else:
        frequencies.append(avg_freq)
    print frequencies[-1]



# numpydata = numpy.hstack(frames)

# wav.write('out.wav', RATE, numpydata)


for freq in frequencies:

    osc.play_frequencies(stream2, CHUNKSIZE/RATE, 1, 100, 100, freq,
                         freq / 2,
                         freq * 3/2,
                         freq * 2,
                         freq * 7/4
                         )
    print freq


# close stream
stream.stop_stream()
stream.close()
p.terminate()
