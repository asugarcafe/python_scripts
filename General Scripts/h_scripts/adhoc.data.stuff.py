# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 10:21:26 2025

@author: BeRoberts
"""
import pandas as pd

def nth(val):
    th = [4,5,6,7,8,9,10,11,12]
    if val == 1:
        return "st"
    elif val == 2:
        return "nd"
    elif val == 3:
        return "rd"
    elif val in th:
        return "th"
    

full_path = "C:/temp/import.xlsx"

df = pd.read_excel(full_path, engine='openpyxl', sheet_name='Sheet1')
df = df.drop(index=0)
cols = ['Latin Name', 'Gloss', 'Symbol', 'Approximate Sun Sign Dates',
       'Ecliptic Longitude', 'House', 'Polarity', 'Modality', 'Triplicity',
       'Modern Ruler']

for i, row in df.iterrows():
    name = row['Latin Name']
    label = row['Gloss']
    date_range = row['Approximate Sun Sign Dates']
    degrees = row['Ecliptic Longitude']
    house = str(row['House']) + nth(row['House'])
    pole = row['Polarity']
    mode = row['Modality']
    element = row['Triplicity']
    planet = row['Modern Ruler']
    print("")    
