# stream that's coming in at 44,100 sps
# which is turned into 1024 sample chunks.
#
# OUTPUT_DIRECTORY
#
# def WriteFileName():
#     What note is this?
#     Ab
# noteName = 'Ab'
# noteNumber = String(note_to_number[noteName])
# date = 04_04_17
# output_filename = noteName + '_' + date + '_' + noteNumber

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
