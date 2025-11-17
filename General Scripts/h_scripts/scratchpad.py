# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:07:23 2025

@author: sucre
"""

from os import listdir
from os.path import isfile, join

font_dir = 'C:/Users/sucre/AppData/Local/Microsoft/Windows/Fonts'
onlyfiles = [f for f in listdir(font_dir) if isfile(join(font_dir, f))]


