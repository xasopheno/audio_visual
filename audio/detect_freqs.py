from __future__ import division
import pyaudio
import numpy
import scipy.io.wavfile as wav

from numpy import argmax, mean, diff, log

from scipy.signal import blackmanharris, fftconvolve
from matplotlib.mlab import find
import butter_bandpass_filter
from parabolic import parabolic
from Oscillators.sine_osc import SineOsc

RATE = 44100
RECORD_SECONDS = 15
CHUNKSIZE = 2048

osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

stream2 = p.open(format=pyaudio.paFloat32,
                 channels=1, rate=RATE, output=2)


def get_cycle_length(sig, fs):
    """
    Estimate frequency using autocorrelation
    """

    # Calculate autocorrelation (same thing as convolution, but with
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
    peak = argmax(corr[start:]) + start
    px, py = parabolic(corr, peak)

    return round(fs / px, 0)

frequencies = []
frames = []

for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
    data = stream.read(CHUNKSIZE)
    frame = numpy.fromstring(data, dtype=numpy.int16)
    frame = butter_bandpass_filter.butter_bandpass_filter(frame, 60, 2000, RATE, order=5)
    frames.append(frame)
    cycle_length = get_cycle_length(frame, RATE)
    print cycle_length
    # osc.play_frequencies(stream2, .0249, 1, 100, 100, cycle_length)
    frequencies.append(cycle_length)


# numpydata = numpy.hstack(frames)
#
# wav.write('out.wav', RATE, numpydata)
#
for freq in frequencies:
    osc.play_frequencies(stream2, .0249, 1, 100, 100, freq)
    print freq


# close stream
stream.stop_stream()
stream.close()
p.terminate()
