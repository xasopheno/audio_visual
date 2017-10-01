from math import sin,pi
import pyaudio
import struct

def play_binaural(left_freq=200, right_freq=460):
    #set some vars
    sampwidth   = 2
    frate       = 44100.0
    amp         = 8000.0
    channels    = 2
    periods     = 50
    data_size = int((frate/left_freq)*(frate/right_freq)) * periods
    audio_string = ""
    audio_string2 = ""

    #setup pyaudio and stream
    PyAudio = pyaudio.PyAudio
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(sampwidth),rate=int(frate),output=True,channels=channels)

    #generate audio data
    for x in range(data_size):
        left = (sin(2*pi*(right_freq / 4 + 2)) + sin((2*pi*right_freq + 20)*(x/frate)) / 2 + sin((2*pi*right_freq - 22 / 2)))
        right = (sin(2*pi*(right_freq / 4 + 2) *(x/frate)) + sin((2*pi*right_freq * 11/8 / 2)*(x/frate))  / 2 + sin((2*pi*right_freq * 7/4 / 2)*(x/frate))) + left / 4
        left = left + right / 4
        audio_string += struct.pack("hh",left*amp/2,right*amp/2)
        audio_string2 += struct.pack("hh",right*amp/2, left*amp/2)


    print "playing"

    i = 1
    while True:
        if i % 2 == 0:
            stream.write(audio_string)
        else:
            stream.write(audio_string2)
        i += 1

    #cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()

play_binaural()
