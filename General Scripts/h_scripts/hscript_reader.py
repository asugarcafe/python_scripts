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

    @staticmethod
    def text_to_speech_ssml(ssml_text, volume = .99):
        engine = pyttsx3.init()
        if random.randint(0, 1) == 0:
            rate = 120 - random.randint(1, 10)
        else:
            rate = 220 - random.randint(1, 40)
        print("r: {} v: {}".format(rate, volume))
        engine.setProperty('rate', rate)  # Adjust the speech rate (words per minute)
        engine.setProperty('volume', volume)  # Adjust the speech rate (words per minute)

        # Set the voice properties to support SSML
        voices = engine.getProperty('voices')
        engine.setProperty('voice', random.choice(voices).id)
    
        engine.say(ssml_text)
        engine.runAndWait()
        #engine.stop()


'''
https://freehypnosisscripts.com/subject-scripts/creative-abilities/

'''


loop = 100
file_text = ""
file_path = 'r_priming.ap.txt'
# file_path = "r_visualization.improvement.txt"
# #file_path = 'r_single.line.repeater.txt'
# file_path = 'r_mentalacuity.txt'
# # file_path = 'r_manifesting.feedback.txt'
file_path = 'r_reading.comprehension.pegs.txt'


desired_outcome = "to " + "open and hone your psychic senses"
repeat = True
randomize = True
count = 0
while count < loop or repeat:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the entire contents of the file into a string
        if randomize:
            file_lines = file.readlines()
            random.shuffle(file_lines)
            file_text  = "".join(file_lines)
        else:
            file_text  = file.read()

        #split the file into statements and wait periods
        file_text = file_text.replace('.','|2|')

        
    q_list = [s.strip() for s in file_text.split('|')]
    for question in q_list:
        print(question)
        #if the value is numeric, wait that many seconds
        if question.isnumeric():
            time.sleep(int(question))
        else:
            #replace values in outcome-specific scripts
            q = question.replace("#{GOAL}", desired_outcome)
            #random volume
            volume = random.choice([.3, .6, .9, .12, .24])
            #speak the statement,
            #this function randomizes TTS voice and speech rate
            textspeaker.text_to_speech_ssml(q, volume)

    count += 1