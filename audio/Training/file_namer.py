from datetime import datetime
from note_to_number import note_to_number


def file_name_generator():
    """
    generates a filename in this format
    name=Ab3__num=11__batch=y2017m04d12H19M05S01

    returns file_name, note_name
    """

    note_name = raw_input('Which note is this?: ')
    now = datetime.now()

    note_number = -1

    for key in note_to_number:
        if key == note_name:
            note_number = note_to_number[key]

    if note_number >= 0:
        file_name = 'name=' + note_name + '__num=' + str(note_number) + "__batch=" + now.strftime('y%Ym%md%dH%HM%MS%S')
        return file_name, note_name
    else:
        print 'Please enter a real note name.'
        file_name_generator()


if __name__ == '__main__':
    name, note = file_name_generator()
    print name
    print note
