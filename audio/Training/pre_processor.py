from Conversion.wav_to_np import wav_to_np


def pre_processor(audio_file):
    data = wav_to_np(audio_file)
    print len(data)
