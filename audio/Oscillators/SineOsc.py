from __future__ import division
import numpy as np
from SineWave import SineWave

sine = SineWave()

class SineOsc:
    def __init__(self):
        pass

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""

        allTones = []

        for freq in freqs:
            waveform = sine.wave(freq, length)

            chunks = [waveform]

            chunk = np.concatenate(chunks) * volume

            attack = attack
            decay = decay

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            chunk[:attack] = np.multiply(chunk[:attack], fade_in)
            chunk[-decay:] = np.multiply(chunk[-decay:], fade_out)

            allTones.append(chunk)

        sum_all_tones = sum(allTones)

        return sum_all_tones.astype(np.float32).tostring()
