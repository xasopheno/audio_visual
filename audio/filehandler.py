import os
import scipy.io.wavfile as wav
# install lame
# install bleeding edge scipy (needs new cython)

def mp3_to_np(file_name):
    fname = file_name
    temp = 'temp.wav'
    cmd = 'lame --decode {0} {1}'.format(fname,temp)
    os.system(cmd)
    data = wav.read(temp)
    # your code goes here
    return data

    clean_cmd = 'rm -rf temp.wav'
    os.system(clean_cmd)

# mp3_to_np('styx.mp3')
