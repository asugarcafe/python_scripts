# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:57:38 2023

@author: sucre
"""

def print_ether_alcohol_ingredients(grams_of_seeds):
    seeds = 75
    grams = 2.7
    seed_to_gram_rate = seeds/grams
    ethanol_ml_rate = seeds/10
    seedcount = grams_of_seeds*seed_to_gram_rate
    print("{0} grams, {1} seeds".format(grams_of_seeds, seedcount))
    print("{0} mL ethanol".format(seedcount / ethanol_ml_rate))


#print(seeds/grams)

print_ether_alcohol_ingredients(2.7)

# shumann = 7.83
# #print((shumann**4)*8192)


# length_m = 2.434
# length_in = 95.66929
# Hz = 30791935.74776832
# MHz = 30.79