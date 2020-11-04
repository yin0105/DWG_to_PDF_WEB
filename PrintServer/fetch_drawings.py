import sys
import os
import glob
import json
import timeit

aDirs = [['h:\\plot\\scanned_tif', 'tif'], ['h:\\plot\\masterbills', 'tif'],
         ['h:\\plot\\apdf', 'pdf'], ['h:\\plot\\bpdf', 'pdf'], ['h:\\plot\\pdf', 'pdf'],
         ['h:\\plot\\cpdf', 'pdf'], ['h:\\plot\\dpdf', 'pdf'], ['h:\\plot\\dxf', 'dxf'],
         ['l:\\PDFDrawings', 'pdf'], ['l:\\Drawings', 'dwg'], ['l:\\SWDRAW~1', 'slddrw'],
         ['f:\\ISNETW~1\mrp\masterbill_archive', 'pdf']]

def get_dir_dict(fDir, fType):
  aDir = glob.glob(fDir + '/*.' + fType)
  tmp_dict = {}
  for item in aDir:
    basename = item[item.rfind('\\') + 1:item.rfind('.')]
    tmp_dict[basename] = item
  return tmp_dict

def get_dir_combined(dDrawingList):
  for item in dDrawingList:
    if item in dCombined:
      dCombined[item.upper()].append(dDrawingList[item])
    else:
      dCombined[item.upper()] = [dDrawingList[item]]

def scan_all_directories():
  for drawing_directory in aDirs:
    dDirectory = get_dir_dict(drawing_directory[0], drawing_directory[1])
    get_dir_combined(dDirectory)
  fJSON = open('combined_directories.json', 'w')
  fJSON.write(json.dumps(dCombined))
  fJSON.close()

def read_json():
  global dCombined 
  with open('combined_directories.json') as json_file:
    dCombined = json.load(json_file)

def search_for_drawing():
  for key, value in dCombined.items():
    if sSearch == '*':
      dReturned[key] = value
    elif key.startswith(sSearch):
      dReturned[key] = value

#############################################################################

dCombined = {}
dReturned = {}

sScanned  = 0

if len(sys.argv) >= 2:
  sSearch = sys.argv[1].upper()
else:
  sSearch = '*'

# sScanned           = str(timeit.timeit(stmt=scan_all_directories, number=1))
sScanned           = str(timeit.timeit(stmt=read_json, number=1))
sSearched          = str(timeit.timeit(stmt=search_for_drawing, number=1))

dReturned['stats'] = { 'search_string'  : sSearch + '...',
                       'total_searched' : str(len(dCombined)),
                       'scan_time'      : sScanned,
                       'drawings_found' : str(len(dReturned)),
                       'search_time'    : sSearched }

print(json.dumps(dReturned, sort_keys=True, indent=2, separators=(',', ': ')))

