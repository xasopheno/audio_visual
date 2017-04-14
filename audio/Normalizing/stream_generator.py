import pyaudio


class StreamGenerator:
    def __init__(self):
        self.sample_rate = 44100
        self.chunk_size = 1024
        self.channels = 1

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def set_chunk_size(self, chunk_size):
        self.chunk_size = chunk_size


    def play_stream_generator(self):
        p = pyaudio.PyAudio()

        return p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            output=2
    )


    def record_stream_generator(self):
        p = pyaudio.PyAudio()

        return p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate = self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
