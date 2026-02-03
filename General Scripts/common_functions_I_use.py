# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:23:06 2021

@author: sucre
"""
#from matplotlib import pyplot as plt
#import numpy as np
#import sys
import random
import datetime
import math
# import xhamster_api
# import json

pi = math.pi
light_speed_mps = 299792458


def inc(val,pct):
    return val + (val*pct)

def toPower(val,power):
    return val**power

def murph(sets):
    print("{0} squats".format(sets*3))
    print("{0} pushups".format(sets*2))
    print("{0} pullups".format(sets))

def inc_over_range(base, rg, incre):
    for y in range(1, rg + 1):
        base = inc(base, incre)
    return base

def compound(principal, rate, periods_per_year, years):
    return principal * ( (1 + rate/periods_per_year)**(periods_per_year*years) )

def getX_countO_Rolls(sides, rounds):
    result = []
    for x in range(0, rounds):
        result.append(random.randint(1, sides))
    return result
    
def max_protein_intake(bodyweight):
    return bodyweight*0.82

def min_protein_intake(bodyweight):
    return bodyweight*0.36

def bmr(weight_Kg, height_Cm, age):
    return (88.362 + (13.397 * weight_Kg) + (4.799 * height_Cm) - (5.677 * age))

def run_with_luck_mod(luck_pct):
    return

def select_rando_item(arr):
    if not arr:
        return None  # Return None if the array is empty
    return random.choice(arr)


# https://jav.guru/category/english-subbed/
# https://jav.guru/tag/mourning/
# https://jav.guru/?tag=Creampie&actress=Uehara-Ai
# https://jav.guru/?s=cheese

#https://jav.guru/category/english-subbed/?tag=dirty-talk

start_val = 100
iterations = 10
d = 1
randvar = 1
inc_pct = .1 * randvar
st_measure = 100.0
new_u = st_measure * (inc_over_range(start_val, iterations, inc_pct)/100)
new_u2 = st_measure * (inc_over_range(start_val, iterations, inc_pct*2)/100)
new_d = st_measure * (inc_over_range(start_val, iterations, -inc_pct)/100)
new_d2 = st_measure * (inc_over_range(start_val, iterations, -inc_pct*2)/100)
print(new_u)
print(new_u2)
print(new_d)
print(new_d2)

'''
st_measure = 130.0
iterations = 60
new_u = st_measure * (inc_over_range(start_val, iterations, inc_pct)/100)
new_u2 = st_measure * (inc_over_range(start_val, iterations, inc_pct*2)/100)
new_d = st_measure * (inc_over_range(start_val, iterations, -inc_pct)/100)
new_d2 = st_measure * (inc_over_range(start_val, iterations, -inc_pct*2)/100)
print(new_u)
print(new_u2)
print(new_d)
print(new_d2)
'''

'''
r1
start debt: 5000.0
current debt: 7999
manager paid: 50000.0
worker paid: 12300.0
count: 1000
days: 60
'''

start_d = 5000.0
start_d = 7999.0
j = 20.0
fee_b = 60.0
fee_p = 0.25
p_d = [15,15,15,15,15,15,15,15,15,15,
       21,21,22,23,12,20,5,25,25,25,
       21,15,15,5,15,15,15,15,15,15,
       20,20,15,15,25,20,20,10,20,20,
       20,20,15,15,10,20,20,20,20,20,
       20,20,15,15,20,20,8,15,15,15,
       ]
rng = len(p_d)
curr = start_d + 0.0
p = 0.0
earned = 0.0
s = 0
per_rate = j - (j * (fee_p))
p_th_h = 0.0

for x in range(0,len(p_d)):
    p_th_h = p_th_h + (2.5 * (j * (p_d[x]+ math.ceil(fee_b/j))))
    new_f = curr 
    if x % 7 == 0:
        new_f = math.ceil(new_f + (new_f * fee_p))
    s = s + p_d[x] + math.ceil(fee_b/j)
    new_f = new_f - math.floor((per_rate * p_d[x]))
    curr = new_f
    p = p + math.floor((per_rate * p_d[x]))

print(f'start debt: {start_d}')
print(f'current debt: {curr}')
print(f'manager paid: {p_th_h}')
print(f'worker paid: {p}')
print(f'count: {s}')
print(f'days: {rng}')

#'''
