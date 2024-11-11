# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:19:19 2024

@author: BeRoberts
"""

import os

#todo: grab all the SVG files in the folder and create a list
directory = 'C:/temp/data/svg/'
wanted_ext = ['.svg']

count = 0
folder = os.listdir(directory)
files = []
with open(directory + "files.txt", "w") as f:

    for fname in folder:
            
        if os.path.isfile(directory + "/" + fname) and fname.endswith(wanted_ext[0]):
            # Full path
            val = '"' + directory + "/" + fname + '"'
            files.append(val)

            f.write(val + '\r')
    f.close()