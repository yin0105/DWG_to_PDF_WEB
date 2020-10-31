'''
Update db
'''

import json
import os

db = {}


def scan_all_directories():
    # get drawing roots and files
    # write scan results to json
    json.dumps('combined_directories.json')
    return dCombinedDirectories


def read_json():
    return json.load('combined_directories.json')

# load stored data from json at startup
dCombinedDirectoriesOld = read_json()

while True:
    dCombinedDirectories = scan_all_directories()

    if dCombinedDirectoriesOld.empty:
        # update entire DB
        pass
        for root in dCombinedDirectories.iterkeys():
            if dCombinedDirectories[root] != db[root]:
                # insert or update db
                pass

    else:
        if dCombinedDirectories == dCombinedDirectoriesOld:
            # no changes -- skip db update
            pass
        else:
            for root in dCombinedDirectories.iterkeys():
                if dCombinedDirectories[root] != dCombinedDirectoriesOld[root]:
                    # update or insert record
                    pass

            dCombinedDirectories = dCombinedDirectoriesOld

    # check for deleted files
    for root in dCombinedDirectories:
        for drawing in dCombinedDirectories[root]:
            if not os.path.isfile(drawing):
                # delete drawing from database
                pass
