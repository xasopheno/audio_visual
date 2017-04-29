import numpy as np
import glob
from Conversion.wav_to_np import wav_to_np
from Detection.Detector import Detector

detector = Detector()

OUTPUT_DIR = './training_data/_training_input'
THRESHOLD = 1000


def predict_freq_from_wav(full_audio, chunk_size, num_chunks, audio_file_name):
    audio_as_array = wav_to_np(full_audio)
    audio_length = len(audio_as_array)
    index = 0

    new_file_name =

    batch_num = len(glob.glob(OUTPUT_DIR)) + 1

    file_name = str(new_file_name + batch_num)
    new_file = open(file_name, 'w')

    min_testable_chunks = chunk_size * num_chunks
    max_testable_chunks = audio_length - index

    window = np.zeros(num_chunks)

    while index < max_testable_chunks:
        chunk = audio_as_array[index:index + chunk_size]

        # Todo: minimum volume
        freq_prediction, volume = Detector.aubio_detector(chunk)

        if volume > THRESHOLD:
            np.roll(window, 1)
            window[1] = freq_prediction

            if index > min_testable_chunks:
                avg_pred = str(np.average(window))
                new_file.write(avg_pred + '=', note_name)
