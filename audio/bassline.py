import pyaudio
import random
import time

from oscillator import Oscillator

osc = Oscillator()

def bassline():
    frequency = random.choice([70, 70, 62, 74])
    volume = .25
    length = random.choice([4, 6.472, 6.472, 6.427, 10.472, 10.472,])
    for i in range(1000000):
        osc.play_frequencies(
            stream,
            length,
            volume,
            random.choice([170000, 14000, 10000]),
            random.choice([2000, 10000]),
            frequency,
            random.choice([frequency * 2,
                           frequency * 3/2 * 2,
                           frequency * 9/8 * 2,
                           frequency * 5/2 * 2,
                           frequency * 7 / 6 * 2,
                           frequency * 11/8 * 2,
                           frequency * 15/8 * 2]),

                           random.choice([frequency * 2,
                           frequency * 3/2 * 3,
                           frequency * 9/8 * 3,
                           frequency * 5/2 * 3,
                           frequency * 7 / 6 * 3,
                           frequency * 11/8 * 3,
                           frequency * 15/8 * 3])
        )
        time.sleep(1)

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

bassline()



