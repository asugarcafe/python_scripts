# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 16:05:38 2025

@author: BeRoberts
"""

def bin_to_dec(binary_string):
    result = 0
    count = len(binary_string)
    for ch in binary_string:
        count = count-1
        result = result + (int(ch) * (2**count))        
    return result
