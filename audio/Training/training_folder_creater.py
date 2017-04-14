from note_to_number import note_to_number
import os

current_path = os.getcwd()
OUTPUT_DIR = '/training_data'

training_data_dir = current_path + OUTPUT_DIR
prepared_data_dir = current_path + OUTPUT_DIR + '/__pre_processed_data'

if not os.path.exists(training_data_dir):
    os.makedirs(training_data_dir)
    print 'created: ' + training_data_dir

if not os.path.exists(prepared_data_dir):
    os.makedirs(prepared_data_dir)
    print 'created: ' + prepared_data_dir

for key in note_to_number:
    key_path = '/' + key

    if not os.path.exists(training_data_dir + key_path):
        os.makedirs(training_data_dir + key_path)
    print 'created: ' + training_data_dir + key_path
