import time
import datetime
import sys

def time_stamp(): 
  return datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%y %H:%M:%S')

iCount = 1
bUp = True
sProgress = '#'
while 1:
  time.sleep(1)
  i = time_stamp()
  sys.stdout.write("\r\t" + i + '\t scanning... ' + iCount * sProgress + ' ' )
  sys.stdout.flush()
  if bUp:
    iCount = iCount + 1
    if iCount > 10:
      bUp = False
  else:
    iCount = iCount - 1
    if iCount < 1:
      bUp = True

