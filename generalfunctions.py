# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 17:22:15 2025

@author: sucre
"""

def compound(principal, apr, years, intervals = 1):
    exp = intervals*years
    drate = apr/intervals
    p = principal * (1 + drate)**exp
    return p


print(compound(6.0, .1, 10))
print(compound(100.0, -.01, 100))
print(compound(100.0, -.005, 100))