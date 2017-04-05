from __future__ import division
import pyaudio
import numpy
import scipy.io.wavfile as wav
from numpy.fft import rfft
from numpy import argmax, log
from scipy.signal import kaiser
import butter_bandpass_filter
from parabolic import parabolic
from Oscillators.sine_osc import SineOsc

RATE = 44100
RECORD_SECONDS = 5
CHUNKSIZE = 2048

osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

stream2 = p.open(format=pyaudio.paFloat32,
                 channels=1, rate=RATE, output=2)


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
past_freq = 0
for freq in frequencies:
    # if freq - freq
    #     freq = past_freq
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
