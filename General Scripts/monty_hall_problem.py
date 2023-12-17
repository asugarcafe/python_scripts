# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:10:47 2021

@author: sucre
"""
import random
import pandas as pd
import numpy as np
from enum import Enum


class Prize(Enum):
    Car = 1
    Goat = 0
    ShownGoat = -1

def rnd(seed):
    return random.randint(0,seed)
    
    
def put_prizes_behind_doors():
    doors = [Prize.Goat, Prize.Goat, Prize.Goat]
    doors[rnd(2)] = Prize.Car
    return doors

def show_one_goat(player_selected_door, doors):
    prize_door = doors.index(Prize.Car)
    if player_selected_door == prize_door:
        #show the first available door
        doors[doors.index(Prize.Goat)] = Prize.ShownGoat
    else:
        for door_index in range(0, 3):
            #print(door_index)
            if door_index != player_selected_door and door_index != prize_door:
                doors[door_index] = Prize.ShownGoat
                break
        
    return doors

def select_other_door(player_selected_door, doors):
    opened_door = doors.index(Prize.ShownGoat)
    for door_index in range(0, 3):
        if door_index != opened_door and door_index != player_selected_door:
            return door_index
    

df = pd.DataFrame(columns=['Doors', 'Player initial choice', 'Result if door kept', 'Result if door changed'])

for x in range(0,10000):
    doors = put_prizes_behind_doors()
    prize_index = doors.index(Prize.Car)
    #print(doors)
    player_door_choice = rnd(2)
    #print("Player chose door number {0}.".format(player_door_choice))
    doors = show_one_goat(player_door_choice, doors)
    #print(doors)
    #print("Player shown goat behind door number {0}".format(doors.index(Prize.ShownGoat)))
    new_selection = select_other_door(player_door_choice, doors)
    #print("Player can now choose door number {0}.".format(new_selection))
    result_1 = 0
    result_2 = 0
    if (prize_index == player_door_choice):
        result_1 = 1    
    if (prize_index == new_selection):
        result_2 = 1    
    
    df.loc[x] = [doors,player_door_choice, result_1, result_2]
    
kept_range = df['Result if door kept']    
new_select_range = df['Result if door changed']    

print("Player wins by keeping initial selection {0}% of the time.".format((sum(kept_range)/len(kept_range))*100))
print("Player wins by making new selection {0}% of the time.".format((sum(new_select_range)/len(new_select_range))*100))




