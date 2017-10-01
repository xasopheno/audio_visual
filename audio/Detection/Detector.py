from subprocess import call
import aubio
import numpy
from numpy import argmax, diff
from matplotlib.mlab import find
from scipy.signal import fftconvolve
from parabolic import parabolic


class Detector:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("Hz")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.85)

        cmd = 'osascript -e "set volume input volume 100"'
        call(cmd, shell=True)

    def aubio_detector(self, data):
        print ('aubio_detector()')
        samples = numpy.fromstring(data,
                                   dtype=aubio.float_type)

        pitch = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = round(volume, 4)

        return pitch, volume

    @staticmethod
    def auto_correlation(sig, fs):
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
