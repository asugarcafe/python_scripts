# -*- coding: utf-8 -*-

import math
E = 9.81

def fall_distance_M(seconds):
    return E*math.exp(seconds)




print(E*2)
print(E+(E*2))
print(fall_distance_M(2))