from math import sqrt
import time
from clear_osc import SineOsc
import pyaudio

osc = SineOsc()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for x in range(4, n + 1, 2):
        primes[x] = False

    for x in range(3,int(sqrt(n))+1,2):
        if primes[x]:
            for y in range(x * x, n+1, x):
                primes[y] = False

    return primes

sieve = sieve_of_eratosthenes(100000)
for i in range(len(sieve)):
    if sieve[i]:
        print(i)
        osc.play_frequencies(stream, .03, .5, 400, 500,
                              40,
                              40,
                              50,
                              100,
                              200,
                              500,
                              800,
                              )
    else:
        time.sleep(.03)
    time.sleep(.02)
