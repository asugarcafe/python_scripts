# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:13:06 2023

@author: sucre
"""
import json
from collections import Counter

def count_occurrences(arr):
    # Use Counter to count occurrences of each number in the array
    counts = Counter(arr)
    
    return counts


def split_string_by_length(s, length):
    """
    Split a string into substrings of a specific length.
    
    Args:
    - s (str): The input string to be split.
    - length (int): The desired length of each substring.
    
    Returns:
    - list: A list of substrings of the input string, each with the specified length.
    """
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Iterate over the input string with a step of 'length'
    for i in range(0, len(s), length):
        # Append the substring of length 'length' to the list
        substrings.append(s[i:i+length])
    
    return substrings


# binary = """1010011000100110100 001101110011000000 11000 10011010100 110000 00110101 010100 1100110111 00110101001100010 0 110110011011100 1100000110 10 00 0 1 1 00 1 1 010101 1100110011 0011 0 110 0011001000110101 001101100011 10000011 0100 00 11 0 1 0 1 01 001110 001100 01 001 1 0 0010 0110 111 0011 0001 0011000000 11 0000 0011 01 10 0011 0011 0011 0010 010001010 0110011001101110011000 1001100010011 000000110001 00111001001 101010100111 0 0011 0010 00110101 00110011001 10 1 11 0011 00100011001000111000 0011 000101000 10 10100010101011001 01000 101 0 101 0011 010011110100011 0 010110010100111101 01010101010010 0100010101011001 01 000 0 10 10 10100110100111101010010 0100100101000111 0100100101001110 0011010100110010 0011 000 00 111001 00 11 0100 00110010 001101 01 0011 0011 0011 0010 01001110 00110001 00 11 00110011 000 1 001100110011 0001 00 11 0010 00110110 011100101010 11101 00 111101010010 01 001 00 1 0 1 00 0 111 01001001 0100 11 1 0 0101100101000 1010100000 1 010100 1000111000 001100 01 00110 000 0011000 0"""
# split = binary.split(" ")
# b = binary.replace(' ','')
# segs = split_string_by_length(b, 4)
# chars = []
# for seg in segs:
#     bin_val = int(seg, 2)
#     char_val = chr(bin_val)
#     chars.append(char_val)
j = 0.5
k = 0.25
print((7*j) + 5 - (8*k))