import json
# import os


def read_json():
    dCombined = {}
    with open('combined_directories.json') as json_file:
        dCombined = json.load(json_file)
    return dCombined


def get_folders():
    for key in dCombined.keys():
        item = dCombined[key]
        for folder in item:
            folders[folder[:folder.rfind('\\')]] = ''

# def create_files():
#   iCnt = 0
#   for key in dCombined.keys():
#     item = dCombined[key]
#     for folder in item:
#       if os.path.isfile(folder):
#         pass
#       else:
#         f = open(folder, 'w+')
#         f.write(folder)
#         f.close()
#         iCnt += 1
#   print '\t files created: ' + str(iCnt)

dCombined = read_json()
folders = {}
get_folders()
iCnt = 0

# create_files()

for folder in folders:
    print(folder)
