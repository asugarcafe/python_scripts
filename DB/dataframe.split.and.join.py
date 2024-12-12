# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:29:37 2024

@author: BeRoberts
"""
from os import listdir, path
from os.path import isfile, join
import pandas as pd


#TODO open all excel sheets in this folder:
mypath = 'I:/Rachel/REPORTS/Monthly Stats/2023/Circulation and Collection by Material Audience/Circulation by Age'    

#List files in folder
exclfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.startswith('2')]

#Put all copies in an array of dataframes
frames = []
adult_frames = []
child_frames = []
teen_frames = []
adult_sums = None
child_sums = None
teen_sums = None
idx = 0
for file in exclfiles: 
    f =  mypath + '/' + file
    excel = pd.read_excel(f,'Sheet1', header=None)
    frames.append(excel)
    fa = frames[0][[0,1]]
    fc = frames[0][[3,4]]    

    fc = fc[fc[4].isna()==False]
    #fc = fc.query('3 != 4')
    
    ft = frames[0][[6,7]]
    adult_frames.append(fa)
    child_frames.append(fc)    
    teen_frames.append(ft)    
    idx += 1
    if idx > 3:
        break

# datN = frames[0][[6,7]]
# print(datN)
