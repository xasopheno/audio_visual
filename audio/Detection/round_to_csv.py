import math
import ast


def round_down(x):
    return int(math.floor(x / 1000.0)) * 1000 / 100

with open('datasets/compressed/second.txt', 'r') as f:
    counter = 0
    with open("rounded.csv", 'a') as rounded_csv:
        values = f.read().split(' ')
        for value in values:
            value = value.replace("', '", " ")
            value = value.replace("[,", "")
            value = value.replace("['", "")
            value = value.replace(",]", "")
            value = value.replace("',", "")
            value = value.replace("'", "")
            value = value.replace("]]", "]")
            value = ast.literal_eval(value)
            # print(value)
            midi_num = int(value[0])
            length = int(value[1])
            # length = round_down(length)
            token = ''
            # if midi_num == 0 and length > 3000:
            # token = '|'

            rounded_csv.write(
                str(counter) + ',' +
                str(midi_num) + ',' +
                str(length / 1000.) + '\n')
            counter += 1
