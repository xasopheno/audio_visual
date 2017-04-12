from datetime import datetime
from note_to_number import note_to_number


def file_name_generator(file_number):
    """
    generates a filename in this format
    # name=B3__i=0__batch=y2017m04d12H15M10S11__num=14
    """

    note_name = raw_input('Which note is this?: ')
    now = datetime.now()

    note_number = -1

    for key in note_to_number:
        if key == note_name:
            note_number = note_to_number[key]

    if note_number >= 0:
        file_name = 'name=' + note_name + '__' + "i=" + str(file_number) + "__batch=" + now.strftime('y%Ym%md%dH%HM%MS%S') + '__num=' + str(note_number)
    else:
        print 'Please enter a real note name.'
        file_name_generator(file_number)

    return file_name

if __name__ == '__main__':
    name = file_name_generator(108)
    print name
