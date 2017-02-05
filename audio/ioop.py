import pyaudio
import wave
import audioop
import time

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "my_path//a_test_2.wav"


time.sleep(1)

p = pyaudio.PyAudio()

s = p.open(format = FORMAT, 
       channels = CHANNELS,
       rate = RATE,
       input = True, 
       frames_per_buffer = chunk)

d = []

print((RATE / chunk) * RECORD_SECONDS)

print("---recording---")
for i in range(0, (RATE // chunk * RECORD_SECONDS)): 
    data = s.read(chunk)
    mx = audioop.max(data, 2)
    if max_volume > 1000:
      print max_volume

print("---done recording---")

s.close()
p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(d))
# wf.close()
