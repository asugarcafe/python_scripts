# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:11:43 2025

@author: sucre
"""
import array

letters = {
1 : ['a','j','s'],
2 : ['b','k','t'],
3 : ['c','l','u'],
4 : ['d','m','v'],
5 : ['e','n','w'],
6 : ['f','o','x'],
7 : ['g','p','y'],
8 : ['h','q','z'],
9 : ['i','r']}

tap_code = [
    ['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['l','m','n','o','p'],
    ['q','r','s','t','u'],
    ['v','w','x','y','z'],
    ]

def get_int_array(value):
    return_val = []
    val = value.lower()
    val = val.replace(' ', '')
    for ch in val:
        for k,v in letters.items():
            if ch in v:
                return_val.append(k)
    return return_val

def reduce_to_numerology_single(intarray):
    returnable = [1,2,3,4,5,6,7,8,9,11,22,33]
    summed = sum(intarray)
    str_summed = str(summed)
    
    while summed not in returnable:
        new_array = []
        for ch in str_summed:
            new_array.append(int(ch))
        
        summed = sum(new_array)
        str_summed = str(summed)

    return int(str_summed)
