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


def predict_freq_from_wav(full_audio_path, chunk_size, num_chunks):
    audio_file = open(full_audio_path, 'r')
    audio_as_array = wav_to_np(full_audio_path)
    print (type(audio_as_array))
    # dtype=np.int16
    audio_length = len(audio_as_array)
    index = 0

    audio_file_name = os.path.splitext("full_audio_path")[0]
    print full_audio_path

    note_number = re.search(r"num=\s*([^\n\r]{2})", str(full_audio_path)).group(1)
    # note_number = note_number.group(1)

    print note_number

    csv_num = len(glob.glob(OUTPUT_DIR)) + 1

    new_file_name = str(audio_file_name) + '__csv=' + str(csv_num)

    new_file = open(new_file_name, 'w')

    min_testable_chunks = chunk_size * num_chunks
    max_testable_chunks = audio_length - index

    window = np.zeros(num_chunks)

    while index < max_testable_chunks:
        chunk = audio_as_array[index:index + chunk_size]
        print ('chunk type', type(chunk))

        # Todo: minimum volume - use detect_freqs

        freq_prediction, volume = Detector.aubio_detector(chunk)
        print (freq_prediction)

        if volume > 0:
            np.roll(window, 1)
            window[1] = freq_prediction

            if index > min_testable_chunks:
                avg_pred = np.average(window)
                new_file.write(int(avg_pred) + ',' + int(note_number.strip('0')) + '/n')

if __name__ == '__main__':
    predict_freq_from_wav(current_path + '/training_data/A3/name=A3__num=12__batch=y2017m04d29H14M48S13__1.wav', 1024, 3)
