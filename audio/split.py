from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio(file):
  sound = AudioSegment.from_mp3(file)
  chunks = split_on_silence(sound, 
      # must be silent for at least half a second
      min_silence_len=1000,

      # consider it silent if quieter than -16 dBFS
      silence_thresh=-25,

      # keep 200 ms of leading/trailing silence
      keep_silence=1000
  )

  for i, chunk in enumerate(chunks):
      chunk.export("./chunk{0}.mp3".format(i), format="mp3")
      print i

split_audio('file.wav')
