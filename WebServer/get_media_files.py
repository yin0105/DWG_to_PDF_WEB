import os
import re
import json
# import fnmatch
import win32api
from os.path import join, dirname
from dotenv import load_dotenv

# iPictures = "I:\\Pictures\\Projects-J-P-X-Ws\\J50000 - J59999"
# iPictures = "I:\\Pictures\\PROJEC~1\\J50000~1"
# iPictures = "I:\\Pictures\\PROJEC~1\\"
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
iPictures = os.environ.get('IPICTURES')

rx = re.compile("\.(JPG|PNG|MOV|AVI|MPG)")
rxJ = re.compile("([J|P|R|S|W|X]{1}\d{5}|T{1}\d{4})")
rxM = re.compile("([1|2|3|4|5]{1}D\d*-[R|S]P[1|2|3|4]{1}-\d{1}|[S|D]L-\d{2})")

pic_folders = {}


def add_to_key(key, safe_folder, folder):
    if key in pic_folders:
        folder_list = pic_folders[key]
        folder_list.append(safe_folder + '\\' + folder)
        # TODO List item => struct
        #         - folder
        #         - safe_folder + '\\' + folder
        #         - number of pictures
        #         - number of videos
    else:
        pic_folders[key] = [safe_folder + '\\' + folder]
print(str(len(iPictures)))
for dx in os.listdir(iPictures):
    print(iPictures)
    safe_folder = win32api.GetShortPathName(iPictures + dx)
    print(safe_folder)
    for root, dirnames, filenames in os.walk(safe_folder):
        folder = root[len(safe_folder) + 1:]
        for key in rxJ.findall(folder.upper()):
            # , rxM.findall(folder.upper())
            print(rxJ.findall(folder.upper())[0] + '\t' + folder.ljust(90))
            add_to_key(key, safe_folder, folder)

fJSON = open('picture_directories.json', 'w')
fJSON.write(json.dumps(pic_folders, sort_keys=True,
                       indent=2, separators=(',', ': ')))
fJSON.close()
