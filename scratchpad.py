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

# Example usage:
phi_76 = [3,3,7,8,4,6,8,8,4,9,5,1,8,5,7]
la_clip = [4,3,7,7,4,1,5,2,5,2,4,8,6,3,1,8,4]
result = count_occurrences(phi_76)
print(result)
result = count_occurrences(la_clip)
print(result)

sun = 7
l_path = 1
bd = 27
py = 6
py_n = 7