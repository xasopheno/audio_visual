import os.path
import sys
import numpy as np
import glob
import re
import wave
import pyaudio
import aubio
from collections import deque

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

OUTPUT_DIR = './training_data/_training_input'
THRESHOLD = 1000
current_path = os.getcwd()
NUM_PAST_FREQS = 5

def predict_freq_from_wav(full_audio_path, chunk_size, num_chunks):
    index = 0
    audio_file_name = os.path.splitext(full_audio_path)[0]
    print (full_audio_path)

    note_number = re.search(r"num=\s*([^\n\r]{2})", str(full_audio_path)).group(1)

    print ('note_num', note_number)

    csv_num = len(glob.glob(OUTPUT_DIR)) + 1
    print (csv_num)

    new_file_name = str(audio_file_name) + '__csv=' + str(csv_num) + '.csv'

    new_file = open(new_file_name, 'w')

    window = np.zeros(num_chunks)

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

    win_s = CHUNK  # fft size
    hop_s = CHUNK  # hop size

    s = aubio.source(filename, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.4

    pitch_o = aubio.pitch("yinfft", win_s, hop_s, samplerate)
    pitch_o.set_unit("Hz")
    pitch_o.set_tolerance(tolerance)

    # total number of frames read
    total_frames = 0
    prev_pred = 0
    data = wf.readframes(CHUNK)

    prev_lines = deque(maxlen=NUM_PAST_FREQS)
    for i in range(NUM_PAST_FREQS):
        prev_lines.append(0)
    empty_Deque = list(prev_lines)

    while True:
        samples, read = s()
        pred = pitch_o(samples)[0]
        pitch = int(round(pred))
        confidence = pitch_o.get_confidence()

        if confidence < 0.5:
            pitch = 0
        if abs(pitch - prev_pred) > 100:
            pitch = 0
        # print("%f %f %f" % (total_frames / float(win_s), pitch, confidence))
        prev_lines.append(pitch)
        counter = sum(1 if a == q else 0 for (a, q) in zip(prev_lines, empty_Deque))
        # if list(prev_lines) != list(empty_Deque):
        if list(prev_lines) != empty_Deque:
            print (prev_lines)

        stream.write(data)
        data = wf.readframes(CHUNK)

        prev_pred = pred
        total_frames += read

        if read < hop_s:
            break


if __name__ == '__main__':
    predict_freq_from_wav(current_path + '/Training/training_data/A3/name=A3__num=12__batch=y2017m05d27H21M46S45__2.wav', 4096, 3)
