import random
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import pyaudio

from Oscillators.sine_osc import SineOsc

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                frames_per_buffer=6615)


def bassline():
    frequency = random.choice([70, 70, 62, 74])
    other_melody = frequency*5
    volume = .05
    length = .1
    for i in range(2):
        sine_osc.play_frequencies(
            stream,
            length,
            volume,
            random.choice([100]),
            random.choice([100]),
            other_melody,
            other_melody + 3,
            other_melody - 3,
            other_melody + 5,
            other_melody - 5,
            other_melody + 10,
            other_melody - 10,
            other_melody + 6,
            other_melody - 6,
            other_melody/2,
        )

        random.choice([
            sine_osc.play_frequencies(
                stream,
                length,
                .1,
                random.choice([200]),
                random.choice([200]),
                other_melody,
                other_melody *11/8,
                other_melody/3,
                other_melody/4,),
            sine_osc.play_frequencies(
                stream,
                length,
                .15,
                random.choice([200]),
                random.choice([200]),
                other_melody/3,
            ),
        ])

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody,
            other_melody *11/8,
            other_melody/3,
            other_melody/4,

            random.choice([frequency * 5,
                           frequency * 5/2 * 5,
                           frequency * 7 / 4 * 5])
        )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody,
            other_melody *3/2,
            other_melody/4,
        )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 7/6,
            )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            frequency,
            frequency / 2,
            )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            frequency,
            frequency / 3,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 2,
            other_melody * 4/3
            )


        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 3/2,
            other_melody * 5/4,
            other_melody * 3/2 / 2,
        )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 3/2,
            other_melody * 5/4,
            other_melody * 3/2 / 2,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            frequency,
            frequency / 3,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 2,
            other_melody * 4/3
        )

        # good ___

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 3/2,
            other_melody * 5/4,
            other_melody * 3/2 / 2,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 3/2,
            other_melody * 5/4,
            other_melody * 3/2 / 2,
            )
        sine_osc.play_frequencies(
            stream,
            length,
            volume,
            random.choice([100]),
            random.choice([100]),
            other_melody,
            other_melody + 3,
            other_melody - 3,
            other_melody + 5,
            other_melody - 5,
            other_melody + 10,
            other_melody - 10,
            other_melody + 6,
            other_melody - 6,
            other_melody/2,
            )

        random.choice([
            sine_osc.play_frequencies(
                stream,
                length,
                .1,
                random.choice([200]),
                random.choice([200]),
                other_melody,
                other_melody *11/8,
                other_melody/3,
                other_melody/4,),
            sine_osc.play_frequencies(
                stream,
                length,
                .15,
                random.choice([200]),
                random.choice([200]),
                other_melody/3,
                ),
        ])

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody,
            other_melody *11/8,
            other_melody/3,
            other_melody/4,

            random.choice([frequency * 5,
                           frequency * 5/2 * 5,
                           frequency * 7 / 4 * 5])
        )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody,
            other_melody *3/2,
            other_melody/4,
            )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 7/6,
            )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            frequency,
            frequency / 2,
            )

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            frequency,
            frequency / 3,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 2,
            other_melody * 4/3
        )
        # good ___

        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 3/2,
            other_melody * 5/4,
            other_melody * 3/2 / 2,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 3/2,
            other_melody * 5/4,
            other_melody * 3/2 / 2,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            frequency,
            frequency / 3,
            )
        sine_osc.play_frequencies(
            stream,
            .1,
            .1,
            random.choice([200]),
            random.choice([200]),
            other_melody * 2,
            other_melody * 4/3
        )

        for i in range(400, 440):
            sine_osc.play_frequencies(
                stream,
                .01,
                .29,
                200,
                200,
                i
        )


if __name__ == '__main__':
    bassline()




