import pyaudio
import numpy as np
from time import time
import random

CHANNELS = 2
RATE = 44100

TT = time()
freq = 100
newfreq = 100
phase = 0


def callback(in_data, frame_count, time_info, status):
    global TT,phase,freq,newfreq
    if newfreq != freq:
        phase = 2*np.pi*TT*(freq-newfreq)+phase
        freq=newfreq
    left = (np.sin(phase+2*np.pi*freq*(TT+np.arange(frame_count)/float(RATE))))
    data = np.zeros((left.shape[0]*2,),np.float32)
    data[::2] = left
    data[1::2] = left
    TT += frame_count/float(RATE)
    return data / 8, pyaudio.paContinue

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                stream_callback=callback)

stream.start_stream()
start = time()
try:
    while 1:
        now = time()
        if now-start > 1/10:
            newfreq = 300 + np.sin(5 * np.pi * 1/1.5 * now) * 240 #update the frequency This will depend on y on the future
            # print newfreq
        start = now
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
