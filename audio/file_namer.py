from datetime import datetime
# stream that's coming in at 44,100 sps
# which is turned into 1024 sample chunks.
#
# OUTPUT_DIRECTORY

note_to_number = {
    'F5': 32,
    'E5': 31,
    'Eb5': 30,
    'D5': 29,
    'Db5': 28,
    'C5': 27,

    'B4': 26,
    'Bb4': 25,
    'A4': 24,
    'Ab4': 23,
    'G4': 22,
    'Gb4': 21,
    'F4': 20,
    'E4': 19,
    'Eb4': 18,
    'D4': 17,
    'Db4': 16,
    'C4': 15,

    'B3': 14,
    'Bb3': 13,
    'A3': 12,
    'Ab3': 11,
    'G3': 10,
    'Gb3': 9,
    'F3': 8,
    'E3': 7,
    'Eb3': 6,
    'D3': 5,
    'Db3': 4,
    'C3': 3,

    'B2': 2,
    'Bb2': 1,
}

def file_namer():
    note_name = raw_input('Which note is this?: ')
    now = datetime.now()

    for key in note_to_number:
        if key == note_name:
            note_number = note_to_number[key]

    # G3__1__2017_04_12__08_58_18__10
    for i in range(20):
        file_name =  now.strftime(note_name + '__' + str(i) + '__%Y_%m_%d__%H_%M_%S__' + str(note_number))
        print file_name

file_namer()
