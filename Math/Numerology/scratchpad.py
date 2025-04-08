# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:29:29 2025

@author: sucre
"""
import array

ALPHANUMERICS = "0123456789abcdefghijklmnopqrstuvwxyz"
OPERATIONS = "()^*/+-="

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

"""
• 1. This number represents power, courage, bravery, impulsiveness, willful, and resilience in life.
• 2. This number represents femininity, flexibility, partnership, over pleasing, meddling, creates divisiveness in life.
• 3. This means creativity, imagination, lifestyle, superficial, gaudy taste, inspiration, and characteristics of a celebrity.
• 4. This means consistency, good organization, patience, takes unnecessary risks, fulfills the given task well, poise, and balance.
• 5. This means versatility, mobility, sensation, urge to change the places, curiosity, impatience, ignores rules and laws, adventurous and energetic.
• 6. This means harmony, romantic personality, easily upset, constant complainer, emotionally controlling, anxious, and carries too many burdens.
• 7. This means self-analysis, explorer, aloof, has technical ability, has faith, secretive, and thinks rather than acts.
• 8. This means confidence, wisdom, material personality, loves display, fears failure, a good judge of character, has executive abilities, and has careless regards for money.
• 9. This means diversity, scale, communicativeness, impractical, depression, too generous, aimless, and insensitive to others’ feelings.
"""

class compute_helper():
    
    def __init__(self):
        """
        """
        
    @staticmethod
    def get_int_array(string):
        return_val = []
        val = string.lower()
        val = val.replace(' ', '')
        for ch in val:
            for k,v in letters.items():
                isnumeric = ch.isdigit()
                if ch in v or (isnumeric and int(ch) == k):
                    return_val.append(k)
        return return_val
    
    @staticmethod
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
    
    @staticmethod
    def bin_to_dec(binary_string):
        binary_string = binary_string[::-1]
        bit_length = len(binary_string)
        result = 0
        for x in range(0, bit_length):
            if binary_string[x] == '1':
                result += 1*(2**x)
        return result    



class input_helper():

    def __init__(self):
        """
        """

    @staticmethod
    def get_tap_code_for_letter(letter):
        if letter == 'k':
            letter = 'c'
        for x in range(1,len(tap_code)+1):
            row = tap_code[x-1]
            if letter in row:
                return [x, row.index(letter)+1]
        
# val = 'benjamin1seth2roberts'
# ints = get_int_array(val)
# single = reduce_to_numerology_single(ints)
# #print(get_tap_code_for_letter('k'))

single = compute_helper.reduce_to_numerology_single([1,9,7,3,0,8,2,7])
print(single)






