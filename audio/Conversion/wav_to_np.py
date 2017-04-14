import scipy.io.wavfile as wav


def wav_to_np(file_name):
    data = wav.read(file_name)
    return data
