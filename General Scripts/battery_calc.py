# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:57:38 2023

@author: sucre
"""
import math

def GetVolume(radius, height):
    return (math.pi * radius) * height

height = 19.5
diam = 10.5
r = diam/2

volume = GetVolume(r, height)

print(volume)