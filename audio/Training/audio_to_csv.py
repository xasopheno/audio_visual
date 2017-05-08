import os.path
import sys
import numpy as np
import glob
import re
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from Conversion.wav_to_np import wav_to_np
from Detection.Detector import Detector

detector = Detector()

OUTPUT_DIR = './training_data/_training_input'
THRESHOLD = 1000
current_path = os.getcwd()

detector = Detector()

def predict_freq_from_wav(full_audio_path, chunk_size, num_chunks):
    audio_as_array = wav_to_np(full_audio_path)[1]

    print (type(audio_as_array))
    print audio_as_array.shape
    print
    audio_length = audio_as_array.astype(float).shape[0]
    print type(audio_length)
    print 'audio_length', audio_length
    index = 0

    audio_file_name = os.path.splitext(full_audio_path)[0]
    print full_audio_path

    note_number = re.search(r"num=\s*([^\n\r]{2})", str(full_audio_path)).group(1)

    print ('note_num', note_number)

    csv_num = len(glob.glob(OUTPUT_DIR)) + 1
    print csv_num

    new_file_name = str(audio_file_name) + '__csv=' + str(csv_num) + '.csv'

    new_file = open(new_file_name, 'w')

    min_testable_chunks = chunk_size * num_chunks
    max_testable_chunks = audio_length - index * chunk_size
    print (min_testable_chunks, max_testable_chunks)

    window = np.zeros(num_chunks)

    while index < max_testable_chunks:
        chunk = audio_as_array[index:index + chunk_size]
        # print chunk.shape
        # print type(chunk)
        # Todo: minimum volume - use detect_freqs

        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)


        freq_prediction, volume = detector.aubio_detector(chunk)
        print (freq_prediction)

        if volume > 0:
            np.roll(window, 1)
            # window[1] = freq_prediction

            if index > min_testable_chunks:
                avg_pred = np.average(window)
                new_file.write(int(avg_pred) + ',' + int(note_number.strip('0')) + '/n')

if __name__ == '__main__':
    predict_freq_from_wav(current_path + '/training_data/A3/name=A3__num=12__batch=y2017m05d07H21M30S31__1.wav', 4096, 3)
