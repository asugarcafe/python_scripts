# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:53:00 2023

@author: sucrerey
"""
from array import array
import time
import pygame
from pygame.mixer import Sound, get_init, pre_init
import pandas as pd
from io import StringIO
K = 1000

class datasets:
    
    def __init__(self):
        '''
        '''
        
    @staticmethod
    def NotesA432():
        # Paste the provided data into a string
        data_string = """Note,FreqHz,WavelengthCM
C0,16.05,2148.96
C#0/Db0,17.01,2028.35
D0,18.02,1914.50
D#0/Eb0,19.09,1807.05
E0,20.23,1705.63
F0,21.43,1609.90
F#0/Gb0,22.70,1519.54
G0,24.05,1434.26
G#0/Ab0,25.48,1353.76
A0,27.00,1277.78
A#0/Bb0,28.61,1206.06
B0,30.31,1138.37
C1,32.11,1074.48
C#1/Db1,34.02,1014.17
D1,36.04,957.25
D#1/Eb1,38.18,903.53
E1,40.45,852.81
F1,42.86,804.95
F#1/Gb1,45.41,759.77
G1,48.11,717.13
G#1/Ab1,50.97,676.88
A1,54.00,638.89
A#1/Bb1,57.21,603.03
B1,60.61,569.19
C2,64.22,537.24
C#2/Db2,68.04,507.09
D2,72.08,478.63
D#2/Eb2,76.37,451.76
E2,80.91,426.41
F2,85.72,402.47
F#2/Gb2,90.82,379.89
G2,96.22,358.56
G#2/Ab2,101.94,338.44
A2,108.00,319.44
A#2/Bb2,114.42,301.52
B2,121.23,284.59
C3,128.43,268.62
C#3/Db3,136.07,253.54
D3,144.16,239.31
D#3/Eb3,152.74,225.88
E3,161.82,213.20
F3,171.44,201.24
F#3/Gb3,181.63,189.94
G3,192.43,179.28
G#3/Ab3,203.88,169.22
A3,216.00,159.72
A#3/Bb3,228.84,150.76
B3,242.45,142.30
C4,256.87,134.31
C#4/Db4,272.14,126.77
D4,288.33,119.66
D#4/Eb4,305.47,112.94
E4,323.63,106.60
F4,342.88,100.62
F#4/Gb4,363.27,94.97
G4,384.87,89.64
G#4/Ab4,407.75,84.61
A4,432.00,79.86
A#4/Bb4,457.69,75.38
B4,484.90,71.15
C5,513.74,67.15
C#5/Db5,544.29,63.39
D5,576.65,59.83
D#5/Eb5,610.94,56.47
E5,647.27,53.30
F5,685.76,50.31
F#5/Gb5,726.53,47.49
G5,769.74,44.82
G#5/Ab5,815.51,42.30
A5,864.00,39.93
A#5/Bb5,915.38,37.69
B5,969.81,35.57
C6,1027.47,33.58
C#6/Db6,1088.57,31.69
D6,1153.30,29.91
D#6/Eb6,1221.88,28.24
E6,1294.54,26.65
F6,1371.51,25.15
F#6/Gb6,1453.07,23.74
G6,1539.47,22.41
G#6/Ab6,1631.01,21.15
A6,1728.00,19.97
A#6/Bb6,1830.75,18.84
B6,1939.61,17.79"""
        
        # Use StringIO to simulate reading from a file
        data_io = StringIO(data_string)
        
        # Read the data into a DataFrame
        music_notes_df = pd.read_csv(data_io)
        
        # Display the DataFrame
        return music_notes_df

    @staticmethod
    def note_freq_wavelength(notes, target_note = 'C4'):        
        freq_wave = [0,0]
        # Check if the note exists in the DataFrame
        if target_note in notes['Note'].values:
            # Access the row corresponding to the target note
            row = notes.loc[notes['Note'] == target_note]
        
            # If you want to access specific values, for example, the frequency
            freq_wave = [row['FreqHz'].values[0],row['WavelengthCM'].values[0]]
            
        return freq_wave

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


class toneplayer():
     
    #https://www.omnicalculator.com/physics/beat-frequency
    
    @staticmethod
    def play_tones(mixer, note1, note2, seconds, loopmod=1000, high = 0.25, low = 0.01, base_tone = 0):
        lchan = mixer.Channel(0)
        rchan = mixer.Channel(1)
        lchan.set_volume(high,low)
        rchan.set_volume(low,high)
        if base_tone > 0 :
            lchan.play(note1 + (base_tone/2), loops=loopmod, maxtime=seconds*K)
            rchan.play(note2 - (base_tone/2), loops=loopmod, maxtime=seconds*K)
        lchan.play(note1, loops=loopmod, maxtime=seconds*K)
        rchan.play(note2, loops=loopmod, maxtime=seconds*K)
        time.sleep(seconds)
        lchan.stop()
        rchan.stop()

    @staticmethod
    def play_scale_hemisynchronous(scale, seconds_per_tone, hemi_tone = 6):
        bit = False
        for step in scale:
            note1 = datasets.note_freq_wavelength(notes,step)
            freq1 = note1[0] - (hemi_tone/2)
            freq2 = note1[0] + (hemi_tone/2)
            print(step + ' - ' + str(note1[0]))
            print('Hemi tone: ' + str(hemi_tone))
            print(freq1)
            print(freq2)
            note1 = Note(freq1) if bit else Note(freq2)
            note2 = Note(freq2) if bit else Note(freq1)
            bit = not bit
            player.play_tones(pygame.mixer, note1, note2, seconds_per_tone, K*((seconds_per_tone**2)))

    @staticmethod
    def play_schumman_400(seconds_per_tone, mid_shift):
        hemi_tone = 7.83
        note1 = 400.00 #datasets.note_freq_wavelength(notes,step)
        freq1 = note1 - (hemi_tone/2)
        freq2 = note1 + (hemi_tone/2)
        if not mid_shift:
            freq1 = note1
            freq2 = note1 + hemi_tone
        note1 = Note(freq1)
        note2 = Note(freq2)
        player.play_tones(pygame.mixer, note1, note2, seconds_per_tone, K*((seconds_per_tone**2)))

#get the notes database
notes = datasets.NotesA432() #only have A=432 but you can add your own
blues_scale_A_fmt = ['A{0}','C{0}','D{0}','D#{0}/Eb{0}','E{0}','G{0}']
whole_notes_fmt = ['A{0}','B{0}','C{0}','D{0}','E{0}','F{0}','G{0}']
chakras = ['A3','B3','C4','C#4/Db4','D4','D#4/Eb4','E4','F#4/Gb4','G4']
scale_to_use = chakras

pygame.init()
# Set a wait duration in seconds
duration = 2
# Initialize the mixer
pygame.mixer.init(channels=2)
#create the tone player
player = toneplayer()

#set some base vars
bit = True
seconds_per_tone = 9
# set the hemi-tone to hear
wobble_at = 7.83 # schumman resonance
while True:
    #the following line loops over a scale playing mid-shifted hemi-tones
    player.play_scale_hemisynchronous(scale_to_use, seconds_per_tone, wobble_at)

    #the following line plays OPs notes but mid-shifted,
    #switch last parameter to False to play OPs exact tones
    player.play_schumman_400(seconds_per_tone, True)

# Quit the pygame mixer
pygame.mixer.quit()