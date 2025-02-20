# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:13:06 2023

@author: sucre
"""
import json
from collections import Counter
import turtle as trtl


def square(length=100):
    for x in range(0,4):
        trtl.forward(length)
        trtl.right(90)
        
def triangle(length=100):
    for x in range(0,2):
        trtl.forward(length)
        trtl.right(120)
        

for x in range(0,12):        
    trtl.right(30)
    square()
    #trtl.right(5)
    triangle()

trtl.done()