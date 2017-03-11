import pyaudio
import random
import time

from oscillator import Oscillator

osc = Oscillator()

def bassline():
    frequency = random.choice([70, 70, 62, 74])
    melody = frequency * 5 * random.choice([3/2, 5/4, 7/6, 9/8, 4/3])
    otherMelody = frequency*5
    volume = .05
    length = .1
    # length = random.choice([4, 6.472, 6.472, 6.427, 10.472, 10.472,]) * 1.2
    for i in range(1000000):
        osc.play_frequencies(
            stream,
            length,
            volume,
            random.choice([100]),
            random.choice([100]),
            # frequency,
            otherMelody,
            otherMelody + 3,
            otherMelody - 3,
            otherMelody + 5,
            otherMelody - 5,
            otherMelody + 10,
            otherMelody - 10,
            otherMelody + 6,
            otherMelody - 6,
            #
            otherMelody/2,
        )

        random.choice([
            osc.play_frequencies(
                stream,
                length,
                .1,
                random.choice([200]),
                random.choice([200]),
                # frequency,
                otherMelody,
                otherMelody *11/8,
                otherMelody/3,
                otherMelody/4,),
            osc.play_frequencies(
                stream,
                length,
                .15,
                random.choice([200]),
                random.choice([200]),
                otherMelody/3,
            ),
            # osc.play_frequencies(
            #     stream,
            #     length,
            #     0,
            #     random.choice([200]),
            #     random.choice([200]),
            #     otherMelody/3,
            #     )
        ])

        # osc.play_frequencies(
        #     stream,
        #     1,
        #     .1,
        #     random.choice([200]),
        #     random.choice([200]),
        #     # frequency,
        #     otherMelody,
        #     otherMelody *11/8,
        #     otherMelody/3,
        #     otherMelody/4,
        #
        #     random.choice([frequency * 5,
        #                    frequency * 5/2 * 5,
        #                    frequency * 7 / 6 * 5])
        # )

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=1,
                    frames_per_buffer=6615)

bassline()



