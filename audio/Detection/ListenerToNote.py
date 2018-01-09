# import time
# import os.path
# import sys
# from sklearn.externals import joblib
# import random
# import numpy
#
# from collections import deque
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
#
# from Oscillators.sine_osc import SineOsc
# from Normalizing.StreamGenerator import *
# # from Midi import NoteToMidi
#
# current_path = os.getcwd()
# pickle_path = current_path + '/Training/csv/knn_classifier.pickle'
# # pickle_data = pickle.dumps(pickle_path)
# classifier = joblib.load(pickle_path)
#
# NUM_PAST_FREQS = 10
# RATE = 44100
# CHUNKSIZE = 1100
#
# osc = SineOsc()
# sg = StreamGenerator()
# stream = sg.output_stream_generator()
#
# f = open('Detection/output.txt', 'r')
# f.seek(0, os.SEEK_END)
# commands = open('Detection/output.txt', 'w')
#
# past_freq = 0
# past_pred = [0]
#
# # generate_deque
# prev_lines = deque(maxlen=NUM_PAST_FREQS)
# for i in range(NUM_PAST_FREQS):
#     prev_lines.append(0)
# empty_deque = list(prev_lines)
#
# def follow():
#     while True:
#         newline = f.readline().strip('\n')
#         if not newline:
#             time.sleep(0.01)
#             continue
#         yield int(float(newline))
#
# for line in follow():
#     if abs(past_freq - line) < 20:
#         prev_lines.append(line)
#     else:
#         prev_lines.append(0)
#     past_freq = line
#     list_lines = list(prev_lines)
#     list_lines = numpy.array(list_lines).reshape(1, -1)
#     # print (list_lines)
#     prediction = classifier.predict(list_lines)
#     prediction_prob = numpy.max(classifier.predict_proba(list_lines))
#
#     # print prediction[0]
#     if prediction == [8]:
#         print (' ')
#     else:
#         if prediction_prob > .9:
#             if prediction != [past_pred]:
#                 print ' '
#                 print(prediction[0])
#                 # NoteToMidi.sendMidi(prediction[0] + 31, .2)
#                 # NoteToMidi.sendMidi(prediction[0] + 38, .2)
#                 # NoteToMidi.sendMidi(prediction[0] + 29, .2)
#                 # NoteToMidi.sendMidi(prediction[0] + 27, .1)
#                 # NoteToMidi.sendMidi(prediction[0] + 29, .1)
#                 # NoteToMidi.sendMidi(prediction[0] + 29, .1)
#                 # NoteToMidi.sendMidi(prediction[0] + 20, .2)
#                 # NoteToMidi.sendMidi(prediction[0] + 19, .2)
#
#
#         # past_pred = prediction
#     # commands.write(str(list(prev_lines)) + '\n')
#     # commands.flush()
#     # os.fsync(commands.fileno())
#     # time.sleep(.5)
#     # f.seek(0, os.SEEK_END)
#     # past_freq = line
#
