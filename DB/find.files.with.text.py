# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:11:31 2024

@author: BeRoberts
"""

import os

skip_folders = ['/','.vs','bin','obj']
wanted_ext = ['.dtsx']

count = 0

def recurse_directory(directory, searchstring):
    folder = os.listdir(directory)
    for fname in folder:
        if os.path.isdir(directory + "/" + fname) and fname not in skip_folders:
            recurse_directory(directory + "/" + fname, searchstring)
            
        if os.path.isfile(directory + "/" + fname) and fname.endswith(wanted_ext[0]):
            # Full path
            f = open(directory + "/" + fname, 'r')
            #print(f)
    
            if searchstring in f.read():
                print('found string in file %s' % (directory + "/" + fname))
            # else:
            #     print('string not found')
            f.close()
            
            
user_input = 'C:/temp/dev/dev'

searchstring = 'Sql'


recurse_directory(user_input, searchstring)