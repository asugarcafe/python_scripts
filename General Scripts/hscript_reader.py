# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os
import pyttsx3
import pyttsx3.voice
import time

class textspeaker():

    @staticmethod
    def text_to_speech_ssml(ssml_text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)  # Adjust the speech rate (words per minute)
    
        # Set the voice properties to support SSML
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.name == 'Microsoft Zira Desktop - English (United States)':
                engine.setProperty('voice', voice.id)
                break
    
        engine.say(ssml_text)
        engine.runAndWait()
        
    @staticmethod
    def text_to_speech(text):
        engine = pyttsx3.init(engine='sapi5')
        engine.setProperty('rate', 120)  # Adjust the speech rate (words per minute)
        engine.say(text)
        engine.runAndWait()
    
'''
https://freehypnosisscripts.com/subject-scripts/creating/
https://freehypnosisscripts.com/subject-scripts/creative-abilities/
https://freehypnosisscripts.com/subject-scripts/reading-faster/
https://freehypnosisscripts.com/

'''


ssml_text = ""
file_path = 'C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/ind_001.txt'
file_path = 'C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/kf_tiger_watches_monkey.txt'
file_path = 'C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/.txt'
file_path = 'C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/repeater.txt'

repeat = True
while True:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the entire contents of the file into a string
        ssml_text  = file.read()
        ssml_text = ssml_text.replace('.','|2|')
        
        
    q_list = [s.strip() for s in ssml_text.split('|')]
    loop = 1000
    count = 0
    for question in q_list:
        print(question)
        time.sleep(int(question)) if question.isnumeric() else textspeaker.text_to_speech_ssml(question)
        count = count + 1
        if count > loop:
            break

    if not repeat:
        break        