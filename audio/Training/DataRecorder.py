import pyaudio
import wave
import audioop
from collections import deque
import os
import math
from file_namer import file_name_generator

class DataRecorder:
    def __init__(self):
        # Microphone stream config.
        self.CHUNK = 1024  # CHUNKS of bytes to read each time from mic
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.THRESHOLD = 1500  # The threshold intensity that defines silence
        # and noise signal (an int. lower than THRESHOLD is silence).

        self.SILENCE_LIMIT = 0.2  # Silence limit in seconds. The max amount of seconds where
        # only silence is recorded. When this time passes the
        # recording finishes and the file is delivered.

        self.PREV_AUDIO = 0.5  # Previous audio (in seconds) to prepend. When noise
        # is detected, how much of previously recorded audio is
        # prepended. This helps to prevent chopping the beginning
        # of the phrase.
        self.GENERATED_FILE_NAME, self.NOTE_NAME = file_name_generator()

        self.PATH = os.getcwd()

    def audio_int(self, num_samples=50):
        """ Gets average audio intensity of your mic sound. You can use it to get
            average intensities while you're talking and/or silent. The average
            is the avg of the 20% largest intensities recorded.
        """

        print "Getting intensity values from mic."
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        values = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 4)))
                  for x in range(num_samples)]
        values = sorted(values, reverse=True)
        r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
        print " Finished "
        print " Average audio intensity is ", r
        stream.close()
        p.terminate()
        return r

    def listen_and_record(self):
        file_number = 1
        num_phrases = -1

        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print "* Listening mic. "
        audio2send = []
        rel = self.RATE/self.CHUNK
        slid_win = deque(maxlen=self.SILENCE_LIMIT * rel)

        # Prepend audio from 0.5 seconds before noise was detected
        prev_audio = deque(maxlen=self.PREV_AUDIO * rel)
        started = False
        n = num_phrases

        while num_phrases == -1 or n > 0:
            cur_data = stream.read(self.CHUNK)
            slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
            # print slid_win[-1]
            if sum([x > self.THRESHOLD for x in slid_win]) > 0:
                if not started:
                    print "Starting record of phrase"
                    started = True
                audio2send.append(cur_data)
            elif started is True:
                print "Finished"
                # The limit was reached, finish capture and deliver.
                self.save_recording(list(prev_audio) + audio2send, file_number, p)
                file_number += 1

                # Reset all
                started = False
                slid_win = deque(maxlen=self.SILENCE_LIMIT * rel)
                prev_audio = deque(maxlen=0.5 * rel)
                audio2send = []
                n -= 1
                print "Listening ..."
            else:
                prev_audio.append(cur_data)

        print "* Done recording"
        stream.close()
        p.terminate()


    def save_recording(self, data, file_number, p):
        filename = self.PATH + '/training_data/' + self.NOTE_NAME + '/' + self.GENERATED_FILE_NAME + '__' + str(file_number)

        # writes data to WAV file
        data = ''.join(data)
        wf = wave.open(filename + '.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.RATE)
        wf.writeframes(data)
        wf.close()

        final_name = filename + '.wav'

        print final_name
        return final_name


if(__name__ == '__main__'):
    DataRecorder().listen_and_record()  # listen to mic.
    # audio_int()  # To measure your mic levels
