import os

current_path = os.getcwd()

outputFileName = current_path + '/Training/csv/output.csv'
output = open(outputFileName, 'a')

import glob

read_files = glob.glob(current_path + '/Training/csv/*.csv')

with open(outputFileName, "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

