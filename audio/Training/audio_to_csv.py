from collections import deque
import aubio
import os.path
import pyaudio
import re
import sys
import wave

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

OUTPUT_DIR = '/Training/csv/'
THRESHOLD = 1000
current_path = os.getcwd()
NUM_PAST_FREQS = 5
SAMPLERATE = 44100
CHUNK = 2048
TOLERANCE = 0.4
CSV_NUM = 1
PLAY_AUDIO = False

def predict_freq_from_wav(full_audio_path):
    print (full_audio_path)

    # find note_number
    note_number = re.search(r"num=\s*([^\n\r]{2})", str(full_audio_path)).group(1)
    note_name = re.search(r"name=\s*([^\n\r].+?(?=_))", str(full_audio_path)).group(1)

    print ('note_num', note_number)
    print ('csv_num=', CSV_NUM)

    # generate file_name
    csv_file_name = \
        current_path \
        + OUTPUT_DIR \
        + 'note_name=' + str(note_name) \
        + '__note_num=' + str(note_number) \
        + '__csv=' + str(CSV_NUM) \
        + '.csv'

    print(csv_file_name)

    if not os.path.isfile(csv_file_name):
        csv_file = open(csv_file_name, 'a')
        for i in range(5):
            csv_file.write('freq_pred' + str(i) + ',')
        csv_file.write('note_number')
        csv_file.write(str('\n'))
    else:
        csv_file = open(csv_file_name, 'a')

    audio_filename = full_audio_path

    p = pyaudio.PyAudio()

    # prepare_aubio
    s = aubio.source(audio_filename, SAMPLERATE, CHUNK)

    pitch_o = aubio.pitch("yinfft", CHUNK, CHUNK, SAMPLERATE)
    pitch_o.set_unit("Hz")
    pitch_o.set_tolerance(TOLERANCE)

    prev_pred = 0

    # generate_deque
    prev_lines = deque(maxlen=NUM_PAST_FREQS)
    for i in range(NUM_PAST_FREQS):
        prev_lines.append(0)
    empty_deque = list(prev_lines)

    if PLAY_AUDIO:
        wf = wave.open(audio_filename)

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)

    while True:
        samples, read = s()
        pred = pitch_o(samples)[0]
        pitch = int(round(pred))
        confidence = pitch_o.get_confidence()

        if confidence < 0.5:
            pitch = 0
        if abs(pitch - prev_pred) > 100:
            pitch = 0
        prev_lines.append(pitch)
        list_prev_lines = list(prev_lines)
        if list_prev_lines != empty_deque:
            print (list_prev_lines)
            for value in list_prev_lines:
                csv_file.write(str(value))
                csv_file.write(str(','))
            csv_file.write(str(note_number))
            csv_file.write('\n')

        if PLAY_AUDIO:
            stream.write(data)
            data = wf.readframes(CHUNK)

        prev_pred = pred

        if read < CHUNK:
            break

if __name__ == '__main__':
    # for every .wav file in training_data
    for root, dirs, files in os.walk(current_path + '/Training/training_data'):
        for file in files:
            if file.endswith(".wav"):
                filename = os.path.join(root, file)
                predict_freq_from_wav(filename)
