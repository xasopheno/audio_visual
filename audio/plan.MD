5/7/17
Got detection working
need to de-couple

data recorder and frequency detector need to work together
guarantee recording volume?


take the last three values that are not 0 and take an average.
last three averages.

    105, 102, 104, 1 prob: 100
    0, 107, 107, 1 prob: 90
    667, 657, 676, prob: 95
    800, 0, 450, 7: prob: 20
    0, 1014, 1000, 28 prob: 80

_________

4/28/17
3 seconds of audio at 44100
1024, 1024, 1024(start)

    def audio_to_csv(full_audio):
        audio_as_array = full_audio.to_np()
        audio_length = len(audio_as_array)
        index = 0
__________
4/14/17

stream that's coming in at 44,100 sps
which is turned into 1024 sample chunks.

OUTPUT_DIRECTORY

def WriteFileName():
    What note is this?
        Ab
    noteName = 'Ab'
    noteNumber = String(note_to_number[noteName])
    date = 04_04_17
    output_filename = noteName + '_' + date + '_' + noteNumber


    

note_to_number = [
    
    'F5' : 32
    'E5' : 31
    'Eb5' : 30
    'D5' : 29
    'Db5' : 28
    'C5' : 27

    'B4' : 26
    'Bb4' : 25
    'A4' : 24
    'Ab4' : 23
    'G4' : 22
    'Gb4' : 21
    'F4' : 20
    'E4' : 19
    'Eb4' : 18
    'D4' : 17
    'Db4' : 16
    'C4' : 15

    'B3' : 14
    'Bb3' : 13
    'A3' : 12
    'Ab3' : 11
    'G3' : 10
    'Gb3' : 9
    'F3' : 8
    'E3' : 7
    'Eb3' : 6
    'D3' : 5
    'Db3' : 4
    'C3' : 3

    'B2' : 2
    'Bb2' : 1
]
