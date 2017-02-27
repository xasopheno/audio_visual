import pyaudio
import random
from Oscillators.Generator import Generator

# numpy.set_printoptions(threshold=numpy.nan)

osc = Generator()

def bassline():
    frequency = 200
    volume = .25
    for i in range(1000000):
        if frequency < 60:
            frequency = random.choice([150, 200, 300])
        waveform = osc.play_frequencies(
            random.choice([.1, .1, .1, .1, .1, .1, .1, .2, .2, .2, .2, .2, .3, .3, .3]),
            volume / 4,
            300,
            4000,
            frequency,
            random.choice([frequency * 3/1, frequency * 3/1])
        )
        change = random.choice([-75, -7, 7, 1, 2, 3, 4, 60, -75, -50])

        stream.write(waveform)

        print ('frequency: ', frequency, 'change: ', change, 'volume: ', volume)
        if frequency > 150 or not frequency < 40:

            volume = random.choice([.25, .25, .25, .3, .3, .5, 0])
        else:
            volume = random.choice([.4, .5])

        frequency = frequency + change

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

bassline()



