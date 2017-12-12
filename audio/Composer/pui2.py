import random
import pyaudio
from clear_osc import SineOsc
import multiprocessing as mp
import time

osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )



class Opening:
    def __init__(self):
        self.root = 120
        self.length = 1.5
        self.volume = .5
        self.attack = 8000
        self.decay = 1000
    
    def bassi(self):
        print ('bass')
        freq = self.root
        volume = self.volume
        length = self.length
        attack = self.attack
        decay = self.decay
        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq,
                     )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 9 / 8,
                     )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 5 / 4,
                     )


        osc.play(stream, length, volume, attack, decay,
                 freq * 4 / 3,
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 9 / 8,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq,
                 )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 3 / 2,
                     )

        # ______________________________________


        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 4 / 3,
                     )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 5 / 4,
                     )

        volume /= 2
        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 9 / 8,
                     )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq,
                     )

        volume *= 2
        osc.play(stream, length, volume, attack, decay,
                 freq * 2,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 2 * 9 / 8,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 2 * 5 / 4,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 2 * 4 / 3,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 4 / 3,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2,
                 )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 5 / 3,
                     )

        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 2,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 4 / 3,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2 / 2,
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq,
                 )

    def viola(self):
        print ('viola')
        freq = self.root * 2
        volume = self.volume
        length = self.length
        attack = self.attack
        decay = self.decay

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 5 / 4,
                     )

        for i in range(2):
            osc.play(stream, length, volume, attack, decay,
                     freq * 9 / 8,
                     )


        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8 / 2,
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 9 / 8
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 5 / 4
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 3 / 2
                 )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 15 / 8
                     )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 2
                 )

        volume /= 2
        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 5 / 3
                     )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 3 / 2
                 )

        volume *= 2
        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 4 / 3
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 2
                 )

        osc.play(stream, length * 2, volume, attack, decay,
                 freq * 4 / 3 * 2
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 5 / 4 * 2
                 )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 5 / 3
                     )


        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8
                 )

        osc.play(stream, length * .75, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length * .25, volume, attack, decay,
                 freq * 4 / 3
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 5 / 4
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 5 / 3
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 9 / 8
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 5 / 4
                 )


    # ______________________________________

    def violino2(self):
        print ('violino2')
        freq = self.root * 2
        volume = self.volume
        length = self.length
        attack = self.attack
        decay = self.decay
        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 3 / 2,
                     )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 4 / 3,
                     )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 5 / 4,
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 5 / 3,
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 4 / 3,
                 )

        osc.play(stream, length / 2, volume, attack, decay,
                 freq * 3 / 2,
                 )


        osc.play(stream, length / 2, volume, attack, decay,
                 freq * 2,
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 15 / 8,
                 )

        # ______________________________________

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 9 / 8,
                     )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 5 / 4,
                 )

        volume /= 2
        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq * 15 / 8 / 2,
                     )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq,
                 )

        volume *=2
        osc.play(stream, length, volume, attack, decay,
                 freq * 5 / 4
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 4 / 3
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length * 2, volume, attack, decay,
                 freq
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8 / 2
                 )

        for i in range(3):
            osc.play(stream, length, volume, attack, decay,
                     freq
                     )

        osc.play(stream, length * 2, volume, attack, decay,
                 freq * 9 / 8
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq
                 )

        osc.play(stream, length * 2, volume, attack, decay,
                 freq
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq
                 )

    def violino1(self):
        print ('violino1')
        freq = self.root * 4
        volume = self.volume
        length = self.length
        attack = self.attack
        decay = self.decay
        osc.play(stream, length * 4, volume, attack, decay,
                 freq,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8 / 2,
                 )


        osc.play(stream, length * .75, volume, attack, decay,
                 freq * 5 / 3 / 2,
                 )

        osc.play(stream, length * .25, volume, attack, decay,
                 freq * 3 / 2 / 2,
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 3 / 2 / 2,
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 5 / 3 / 2,
                 )

        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8 / 2,
                 )

        osc.play(stream, length * .25, volume, attack, decay,
                 freq
                 )

        osc.play(stream, length * .25, volume, attack, decay,
                 freq * 9 / 8
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 5 / 4
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 9 / 8
                 )

        # ______________________________________

        volume /= 2
        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 5 / 3
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 3 / 2
                 )

        # time.sleep(1)
        volume *= 2
        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 4 / 3
                 )


        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 5 / 4
                 )

        # time.sleep(1)

        # _____________________________________

        osc.play(stream, length, volume, attack, decay,
                 freq * 2
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 2
                 )


        osc.play(stream, length, volume, attack, decay,
                 freq * 15 / 8
                 )

        osc.play(stream, length * 1.5, volume, attack, decay,
                 freq * 5 / 3
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length * 1.5, volume, attack, decay,
                 freq * 3 / 2
                 )

        for i in range(2):
            osc.play(stream, length * .5, volume, attack, decay,
                     freq * 25 / 18
                     )
            osc.play(stream, length * .5, volume, attack, decay,
                     freq * 3 / 2
                     )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 25 / 18
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq * 3 / 2
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 4 / 3
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq * 5 / 4
                 )

        osc.play(stream, length * 1.5, volume, attack, decay,
                 freq * 9 / 8
                 )

        osc.play(stream, length * .5, volume, attack, decay,
                 freq
                 )

        osc.play(stream, length * 3, volume, attack, decay,
                 freq
                 )


if __name__=='__main__':
    mp.set_start_method('spawn')
    opening = Opening()
    p1 = mp.Process(target=opening.bassi)
    p1.start()
    p2 = mp.Process(target=opening.viola)
    p2.start()
    p3 = mp.Process(target=opening.violino2)
    p3.start()
    p4 = mp.Process(target=opening.violino1)
    p4.start()
