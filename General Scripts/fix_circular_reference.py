# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:50:29 2021

@author: sucre
"""

class selection:
    lineNumber = -1
    text = ''
    
    def __init__(base, lineNumber, text):
        base.lineNumber = lineNumber
        base.text = text

class bottomLine:
    

    def maxLineNumber(base, arrSelections):
        nums = []
        for x in range(0,len(arrSelections)):
            nums.append(arrSelections[x].lineNumber)
            

newSelections = []  
newSelections.append(selection(1,"first"))
newSelections.append(selection(2,"second"))
newSelections.append(selection(3,"third"))