from collections import deque
import aubio
import os.path
import pyaudio
import re
import sys
import wave

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


class AudioToCSV:
    def __init__(self):
        self.play_audio = False

        self.current_path = os.getcwd()
        self.output_dir = '/Training/csv/'
        self.csv_num = 1
        self.csv_file = ''

        self.num_past_freqs = 10
        self.sample_rate = 44100
        self.chunk_size = 700
        self.tolerance = .9
        self.confidence_threshold = .9

        self.p = pyaudio.PyAudio()
        self.pitch_o = aubio.pitch("yinfft", self.chunk_size * 2, self.chunk_size, self.sample_rate)
        self.pitch_o.set_unit("midi")
        self.pitch_o.set_tolerance(self.tolerance)
        self.audio_file = None

        self.prev_lines, self.empty_deque = self.generate_deque()
        self.prev_pred = 0

    def generate_deque(self):
        prev_lines = deque(maxlen=self.num_past_freqs)

        for i in range(self.num_past_freqs):
            prev_lines.append(0)
        empty_deque = list(prev_lines)

        return prev_lines, empty_deque

    def name_generator(self, audio_filename):
        # print (audio_filename)

        note_number = re.search(r"num=\s*([^\n\r]{2})", str(audio_filename)).group(1)
        note_name = re.search(r"name=\s*([^\n\r].+?(?=_))", str(audio_filename)).group(1)

        # print ('note_num', note_number)
        # print ('csv_num=', self.csv_num)

        # generate file_name
        csv_file_name = \
            self.current_path \
            + self.output_dir \
            + 'note_name=' + str(note_name) \
            + '__note_num=' + str(note_number) \
            + '__csv=' + str(self.csv_num) \
            + '.csv'
        # print(csv_file_name)

        return note_number, note_name, csv_file_name

    def predict_freq_from_wav(self, audio_filename):
        note_number, note_name, csv_file_name = self.name_generator(audio_filename)
        self.csv_file = open(csv_file_name, 'a')
        file_in_aubio = aubio.source(audio_filename, self.sample_rate, self.chunk_size)

        if self.play_audio:
            self.audio_file = wave.open(audio_filename)

            stream = self.p.open(format=self.p.get_format_from_width(self.audio_file.getsampwidth()),
                                 channels=self.audio_file.getnchannels(),
                                 rate=self.audio_file.getframerate(),
                                 output=True)

            data = self.audio_file.readframes(self.chunk_size)

        while True:
            samples, chunks_read = file_in_aubio()
            pred = self.pitch_o(samples)[0]
            pitch = int(round(pred))
            confidence = self.pitch_o.get_confidence()

            # if confidence < self.confidence_threshold:
            #     pitch = 0
            if abs(pitch - self.prev_pred) > 1:
                pitch = 0

            self.prev_lines.append(pitch)

            list_prev_lines = list(self.prev_lines)
            if list_prev_lines != self.empty_deque:
                print (list_prev_lines)
                for value in list_prev_lines:
                    self.csv_file.write(str(value))
                    self.csv_file.write(str(','))
                self.csv_file.write(str(note_number))
                self.csv_file.write('\n')

            if self.play_audio:
                stream.write(data)
                data = self.audio_file.readframes(self.chunk_size)

            self.prev_pred = pred

            if chunks_read < self.chunk_size:
                break

        self.prev_lines, self.empty_deque = self.generate_deque()

if __name__ == '__main__':
    audio_to_csv = AudioToCSV()
    # for every .wav file in training_data
    for root, dirs, files in os.walk(audio_to_csv.current_path + '/Training/training_data'):
        for file in files:
            if file.endswith(".wav"):
                filename = os.path.join(root, file)
                print (file)
                audio_to_csv.predict_freq_from_wav(filename)
