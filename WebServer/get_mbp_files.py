import os
import re


DRAWING_CHARACTERS = "ABCDEX012345"
X_PART_CHARACTERS = "12345"
rx = re.compile('[a-zA-z]')

mbp_dir = 'F:\\Operations\\MBPlot\\'

mbp_files = os.listdir(mbp_dir)

for mbp_file in mbp_files:
    file = open(mbp_dir + mbp_file, 'r')
    print(mbp_file[:mbp_file.find('.')])
    for line in file.readlines():
        if len(line) > 2 and line[0] in DRAWING_CHARACTERS:
            if line[0] in X_PART_CHARACTERS:
                print(line[:-1], line[0:6])
            else:
                print(line[:-1], line[1:6])
        else:
            pass
            # print '\t' + line[:-1]
