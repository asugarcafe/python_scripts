# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 17:22:15 2025

@author: sucre
"""
from asteval import Interpreter
import math

def compound(principal, apr, years, intervals = 1):
    exp = intervals*years
    drate = apr/intervals
    p = principal * (1 + drate)**exp
    return p

def bin_to_dec(binary_string):
    binary_string = binary_string[::-1]
    bit_length = len(binary_string)
    result = 0
    for x in range(0, bit_length):
        if binary_string[x] == '1':
            result += 1*(2**x)
    return result    

def diam_from_circum(circumference):
    return circumference/math.pi

cir = 130
diam = diam_from_circum(cir)
hei = 153.0
vol = math.pi*((diam/2)**2)*hei

b_diam = 70

# print(f"diam: {diam:.2f} {compound(diam, .04, 10):.2f}")#vol
# print(f"cir: {cir:.2f} {compound(cir, .04, 10):.2f}")#vol
# print(f"hei: {hei:.2f} {compound(hei, .04, 10):.2f}")#vol
# print(f"vol: {vol:.2f} {compound(vol, .04, 10):.2f}")#vol
# print('--')
# print(compound(100.0, .01, 100))
# print(compound(100.0, -.01, 100))
# print(compound(100.0, -.005, 100))
print(bin_to_dec('11111'))
print(bin_to_dec('1'))
print(len("abcdefghijklmnopqrstuvwxyz_"))
print(len("0123456789."))
print(len("()^*/+-=_"))

# aeval = Interpreter()
# result = aeval('2**(4 + 1)')
# print(result) 
#print(diam_from_circum(130))
#print(1.25*(10**4))
