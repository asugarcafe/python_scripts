# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import threading
import pyttsx3
import pyttsx3.voice
import time
import random

class textspeaker():
    engine = None

    def __init__(self):
        self.set_engine()

    def set_engine(self):
        self.engine = pyttsx3.init()

    def stop_engine(self):
        self.engine.stop()

    def say_text(self, ssml_text, volume = .99):
        rate = 120
        if random.randint(0, 1) == 0:
            rate = 120 - random.randint(1, 10)
        else:
            rate = 220 - random.randint(1, 40)
        print("r: {} v: {}".format(rate, volume))
        self.engine.setProperty('rate', rate)  # Adjust the speech rate (words per minute)
        self.engine.setProperty('volume', volume)  # Adjust the speech rate (words per minute)

        # Set the voice properties to support SSML
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', random.choice(voices).id)
    
        self.engine.say(ssml_text)
        self.engine.runAndWait()


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


file_text = ""
file_path = 'r_priming.ap.txt'
# file_path = "r_visualization.improvement.txt"
# #file_path = 'r_single.line.repeater.txt'
# file_path = 'r_mentalacuity.txt'
# # file_path = 'r_manifesting.feedback.txt'
file_path = 'r_reading.comprehension.pegs.txt'
file_path = 'r_time.distortion.txt'



def run_loop(file_path, loops, repeat, randomize):
    count = 0
    desired_outcome = "to " + "improve my time distortion skill"
    while count < loop or repeat:
        # Open the file in read mode ('r')
        file_text = get_file_text(file_path, randomize)
    
        speaker = textspeaker()
            
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
                #textspeaker.text_to_speech_ssml(q, volume)
                speaker.say_text(q, volume)
    
        speaker.stop_engine()
        speaker = None
        count += 1

def run_threads_test(fp, l, r, rand):
    thread1 = threading.Thread(target=run_loop, args=('r_time.distortion.txt', l, r, rand))
    thread1.start()
    thread2 = threading.Thread(target=run_loop, args=('r_priming.ap.txt', l, r, rand))
    thread2.start()



repeat = False
randomize = True
loop = 100
run_threads_test(file_path, loop, repeat, randomize)