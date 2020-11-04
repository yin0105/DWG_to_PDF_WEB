import os
import time

out_queue  = '\\\\omegafs01\\data\\Operations\\masterbills\\'

def check_older_out_queue():
  #       check masterbill out queue for and delete older files
  now = time.time()
  print(now)
  if not os.path.exists(out_queue):
    print('cannot access ' + out_queue)
  else:
    for file in os.listdir(out_queue):
      print(file, os.stat(out_queue + file).st_mtime, (os.stat(out_queue + file).st_mtime < now - 86400))
      print('\t\t ' + str(os.path.isfile(os.path.join(out_queue, file))))
      if os.path.isfile(os.path.join(out_queue, file)):
        try:
          if os.stat(out_queue + file).st_mtime < now - 86400:
            print('deleting older file: ' + file)
            # os.remove(out_queue + file)
          else:
            print('\t\t not: ' + file)
        except Exception as e:
          print('failed to delete older pdf file')
          print(e)

    for file in os.listdir(out_queue + '\\text'):
      if os.path.isfile(file):
        try:
          if os.stat(out_queue + 'text/' + file).st_mtime < now - 86400:
            print('deleting older text file: ' + file)
            # os.remove(out_queue + 'text/' + file)
        except Exception as e:
          print('failed to delete older file')
          print(e)


check_older_out_queue()
