#
# SendPlot Server
#

import os
import subprocess
import signal
import sys
import configparser
import logging
from os import listdir, remove
from time import sleep, localtime, strftime

def initialize():
  # Read configuration file
  config                           = configparser.RawConfigParser()
  config.read('server_config.ini')

  server_config                    = config._sections['Server']
  QUEUES                           = server_config['queue_root']
  FILES                            = server_config['files_root']
  LOG_FILE                         = server_config['log_file']
  IVIEW                            = server_config['i_view32'] 
  SCAN_INTERVAL                    = float(server_config['scan_interval'])

  # Initialize logging
  logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s %(message)s')

  logging.info('========================= SendPlot Server startup =========================')
  logging.info('>>>>> Begin Initializing <<<<<')

  def signal_handler(signal, frame):
      print ('Shutting down SendPlot Server!')
      logging.info('\tshutting down...')
      logging.info('========================= SendPlot Server shutdown ========================')
      sys.exit(0)
  signal.signal(signal.SIGINT, signal_handler)
  logging.info('\t\t\t ===[ Press Ctrl+C to shutdown SendPlot Server ]===')

  # Display console startup message
  print ('========================= SendPlot Server startup =========================')
  print ('\t\t\t ===[ Press Ctrl+C to shutdown SendPlot Server ]===')
  print ('Monitoring...')

  # Scan for queues
  queue_count = 0
  plot_queues = {}
  logging.info('\tqueues\t' + QUEUES)
  while 1:
    if os.path.exists(QUEUES):
      for queue in listdir(QUEUES):
        if not queue.endswith('md'):
          queue_count += 1
          q_config                              = configparser.RawConfigParser()
          q_config.read(QUEUES + '\\' + queue + '\\i_view32.ini')
          print_config                          = q_config._sections['Print']
          q_struc                               = {'printer': print_config['printer'], 'path': QUEUES + '\\' + queue}
          plot_queues[queue]                    = q_struc

          logging.info('\t\t' + queue)
      break
    else:
      logging.warning('Cannot access queues:\t' + QUEUES)
      logging.warning('Waiting 60 seconds')
      sleep(60)

  logging.info('\t\t[' + str(queue_count) + '] queues scanned')

  # Scan for filesF:\Operations\masterbills\MBPlot
  file_count = 0 
  logging.info('\tfiles\t' + FILES)
  for file in listdir(FILES):
    if not file.endswith('md'):
      file_count += 1
  logging.info('\t\t[' + str(file_count) + '] files scanned')
  logging.info('\tScan interval: ' + str(SCAN_INTERVAL) + ' seconds')
  logging.info('>>>>> Finished Initializing <<<<<')

  # Return initialized values
  return QUEUES, FILES, LOG_FILE, SCAN_INTERVAL, plot_queues, IVIEW

###############################################################################
if __name__ == "__main__":
  # Execute
  QUEUES, FILES, LOG_FILE, SCAN_INTERVAL, plot_queues, IVIEW = initialize()

  logging.info('Start monitoring queues...') 
  while 1: 
    # logging.info('\t' + 'monitoring...') 

    for queue in plot_queues:
      if os.path.exists(QUEUES + '\\' + queue):
        for file in listdir(QUEUES + '\\' + queue):
          if file.endswith('pdf') or file.endswith('PDF'):
            logging.info('\tprocessing\t' + queue.ljust(25) + '\t' + file)
            # logging.info(plot_queues[queue]['path'])
            queue_path = QUEUES + '\\' + queue
            cmd = IVIEW + ' ' + queue_path + '\\' + \
                  file + ' /ini="' + queue_path + \
                  '\\" /print="' + plot_queues[queue]['printer'] + '"'
            subprocess.call(cmd)
            # logging.info(cmd)
            # sleep(1)
            remove(QUEUES + '\\' + queue + '\\' + file)
      else:
        logging.warning('Cannot access queue:\t ' + QUEUES + '\\' + queue)
        logging.warning('Refreshing configuration in 60 seconds')
        sleep(60)
        QUEUES, FILES, LOG_FILE, SCAN_INTERVAL, plot_queues, IVIEW = initialize()       

    sleep(SCAN_INTERVAL)

