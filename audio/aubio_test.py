from subprocess import call
import aubio
import numpy


class Detector:
    def __init__(self):
        self.pDetection = aubio.pitch("default", 2048, 2048//2, 44100)
        self.pDetection.set_unit("Hz")
        self.pDetection.set_silence(-40)

        cmd = 'osascript -e "set volume input volume 20"'
        call(cmd, shell=True)

    def frequency_detector(self, data):
        samples = numpy.fromstring(data,
                                   dtype=aubio.float_type)

        pitch = self.pDetection(samples)[0]

        volume = numpy.sum(samples ** 2) / len(samples)
        volume = "{:.6f}".format(volume)

        return pitch, volume
