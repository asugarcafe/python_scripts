# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os
import pyttsx3
import pyttsx3.voice
import time
import random

class textspeaker():
    engine = None
    voices = None
    
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        
    def silence(self):
        self.engine.stop()
        
    def getRand(self, upper):
        return random.randint(1, upper)
        

    def text_to_speech(self, text, volume = .99):
        if self.getRand(1) == 0:
            if random.randint(0, 1) == 0:
                rate = 100 - self.getRand(10)
            else:
                rate = 200 - self.getRand(10)
        else:
            rate = 160 - self.getRand(40)
        print("r: {} v: {}".format(rate, volume))
        self.engine.setProperty('rate', rate)  # Adjust the speech rate (words per minute)
        self.engine.setProperty('volume', volume)  # Adjust the speech rate (words per minute)

        # Set the voice properties to support SSML
        self.engine.setProperty('voice', random.choice(self.voices).id)

    
        self.engine.say(text)
        self.engine.runAndWait()

    @staticmethod
    def text_to_speech_ssml(ssml_text, volume = .99):
        engine = pyttsx3.init()
        if random.randint(0, 1) == 0:
            if random.randint(0, 1) == 0:
                rate = 100 - random.randint(1, 10)
            else:
                rate = 200 - random.randint(1, 10)
        else:
            rate = 160 - random.randint(1, 40)
        print("r: {} v: {}".format(rate, volume))
        engine.setProperty('rate', rate)  # Adjust the speech rate (words per minute)
        engine.setProperty('volume', volume)  # Adjust the speech rate (words per minute)

        # Set the voice properties to support SSML
        voices = engine.getProperty('voices')
        engine.setProperty('voice', random.choice(voices).id)

    
        engine.say(ssml_text)
        engine.runAndWait()

def get_file_text(file, randomize_lines=True):
    file_text = ''
    with open(file, 'r') as file:
        # Read the entire contents of the file into a string
        if randomize_lines:
            file_lines = file.readlines()
            random.shuffle(file_lines)
            file_text  = "".join(file_lines)
        else:
            file_text  = file.read()

        #split the file into statements and wait periods
        file_text = file_text.replace('.','|1|')
        file.close()
    return file_text


'''
https://freehypnosisscripts.com/subject-scripts/creative-abilities/

'''


loop = 100
file_path = "r_single.line.repeater.txt"
#file_path = 'r_priming.ap.txt'
#file_path = "r_visualization.improvement.txt"
#file_path = 'r_mnemonics.electrical.txt'
file_path = 'r_mentalacuity.txt'
# # file_path = 'r_manifesting.feedback.txt'
#file_path = 'r_reading.comprehension.pegs.txt'
#file_path = 'r_time.distortion.txt'
#file_path = 'r_memory.txt'
<<<<<<< Updated upstream
#file_path = 'r_memory.card.pegs.txt'
file_path = 'r_manifestation.healing.txt'
=======
file_path = 'r_memory.card.pegs.txt'
#file_path = 'r_manifestation.healing.txt'
>>>>>>> Stashed changes


desired_outcome = "to " + "slow down time at will"
repeat = True
randomize = False
count = 0
speaker = textspeaker()
while count < loop or repeat:
    # Open the file in read mode ('r')
    file_text = get_file_text(file_path, randomize)

    q_list = [s.strip() for s in file_text.split('|')]
    for question in q_list:
        #if the value is numeric, wait that many seconds
        if question.isnumeric():
            time.sleep(int(question))
            print(question)
        else:
            #replace values in outcome-specific scripts
            q = question.replace("#{GOAL}", desired_outcome)
            #random volume
            volume = random.choice([.45, .55, .65])
            #speak the statement,
            #this function randomizes TTS voice and speech rate
            print(q)
            if q != '':
                speaker.text_to_speech(q, volume) 

    count += 1
    
'''speaker.silence()'''