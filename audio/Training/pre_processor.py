import os
from Conversion.wav_to_np import wav_to_np

current_path = os.getcwd()
TRAINING_DIR = '/training_data'

training_data_dir = current_path + TRAINING_DIR
prepared_data_dir = current_path + TRAINING_DIR + '/__pre_processed_data'

def pre_processor(audio_file):
    data = wav_to_np(audio_file)
    print len(data)

