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
import numbers
from datasets import datasets
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
        for t in range(period):
            if t < period / 2:
                samples[t] = amplitude
            else:
                samples[t] = -amplitude
            
        return samples

    @staticmethod
    def freq_to_note(freq):
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
        #BSR: this is 440 and I have been using A = 432
        note_number = 12 * math.log2(freq / 432) + 49  
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
    def play_tones(mixer, note1, note2, seconds, loopmod=1000, high = 0.15, low = 0.01, primary = None):
        lchan = mixer.Channel(0)
        lchan2 = mixer.Channel(2)
        
        rchan = mixer.Channel(1)
        rchan2 = mixer.Channel(3)
        
        lchan.set_volume(high,low)
        rchan.set_volume(low,high)
        
        lchan2.set_volume(high,low)
        rchan2.set_volume(low,high)
        
        lchan.play(note1, loops=loopmod, maxtime=seconds*K)
        rchan.play(note2, loops=loopmod, maxtime=seconds*K)

        if primary is not None:
            lchan2.play(primary, loops=loopmod, maxtime=seconds*K)
            rchan2.play(primary, loops=loopmod, maxtime=seconds*K)

        time.sleep(seconds)
        lchan.stop()
        rchan.stop()
        lchan2.stop()
        rchan2.stop()

    @staticmethod
    def play_scale_hemisynchronous(scale, seconds_per_tone, hemi_tone = 6):
        bit = False
        for step in scale:
            if isinstance(step, (int,float)):
                note1 = [float(step), float(step)]
            else:
                note1 = datasets.note_freq_wavelength(notes,step)
            true_note = Note(note1[0])
            
            #BSR: this math is off, 
            # https://agentcalc.com/binaural-beat-frequency-calculator
            freq1 = note1[0] - (hemi_tone/2)
            freq2 = note1[0] + (hemi_tone/2)
            #BSR: fix the math above
            
            print(str(step) + ' - ' + str(note1[0]))
            print('Hemi tone: ' + str(hemi_tone))
            print(freq1)
            print(freq2)
            note1 = Note(freq1) if bit else Note(freq2)
            note2 = Note(freq2) if bit else Note(freq1)
            bit = not bit
            player.play_tones(pygame.mixer, note1, note2, seconds_per_tone, K*((seconds_per_tone**2)), primary=true_note)

    @staticmethod
    def play_schumman(seconds_per_tone):
        hemi_tone = 7.83
        note1 = 400.00 #datasets.note_freq_wavelength(notes,step)
        freq1 = note1 - (hemi_tone/2)
        freq2 = note1 + (hemi_tone/2)
        note1 = Note(freq1)
        note2 = Note(freq2)
        player.play_tones(pygame.mixer, note1, note2, seconds_per_tone, K*((seconds_per_tone**2)))

notes = datasets.NotesA432()

A4 = datasets.note_freq_wavelength(notes,'A4')
E0 = datasets.note_freq_wavelength(notes,'E0')
c4 = datasets.note_freq_wavelength(notes,'C4')

blues_scale_A_fmt = ['A{0}','C{0}','D{0}','D#{0}/Eb{0}','E{0}','G{0}']
whole_notes_fmt = ['A{0}','B{0}','C{0}','D{0}','E{0}','F{0}','G{0}']
chakras = ['A2','B2','C3','C#3/Db3','D3','D#3/Eb3','E3','F#3/Gb3','G3']
#chakras = ['A1','B1','C2','C#2/Db2','D2','D#2/Eb2','E2','F#2/Gb2','G2']
#chakras = ['A3','B3','C4','C#4/Db4','D4','D#4/Eb4','E4','F#4/Gb4','G4']
#chakras = [396.0, 417.0, 528.0, 639.0, 741.0, 852.0, 963.0]
#chakras = [528.0, 639.0, 741.0]
short = [128.43,132.25,136.07,132.25]
short = [108.00,111.21,114.42,111.21]



scale_to_use = short

pygame.init()
# Set a wait duration in seconds
duration = 2
# Initialize the mixer
pygame.mixer.init(channels=4)
player = toneplayer()
bit = True
seconds_per_tone = 30


# set the hemi-tone to hear
wobble_at = 6
while True:
    player.play_scale_hemisynchronous(scale_to_use, seconds_per_tone, wobble_at)
    #player.play_schumman(seconds_per_tone)

# Quit the pygame mixer
pygame.mixer.quit()