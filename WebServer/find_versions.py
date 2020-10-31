
# There are rules to the revision naming convention.
# SINGLE SHEET FILES:
# 12345-00
# 12345-A0
# 12345-B0
#           regex: '[0-9]{5}-[0|A-Z][0-9]{1}\.pdf'
#                 5 digits ( 0 through 9 )
#                 hypen ( - )
#                 0 or A through Z version
#                 1 digit ( 0 through 9 )
#
# MULTIPLE SHEET FILES
# 12345-001
# 12345-002
# 12345-A01
# 12345-A02
# 12345-B01
# 12345-B02
#           regex: '[0-9]{5}-[0|A-Z][0-9]{2}\.pdf'
#                 5 digits ( 0 through 9 )
#                 hypen ( - )
#                 0 or A through Z version
#                 2 digits ( 0 through 9 )
#

import os
import re
# import time
import logging
import shutil

pdf_folder = 'L:\\pdf_out'
# pdf_folder = 'C:\\var\\work\\pdf_filter\\pdf_out'
pdf_deleted = pdf_folder + '\\deleted'
# pdf_folder = 'C:\\var\\work\\Converter-Z\\SW_PDF_OUT'
pdf_files = os.listdir(pdf_folder)
pdf_files = [file.upper() for file in pdf_files]


class Logger(logging.Logger):

    def __init__(self):
        logging.Logger.__init__(self, 'find_drawing_versions')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        #     Set level for the events to be logged
        self.root.setLevel(logging.NOTSET)
        #     Create handler for logging to console
        console = logging.StreamHandler()
        console.setLevel(0)
        console.setFormatter(formatter)
        self.addHandler(console)
        #     Create handler for logging to log file
        sLogFile = './log/find_drawing_versions.log'
        fileHandler = logging.FileHandler(sLogFile)
        fileHandler.setFormatter(formatter)
        self.addHandler(fileHandler)

logger = Logger()

logger.info(
    '==============[ find_drawing_versions processor ]================')
# logger.info('Initializing...')


def scan_pdfs(sType):
    versioned_drawings = []
    delete_count = 0

    if sType == 'Single':
        # re_single_sheet = re.compile('[0-9]{5}-[0|A-Z][0-9]{1}\.pdf')
        re_search = re.compile(
            '[0-9]{5}-[0|A-Za-z][0-9]{1}\.pdf', re.IGNORECASE)
    elif sType == 'Multi':
        re_search = re.compile(
            '[0-9]{5}-[0|A-Za-z][0-9]{2}\.pdf', re.IGNORECASE)
    else:
        re_search = re.compile(
            '(?!([0-9]{5}-[0|A-Za-z][0-9]{1}\.pdf|[0-9]{5}-[0|A-Za-z][0-9]{2}\.pdf))', re.IGNORECASE)

    for pdf_file in pdf_files:
        if re_search.match(pdf_file):
            versioned_drawings.append(pdf_file)
    # logger.info(' ---------------------------------------------------------')
    # logger.info(' PDF Drawings checked: ' + str(len(pdf_files)))
    # logger.info(' PDF Drawings - matching ' + sType + ' pattern: \t\t\t[ ' + str(len(versioned_drawings)) + ' ]')

    drawing_groups = {}
    drawing_versions = {}
    for drawing in versioned_drawings:
        drawing_groups[drawing[0:5]] = []
        drawing_versions[drawing[0:5]] = {}

    for drawing in versioned_drawings:
        drawing_groups[drawing[0:5]].append(drawing)
        drawing_versions[drawing[0:5]][drawing[6:7]] = '-'

    for key in drawing_groups:
        versions = drawing_versions[key].keys()
        versions.sort()
        number_of_versions = len(versions)
        latest_version = versions[-1]
        # print '\n drawing: \t' + key
        if sType != 'Other':
            pass
            # print ' versions: \t(' + str(number_of_versions) + ') ',
            # print versions
            # print ' latest: \t[ ' + latest_version + ' ]'
        for drawing in drawing_groups[key]:
            # print '\t' + drawing,
            if number_of_versions > 1:
                if drawing[6:7] != latest_version and sType != 'Other':
                    logger.info('\tdelete ' + drawing)
                    shutil.copy(pdf_folder + '\\' + drawing,
                                pdf_deleted + '\\' + drawing)
                    os.remove(pdf_folder + '\\' + drawing)
                    delete_count += 1
                else:
                    pass
                    # print
            else:
                pass
                #  print
    sMsg = ' PDF Drawings - ' + sType + \
           ' pattern (matched / deleted): \t[ ' + \
        str(len(versioned_drawings)) + ' / ' + str(delete_count) + ' ]'

    logger.info(sMsg)

    # logger.info(' ' + sType + ' Total deletions:\t' + str(delete_count))

logger.info(
    ' PDF Drawings - checked: \t\t\t\t\t[ ' + str(len(pdf_files)) + ' ]')
scan_pdfs('Single')
scan_pdfs('Multi')
scan_pdfs('Other')
