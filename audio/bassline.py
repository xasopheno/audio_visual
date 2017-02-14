import numpy
import pyaudio
import random
from oscillator import play_frequencies
# numpy.set_printoptions(threshold=numpy.nan)

def bassline():
    frequency = 300
    volume = .25
    for i in range(1000000):
        play_frequencies(
            stream,
            .15,
            volume,
            frequency,
            random.choice([frequency * 2/1, frequency + 5, frequency - 5, frequency, frequency * 3/2]))
        change = random.choice([-75, -75, -7, 7, 1, 2, 3, 4, 100, -125])

        print ('frequency: ', frequency, 'change: ', change, 'volume: ', volume)
        if frequency > 150 or not frequency < 40:
            volume = random.choice([.25, .25, .25, .3, .3, .5, 0, 0])
        else:
            volume = random.choice([.4, .5])

        if frequency < 0:
            frequency = random.choice([50, 100, 200, 300])
        else:
            frequency = frequency + change

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

bassline()


