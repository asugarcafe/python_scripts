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
        engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    
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
        engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
        engine.say(text)
        engine.runAndWait()
    
    def read_files_in_folder(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):  # Change the file extension if needed
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    print(f"Reading content of file: {file}\n")
                    print(content)
                    print("\n\nReading content through text-to-speech...\n")
                    textspeaker.text_to_speech(content)



ssml_text = '''
How can I best orient myself towards the next part of my day?20?
How can I get my best performance out of myself today?20?
On a scale of 1-10 how intense should my positive and empowering states be today?15?
What do I love about myself right now?20? what about that makes me love myself?10? how does that make me feel?30?
What do I respect about myself right now?20? what about that makes me respect myself?10? how does that make me feel?30?
How am I choosing positivity in my life right now?20? why am I choosing positivity?10? how does that make me feel?30?
What am I happy about in my life right now?20? what about that makes me feel happy?10? how does that make me feel?30?
What am I excited about in my life right now?20? what about that makes me feel excited?10? how does that make me feel?30?
What am I proud about in my life right now?20? what about that makes me feel pride?10? how does that make me feel?30?
How do I want to be accepted today?30? how will I accept others?10? how will I accept myself?30?
What am I experiencing right now that let's me know I'm wealthy?30?How can I create more wealth in my life?15?How can I share my wealth with others?30?
How can I make my goals my reality as quickly as possible?30?
What am I responsible for today?20? How should I best handle those responsibilities?
'''

q_list = [s.strip() for s in ssml_text.split('?')]

for question in q_list:
    print(question)
    time.sleep(int(question)) if question.isnumeric() else textspeaker.text_to_speech_ssml(question + "?")
    