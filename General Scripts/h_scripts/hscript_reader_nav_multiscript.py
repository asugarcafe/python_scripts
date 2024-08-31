# -*- coding: utf-8 -*-
"""
Created on 2024-08-30

@author: sucrerey
"""
import pyttsx3
import pyttsx3.voice
import time
import random
from pynput import keyboard

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


class script_navigator:
    scripts = [""]    
    current_script = scripts[0]
    
    script_index = 0
    
    def __init__(self, script_array):
        """
        """
        self.scripts = script_array

    def get_current_script(self):
        return self.scripts[self.script_index]

    def set_script(self, index):
        self.script_index = index
        self.current_script = self.scripts[self.script_index]
        
    def move_back(self):
        if self.script_index > 0:
            self.script_index = self.script_index - 1    
        self.set_script(self.script_index)
        
    def move_forward(self):
        if self.script_index < len(self.scripts) -1:
            self.script_index = self.script_index + 1    
        self.set_script(self.script_index)
        
        
    
class script_reader:
    #interrupt is a bool so both the script navigator 
    #and the reader can handle user input
    interrupt = False
    exit_program = False
    navigator = script_navigator([""])
    target_id = ""

    def __init__(self, the_scripts, targetid):
        """
        """
        self.navigator = script_navigator(the_scripts)
        self.target_id = targetid

    def on_press(self, key):
                
        if key == keyboard.Key.right or key == keyboard.Key.up or key == keyboard.Key.page_up:
            self.navigator.move_forward()
            self.interrupt = True;
                
        if key == keyboard.Key.left or key == keyboard.Key.down or key == keyboard.Key.page_down:
            self.navigator.move_back()
            self.interrupt = True;
                
        if key == keyboard.Key.esc or key == keyboard.Key.end:
            self.exit_program = True;
            
    def get_script_lines(self, script_file):
            #open the current file
            with open(script_file, 'r', encoding='utf-8') as file:
                # Read the entire contents of the file into a string
                file_text = file.read()
                file_text = file_text.replace('.','|1|')
                
            #split the file into an array of statements
            return [s.strip() for s in file_text.split('|')]

    def loop_current_script(self):

        while not self.exit_program:
        
            q_list = self.get_script_lines(self.navigator.get_current_script())
            #count = 0
            for question in q_list:
                if self.interrupt:
                    self.interrupt = False
                    break
                if self.exit_program:
                    return
                
                if question.isnumeric():
                    print(question)                    
                    time.sleep(int(question))
                else:
                    q = question.replace("#{TARGET_ID}", self.target_id)
                    print(q) 
                    volume = random.choice([.3, .6, .9, .12, .24])
                    textspeaker.text_to_speech_ssml(q, volume)
            
            #loop over the array, reading the statements
                #listen for interrupt

    def main_loop(self):
        
        listener = keyboard.Listener(on_press=self.on_press)
        # run listener in background so that the while loop gets executed
        listener.start()
        
        self.navigator.set_script(0)
        
        while not self.exit_program:
            self.loop_current_script()
        
        listener.stop()
        
      

TARGET_ID = "wwqrx94a" #"20.214573506000978, -87.42889533936818"
my_scripts = ["C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\remote_viewing\\r_rv.induction.txt",
            "C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/remote_viewing/r_rv.movement.to.target.txt",
            "C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\remote_viewing\\r_rv.major.gestalt.txt",
            "C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/remote_viewing/r_rv.sensory.contact.txt",
            "C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/remote_viewing/r_rv.dimension.txt",
            "C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/remote_viewing/r_rv.general.aspects.txt",
            "C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/remote_viewing/r_rv.specific.aspects.txt",
            "C:/Repos/github_asugarcafe/python_scripts/General Scripts/h_scripts/remote_viewing/r_rv.modeling.txt",]



reader = script_reader(my_scripts, TARGET_ID)
reader.main_loop()

        
    
