from __future__ import division

import os.path
import sys
import time
from collections import deque

import aubio
import numpy as np
import pyaudio
import tensorflow as tf
tf.reset_default_graph()

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
current_path = os.getcwd()
from Midi.NoteToMidi import sendMidi
from NeuralNetwork import Network
import math
import rtmidi
import ast
midiout = rtmidi.MidiOut()
midiout.open_port(0)

class StreamToFrequency:
    def __init__(self):
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("midi")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.99)

        self.output_file = open('output.txt', 'w')

        self.volume_threshold = 400
        self.acceptable_confidence = 0.61

        self.past_freq = 0
        self.predicted_frequency = 0

    def callback(self, in_data, frame_count, time_info, status):
        samples = np.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = self.pDetection(samples)[0]

        volume = np.sum(samples ** 2) / len(samples)
        volume = round(volume, 6) * 10 ** 5

        confidence = self.pDetection.get_confidence()

        if confidence < self.acceptable_confidence or volume < self.volume_threshold:
            self.predicted_frequency = 0
        else:
            self.predicted_frequency = prediction

        prediction = round(self.predicted_frequency)
        # print(prediction)
        self.past_freq = prediction

        # self.output_file.write(str(self.predicted_frequency) + '\n')
        # self.output_file.flush()
        # os.fsync(self.output_file.fileno())

        return in_data, pyaudio.paContinue


class Generator:
    def __init__(self):
        self.subdivision = 100/44100
        self.isZero = True
        self.sample_counter = 0
        self.note_counter = 1
        self.last_value = 0
        self.detector = StreamToFrequency()
        self.pred_set = deque(maxlen=9)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=44100,
                                  frames_per_buffer=2048,
                                  input=True,
                                  output=False,
                                  stream_callback=self.detector.callback)

        self.pred_deque = deque(maxlen=30)
        self.vocab = self.make_vocab()
        self.initialize_network()


    def initialize_network(self):
        print('init net')
        config = tf.ConfigProto()
        config.gpu_options.allow_growth=True
        self.sess = tf.InteractiveSession(config=config)
        self.sess.run(tf.global_variables_initializer())

        self.lstm_size = 128 #128s
        self.num_layers = 2
        self.net = Network(in_size = self.in_size,
                      lstm_size = self.lstm_size,
                      num_layers = self.num_layers,
                      out_size = self.out_size,
                      session = self.sess,
                      learning_rate = 0.003,
                      name = "char_rnn_network",
                        )
        self.saver = tf.train.Saver(tf.global_variables())
        self.saver.restore(self.sess, 'saved/model.ckpt')

    def make_vocab(self):
        data_ = ""
        with open('datasets/compressed/second_rounded.txt', 'r') as f:
            data_ += f.read()
        data_ = data_.split(' ')
        vocab = sorted(list(set(data_)))
        print(vocab)

        self.in_size = self.out_size = len(vocab)
        return vocab

    def embed_to_vocab(self, data_, vocab):
        data_ = data_.replace("'", "")
        data_ = data_.replace("', '", " ")
        data_ = data_.replace("[,", "")
        data_ = data_.replace("['", "")
        data_ = data_.replace(",]", "")
        data_ = data_.replace("',", "")
        data_ = data_.replace("'", "")
        data_ = data_.replace("]]", "]")
        data_ = str(data_)

        data = np.zeros((len(data_), len(vocab)))
        count=0

        s = data_
        v = [0.0]*len(vocab)
        v[vocab.index(s)] = 1.0
        data[count, :] = v
        count += 1

        return data

    def generate_set(self):
        while True:
            pred = self.detector.predicted_frequency
            value = int(round(pred))
            # self.pred_set.append(value)
            self.play_value(value)

    def play_midi(self, value):
        if value == 0:
            time.sleep(.00001)
        else:
            sendMidi(value, .00001)
            # sendMidi(value - 7, .01)
            # sendMidi(value * 1.5, .001)

    def play_midi(self, value, length):
        print ('play_midi', value, length)
        if value == 0:
            time.sleep(length * .01)
        else:
            note_on = [0x90, value, 120] # channel 1, middle C, velocity 112
            midiout.send_message(note_on)
            time.sleep(length * .001)
            note_off = [0x80, value, 120]
            midiout.send_message(note_off)

    def play_silence(self):
        print(0)
        # time.sleep(self.subdivision * 1.0)

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

    def round_down(self, x):
        return int(math.floor(x / 1000.0)) * 1000

    def play_value(self, value):
        # self.sample_counter += 1
        # print(value)
        # time.sleep(.005)

        # sys.stdout.write(str(self.note_counter))
        # sys.stdout.flush()
        # self.restart_line()


        with open("midiOutput.txt", 'a') as myfile:
            # value = max(set(self.pred_set), key=self.pred_set.count)
            # print(self.pred_set)
            # print(value)
            # arg_max = Counter(self.pred_set[0])
            # print(arg_max)
            if value == self.last_value:
                self.note_counter += 1
            else:
                stored_value = str(self.last_value)
                if self.note_counter < 3000 or self.last_value > 100:
                    stored_value = str(0)
                # print(self.last_value, self.note_counter)
                # self.play_midi(self.last_value)
                try:
                    out = self.net.run_step(self.embed_to_vocab('[' + stored_value + ',' + str(self.round_down(self.note_counter)) + ']', self.vocab))
                    element = np.random.choice(range(len(self.vocab)), p=out)
                    prediction = self.vocab[element]
                    prediction_eval = ast.literal_eval(prediction)
                    note = prediction_eval[0]
                    length = prediction_eval[1] / 350
                    self.play_midi(note, length)
                except Exception as e:
                    print (e)
                self.note_counter = 1

                # print(value == self.last_value)

            self.last_value = value

if __name__ == '__main__':
    generator = Generator()
    generator.generate_set()
