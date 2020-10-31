# import sys
import os
import re
import json

MBM_FOLDER = 'f:\\Operations\\Masterbills\\text'

# rx_drawings    = re.compile("[A|B|C|D|J|P|R|W|X]{1}\d{5}")
rx_drawings = re.compile(("\s[A|B|C|D|J|P|R|W|X]{1}\d{5}\w{6}\s"))

rx_changeparts = re.compile("[1|2|3]X\d{4}[A-z]")

masterbills = {}

for fName in os.listdir(MBM_FOLDER):

    mbm_file = open(MBM_FOLDER + '\\' + fName, 'r')
    mbm_drawings = {}

    for line in mbm_file.readlines():
        # line = line[10:79]
        if len(rx_drawings.findall(line)) > 0:
            # check for match with mb file name
            key = rx_drawings.findall(line)[0]
            pos = line.find(key) + 1
            desc = line[pos:pos + 53]
            search_key = line[pos + 1:pos + 6]
            mbm_drawings[search_key] = desc

        if len(rx_changeparts.findall(line)) > 0:
            key = rx_changeparts.findall(line)[0]
            pos = line.find(key)
            desc = line[pos:pos + 53]
            search_key = line[pos:pos + 6]
            mbm_drawings[search_key] = desc

    masterbills[fName[:fName.rfind('.')]] = mbm_drawings

    mbm_file.close()

fJSON = open('mb_drawings.json', 'w')
fJSON.write(json.dumps(masterbills, sort_keys=True,
                       indent=4, separators=(',', ': ')))
fJSON.close()
