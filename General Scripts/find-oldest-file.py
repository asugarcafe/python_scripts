# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:54:56 2020

@author: sucre
"""

import os, glob, time, operator, os.path, re

def get_oldest_files(files, _invert=False):
    """ Find and return the oldest file of input file names.
    Only one wins tie. Values based on time distance from present.
    Use of `_invert` inverts logic to make this a youngest routine,
    to be used more clearly via `get_youngest_file`.
    """
    gt = operator.lt if _invert else operator.gt
    # Check for empty list.
    if not files:
        return None
    # Raw epoch distance.
    now = time.time()
    # Select first as arbitrary sentinel file, storing name and age.
    oldest = files[0], now - os.path.getctime(files[0])
    # Iterate over all remaining files.
    for f in files[1:]:
        age = now - os.path.getctime(f)
        if gt(age, oldest[1]):
            # Set new oldest.
            oldest = f, age
    # Return just the name of oldest file.
    return oldest[0]

def get_youngest_file(files):
    return get_oldest_files(files, _invert=True)

# Example.
allfiles = []
exclude = ['.dropbox.cache']
pattern = ".*"
mypath = "e:\\dropbox\\"
for root, dirs, files in os.walk(mypath):
    for file in filter(lambda x: re.match(pattern, x), files):
        if exclude[0] not in root:
            allfiles.append(root + file)
print ('oldest:', get_oldest_files(allfiles))
#print ('youngest:', get_youngest_file(files))