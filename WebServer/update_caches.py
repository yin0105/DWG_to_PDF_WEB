# Update caches

import subprocess
import logging
from time import sleep

SCAN_INTERVAL = 60    # seconds
CMD_UPDATE_FILES = 'python fetch_drawings.py'
CMD_UPDATE_MB_NOTES = 'python scanned_masterbills.py'
CMD_UPDATE_MB_DRAWINGS = 'python parse_mbm.py'
CMD_FIND_MISPLACED_FILES = 'python find_misplaced_files.py'
CMD_FIND_OLD_VERSIONS = 'python find_versions.py'


class Logger(logging.Logger):

    def __init__(self):
        logging.Logger.__init__(self, 'sendplot_web_cache')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        #     Set level for the events to be logged
        self.root.setLevel(logging.NOTSET)
        #     Create handler for logging to console
        console = logging.StreamHandler()
        console.setLevel(0)
        console.setFormatter(formatter)
        self.addHandler(console)
        #     Create handler for logging to log file
        sLogFile = './log/sendplot_web_cache.log'
        fileHandler = logging.FileHandler(sLogFile)
        fileHandler.setFormatter(formatter)
        self.addHandler(fileHandler)


logger = Logger()

logger.info('sendplot_web_cache processor ||||||||||||||||||||||||||||||||||')
logger.info('Initializing...')
logger.info('starting...')


while 1:
    logger.info('start updating file cache...')
    subprocess.call(CMD_UPDATE_FILES)
    logger.info('finished updating file cache...')

    sleep(3)

    logger.info('start updating mb notes cache...')
    subprocess.call(CMD_UPDATE_MB_NOTES)
    logger.info('finished updating mb notes cache...')

    sleep(3)

    logger.info('start updating mb drawings cache...')
    subprocess.call(CMD_UPDATE_MB_DRAWINGS)
    logger.info('finished updating mb drawings cache...')

    logger.info('start check for misplaced files...')
    subprocess.call(CMD_FIND_MISPLACED_FILES)
    logger.info('finished check for misplaced files...')
    # print '\n\t waiting for ' + str(SCAN_INTERVAL) + ' seconds...\n'

    logger.info('start check for old versions...')
    subprocess.call(CMD_FIND_OLD_VERSIONS)
    logger.info('finished check for old versions...')

    sleep(SCAN_INTERVAL)
