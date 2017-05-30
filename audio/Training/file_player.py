import os
import sys
from aubio import source, pitch
import pyaudio
import wave

current_path = os.getcwd()
filename = current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav'

p = pyaudio.PyAudio()

wf = wave.open(filename)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

samplerate = 44100
CHUNK = 2048

win_s = 2048  # fft size
hop_s = 2048  # hop size

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.4

pitch_o = pitch("yinfft", win_s, hop_s, samplerate)
pitch_o.set_unit("Hz")
pitch_o.set_tolerance(tolerance)

# total number of frames read
total_frames = 0
prev_pred = 0
data = wf.readframes(CHUNK)
while True:
    samples, read = s()
    pred = pitch_o(samples)[0]
    pitch = int(round(pred))
    confidence = pitch_o.get_confidence()
    if confidence < 0.5:
        pitch = 0.
    if abs(pitch - prev_pred) > 100:
        pitch = 0.
    print("%f %f %f" % (total_frames / float(win_s), pitch, confidence))
    stream.write(data)
    data = wf.readframes(CHUNK)

    prev_pred = pred
    total_frames += read

    if read < hop_s:
        break

