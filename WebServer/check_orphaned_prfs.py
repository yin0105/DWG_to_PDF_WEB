import os
import json
import logging
import shutil

prf_archive = 'H:\\PLOT\\PRF-Archive\\'


class Logger(logging.Logger):

    def __init__(self):
        logging.Logger.__init__(self, 'find_orphan_prfs')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        #     Set level for the events to be logged
        self.root.setLevel(logging.NOTSET)
        #     Create handler for logging to console
        console = logging.StreamHandler()
        console.setLevel(0)
        console.setFormatter(formatter)
        self.addHandler(console)
        #     Create handler for logging to log file
        sLogFile = './log/find_orphan_prfs.log'
        fileHandler = logging.FileHandler(sLogFile)
        fileHandler.setFormatter(formatter)
        self.addHandler(fileHandler)

logger = Logger()

logger.info('==============[ find_orphan_prfs processor ]================')


def read_json():
    with open('combined_directories.json') as json_file:
        dCombined = json.load(json_file)

    return dCombined


def has_prf(drawings):
    for drawing in drawings:
        extension = drawing[drawing.rfind('.') + 1:].upper()
        # print '\t' + extension
        if extension == 'PRF':
            return True
    return False


def has_dwg(drawings):
    for drawing in drawings:
        extension = drawing[drawing.rfind('.') + 1:].upper()
        # print '\t' + extension
        if extension == 'DWG':
            return True
    return False


def get_prf(drawings):
    for drawing in drawings:
        extension = drawing[drawing.rfind('.') + 1:].upper()
        # print '\t' + extension
        if extension == 'PRF':
            return drawing

dCombined = read_json()
iCnt = 0
file_count = 0
matched = 0
unmatched = 0

for root in dCombined.items():
    # print root[0]
    if has_prf(root[1]) and has_dwg(root[1]):
        matched += 1
    elif has_prf(root[1]):
        shutil.copy(get_prf(root[1]), prf_archive)
        os.remove(get_prf(root[1]))
        logger.info(' ' + root[0].ljust(25) + 'unmatched\t' + get_prf(root[1]))
        unmatched += 1

    iCnt += 1
    file_count = file_count + len(root[1])
    # if iCnt > 500:

logger.info(' Total roots:    '.ljust(25) + str(iCnt))
logger.info(' Total files:    '.ljust(25) + str(file_count))
logger.info(' Matched prfs:   '.ljust(25) + str(matched))
logger.info(' Unmatched prfs: '.ljust(25) + str(unmatched))
