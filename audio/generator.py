import random
import pyaudio
import time

from Oscillators.sine_osc import SineOsc
from Oscillators.sine_osc_with_mp3 import SineOscWithMp3

osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                frames_per_buffer=6615)


def generate_series(*ranges):
    freq_series = []
    length_series = []

    for i in range(0, ranges[0][0]):
        freq = random.randrange(ranges[0][1][0], ranges[0][1][1])
        freq_series.append(freq)
        length = random.uniform(ranges[0][2][0], ranges[0][2][1])
        length_series.append(length)

    print 'freqs: ', freq_series
    print 'lengths', length_series

    return freq_series, length_series


seed = [5, [50, 80], [.3, .8]]
seed2 = [5, [200, 500], [.2, 1]]

for k in range(4):
    freqs, lengths = generate_series(seed)
    freqs2, lengths2 = generate_series(seed2)

    for j in range(0, 8):
        for i in range(0, len(freqs)):
            osc.play_frequencies(stream,
                                 lengths[i],
                                 random.uniform(.5, 1),
                                 2000,
                                 2000,
                                 freqs[i],
                                 freqs[i] * 2,
                                 freqs2[i],
                                 freqs2[i] * random.choice([3/2, 5/4, 7/4, 6/5, 4/3]),
                                 freqs[i] * 2 * random.choice([3/2, 5/4, 7/4, 6/5, 4/3]),
                                 ),

time.sleep(.01)

