# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 09:05:01 2025

@author: BeRoberts
"""
import numbers

class numerology_helper():
    reduced_to_values = [1,2,3,4,5,6,7,8,9,11,22,33]
    number_dict = {
        1: ['a','j','s'],
        2: ['b','k','t'],
        3: ['c','l','u'],
        4: ['d','m','v'],
        5: ['e','n','w'],
        6: ['f','o','x'],
        7: ['g','p','y'],
        8: ['h','q','z'],
        9: ['i','r'] }

    @staticmethod
    def get_ints_array(value):
        value = value.lower()
        return_value = []
        for ch in value:
            ch_is_numeric = ch.isnumeric()
            for k,v in numerology_helper.number_dict.items():
                if ch in v or ch_is_numeric:
                    if ch_is_numeric and int(ch) == k:
                        return_value.append(k)
                    else:
                        return_value.append(k)
                    continue
        return return_value
    
    @staticmethod
    def reduce_array(array):
        working_array = array
        summed = sum(working_array)
        while summed not in numerology_helper.reduced_to_values:
            string_sum = str(summed)
            working_array = []
            for ch in string_sum:
                working_array.append(int(ch))
            
            summed = sum(working_array)
            
            
        return summed
        
    @staticmethod
    def compute(val):
        return numerology_helper.reduce_array(numerology_helper.get_ints_array(val))
    
print(numerology_helper.compute("Benjamin Seth Roberts"))