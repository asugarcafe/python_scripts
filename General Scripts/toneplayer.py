# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:53:00 2023

@author: sucre
"""
import math
from array import array
import time
from time import sleep
import pygame
from pygame.mixer import Sound, get_init, pre_init
import sys, os
from datasets import datasets
#sys.path.insert(0, 'E:/Dropbox/Work/Self Study/python/ScienceAndPrecisionCalc/tone.data.py')
K = 1000

class Note(Sound):

    def __init__(self, frequency, volume=.04):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
            
        return samples

    @staticmethod
    def freq_to_note(freq):
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
        #BSR: this is 440 and I have been using 432
        note_number = 12 * math.log2(freq / 440) + 49  
        note_number = round(note_number)
            
        note = (note_number - 1 ) % len(notes)
        note = notes[note]
        
        octave = (note_number + 8 ) // len(notes)
        
        return [note, octave]
    
class toneplayer():
     
    @staticmethod
    def calc_2nd_freq(goal_beat_frequency, first_frequency):
        return first_frequency + goal_beat_frequency
    
    #https://www.omnicalculator.com/physics/beat-frequency
    
    @staticmethod
    def play_tones(mixer, note1, note2, seconds, loopmod=1000, high = 0.25, low = 0.01):
        lchan = mixer.Channel(0)
        rchan = mixer.Channel(1)
        lchan.set_volume(high,low)
        rchan.set_volume(low,high)
        lchan.play(note1, loops=loopmod, maxtime=seconds*K)
        rchan.play(note2, loops=loopmod, maxtime=seconds*K)
        time.sleep(seconds)
        lchan.stop()
        rchan.stop()

    @staticmethod
    def play_scale_hemisynchronous(scale, seconds_per_tone):
        bit = False
        for step in scale:
            note1 = datasets.note_freq_wavelength(notes,step)
            off_pct = note1[0] * 0.015
            print(off_pct)
            freq1 = note1[0] - off_pct
            freq2 = note1[0] + off_pct
            print(step)
            print(freq1)
            print(freq2)
            note1 = Note(freq1) if bit else Note(freq2)
            note2 = Note(freq2) if bit else Note(freq1)
            bit = not bit
            player.play_tones(pygame.mixer, note1, note2, seconds_per_tone, K*((seconds_per_tone**2)))

notes = datasets.NotesA432()

A4 = datasets.note_freq_wavelength(notes,'A4')
E0 = datasets.note_freq_wavelength(notes,'E0')
c4 = datasets.note_freq_wavelength(notes,'C4')

blues_scale_A_fmt = ['A{0}','C{0}','D{0}','C#{0}/Db{0}','E{0}','G{0}']
whole_notes_fmt = ['A{0}','B{0}','C{0}','D{0}','E{0}','F{0}','G{0}']
chakras = ['A2','B2','C3','C#3/Db3','D3','D#3/Eb3','E3','F#3/Gb3','G3']


scale_to_use = chakras

pygame.init()

# Set a wait duration in seconds
duration = 2

# Initialize the mixer
pygame.mixer.init(channels=2)

scale_index = 4
goal_freq = A4[0]
ms = 1000
seconds = 1
sec = ms * seconds


#play_tones(pygame.mixer, Note(goal_freq), Note(goal_freq), 3, loopmod=10000)


player = toneplayer()
bit = True




player.play_scale_hemisynchronous(chakras, 3)










'''
for x in range(0,1):
    for step in scale_to_use:
        bit = not bit
        n = step.format(x)
        print(n)
        note1 = datasets.note_freq_wavelength(notes,n)
        freq1 = note1[0] 
        freq2 = player.calc_2nd_freq(goal_freq, freq1) # 99.9
        print(freq1)
        print(freq2)
        note1 = Note(freq1) if bit else Note(freq2)
        note2 = Note(freq2) if bit else Note(freq1)
        player.play_tones(pygame.mixer, note1, note2, seconds, K*((x+3)^2))
'''



'''
left_channel.play(note1, loops=dur1)
print('playing note 1')
time.sleep(1)
right_channel.play(note2, loops=dur2)
print('playing note 2')
time.sleep(seconds)
'''
# print('stopping note 1')
# left_channel.stop()
# print('stopping note 2')
# right_channel.stop()

# Quit the pygame mixer
pygame.mixer.quit()


#next play through an arpeggio of note 
#combinations that all resonate the goal frequency

'''
as for a sensible plan. you dont have one. you are a simp. youre jealous of a loser; making you less than a loser. if you want to attract her dont use magick, just be more of a loser than him. be broken in the way she feels compelled to fix. be the exact kind of loser bait she'd fall for. congratulation, you now know what the demon is going to tell you when you present that plan.

or, use the power of magick to free yourself and literally make everything in your life better. first, you could free yourself from the stupid fucking delusion that some bitch with no sense is worth wasting good magick on.
'''