# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os, time, random
import pyttsx3
import pyttsx3.voice
import tkinter, win32api, win32con, pywintypes
from tkinter import ttk

fonts = ["Aharoni","Arial",
         "Bahnschrift","Calibri",
         "Comic Sans MS","Corbel",
         "David","Georgia",
         "Segoe UI","Tahoma",]
sizes = [24,64]
font_colors = ["red", "blue", "blue4",
               "brown4","burlywood4",
               "cadetblue4",
               "green", "aquamarine4",
               "darkolivegreen4", "darkgreen",
               "darkorchid4", "darkslateblue",
               "darkslategray", "deeppink4",
               "firebrick", "firebrick4",
               "indigo", "lightblue4",
               "black", "bisque4"]

def quit_label(lbl):
    lbl.master.destroy()
    lbl.quit()

def create_disappearing_label(caption, dur_ms):
    #print(caption)
    rand_font = get_random_font()
    # rand_style = ttk.Style()
    # rand_style.configure("BoldLabel", font=(rand_font[0], int(rand_font[1]), "bold"))
    label = tkinter.Label(text=caption, 
                          wraplength=1200,
                          font=(rand_font[0], int(rand_font[1]), "bold"), 
                          fg=get_random_font_color(), 
                          anchor=tkinter.CENTER,
                          justify=tkinter.CENTER,
                          bg='black')
    label.master.overrideredirect(True)
    label.master.geometry(get_random_position())
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "black")
    
    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
    # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    label.pack()
    label.after(dur_ms, lambda: quit_label(label))
    label.mainloop()

def get_random_font():
    font = random.choice(fonts)
    size = random.randrange(sizes[0],sizes[1])
    return (font, str(size))

def get_random_position():
    max_top = 700
    max_left = 800
    top = random.randrange(1,max_top)
    left = random.randrange(1,max_left)
    return "+{0}+{1}".format(left,top)

def get_random_font_color():
    return random.choice(font_colors)


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
        

    def text_to_speech(self, text, volume = .99, rate='fast'):
        flip = 0
        
        uppers = [180,260,200]
        if rate == 'vfast':
            uppers = [255,305,355]
        if rate == 'slow':
            uppers = [90,130,200]
        if rate == 'both':
            uppers = [180,260,200,90,130,200]
            
        if random.randint(0, 1) == 0:
            if random.randint(0, 1) == 0:
                rate = uppers[0] - self.getRand(10)
                flip = 1
            else:
                rate = uppers[1] - self.getRand(10)
                flip = 2
        else:
            rate = uppers[2] - self.getRand(40)
            flip = 3


        print("r{}: {} v: {}".format(flip, rate, volume))
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
    all_lines = []
    file_lines = []
    files = []
    file_text = ''
    if type(file) == str:
        files = [file]
    else:
        files = file

    for f in files:
        #print(f)
        with open(f, 'r') as curr_file:
            # Read the entire contents of the file into an array
            file_lines = curr_file.readlines()
            all_lines.extend(file_lines)
            print(len(all_lines))
            curr_file.close()

    if randomize_lines:
        random.shuffle(all_lines)

    file_text  = "".join(all_lines)
    file_text = file_text.replace('.','|1|')

    return file_text


'''
https://freehypnosisscripts.com/subject-scripts/creative-abilities/

'''


file_path = []
#file_path.append("r_single.line.repeater.txt")
#file_path.append('r_priming.ap.txt')
#file_path.append("r_visualization.improvement.txt")
#file_path.append('r_mnemonics.electrical.txt')
#file_path.append('r_mentalacuity.txt')
#file_path.append('r_manifesting.feedback.txt')
#file_path.append('r_reading.comprehension.pegs.txt)'
#file_path.append('r_time.distortion.txt')
#file_path.append('r_memory.txt')
#file_path.append('r_dream_job.txt')
#file_path.append('r_dream_job.a.txt')
#file_path.append('r_goal.questions.txt')
#file_path.append('r_metaphysical.chakras.txt')
#file_path.append('r_manifestation.healing.txt')
#file_path.append('r_single.line.repeater.txt')
file_path.append('r_meditation.manifestation.coaching.txt')
file_path.append('dickens_leverage_pain.txt')
file_path.append('dickens_leverage_pleasure.txt')
#file_path.append('r_shinanju.txt')
multifile = file_path


manifestation = []
# manifestation.append(" I receive thirteen thousand dollars every month ")
# manifestation.append(" I have mastered my chee energy and use it like a master of sheenanjoo ")
# manifestation.append(" I control and direct my chee energy ")
# manifestation.append(" I reed peoples emotions easily whenever I want ")
# manifestation.append(" I consciously strengthen and focus my will throughout the day ")
#"""
# manifestation.append(" I have my dream job and I love it more every workday ")
# manifestation.append(" I feel liberated because I earn great money from my dream job ")
# manifestation.append(" I feel great relief that I earn great money from my dream job ")
# manifestation.append(" I feel pride in the skill I demonstrate at my dream job ")
# manifestation.append(" I am the star employee at my dream job ")
# manifestation.append(" I am full of joy that my dream job has found me ")
# manifestation.append(" I feel tremendous optimism before during and after working at my dream job ")
# manifestation.append(" I feel peaceful when I realize I have my dream job ")
# manifestation.append(" I feel glad because I have my dream job ")
# manifestation.append(" I feel grateful when I realize I have my dream job ")
# manifestation.append(" I feel grateful because I have my dream job ")
# manifestation.append(" I feel passionate at my dream job ")

"""
manifestation.append(" I associate to why I want my dream job ")
manifestation.append(" I associate to why I desire my dream job ")
manifestation.append(" I visualize myself having my dream job ")
manifestation.append(" I visualize myself doing my dream job ")
manifestation.append(" I vividly see visualize myself having my dream job ")
manifestation.append(" I vividly see  myself doing my dream job ")
manifestation.append(" I envision myself having my dream job ")
manifestation.append(" I clearly see myself having my dream job ")
manifestation.append(" I know I have my dream job ")
manifestation.append(" I release all resistance between me and my dream job ")
manifestation.append(" I believe I have my dream job ")
manifestation.append(" I already have my dream job ")
manifestation.append(" I ask for my dream job ")
manifestation.append(" I act to create my dream job ")
manifestation.append(" I work to create my dream job ")
manifestation.append(" I build my dream job ")
manifestation.append(" I allow my dream job into my life ")
manifestation.append(" I accept my dream job " )
"""
# manifestation.append(" I maintain and deepen the connection when I channel ")
# manifestation.append(" I maintain a strong connection when I channel ")
# manifestation.append(" I deepen the connection when I channel ")
# manifestation.append(" I channel with great focus ")
#"""
#"""
manifestation.append(" I can psychokinetically affect any and all matter ")
manifestation.append(" I psychokinetically affect anything I desire ")
manifestation.append(" I use psychokinesis at will ")
manifestation.append(" I become more telekinetically skilled ")
manifestation.append(" I continue discovering more ways to use psychokinesis ")
manifestation.append(" I nurture and grow my innate psychokinetic skills ")
#"""

desired_outcome = "to " + "come up with an idea for a business that would help my community"
pain_leverage_statements = []
pain_leverage_statements.append(" skipping psychokinesis study and practice ")
pain_leverage_statements.append(" avoiding psychokinesis practice ")
pain_leverage_statements.append(" failing to practice psychokinesis ")

pleasure_leverage_statements = []
pleasure_leverage_statements.append(" I become more skilled at psychokinesis ")
pleasure_leverage_statements.append(" I practice psychokinetically affecting objects ")
pleasure_leverage_statements.append(" I improve all my psychokinesis skills ")
pleasure_leverage_statements.append(" I quickly improve all my psychokinesis skills ")

repeat = True
randomize = True
display_text = False
count = 0
loop = 1000
speaker = textspeaker()
rate = 'vfast'
volumes = [.15, .20, .25, .30]
#volumes = [.30, .35, .40, .45]
destroy_label_after = 300
#rate = 'both'
while count < loop or repeat:
    # Open the file in read mode ('r')
    #file_text = get_file_text(file_path, randomize)
    file_text = get_file_text(multifile, randomize)
    #print(multifile)

    q_list = [s.strip() for s in file_text.split('|')]
    for question in q_list:
        #if the value is numeric, wait that many seconds
        if question.isnumeric():
            time.sleep(int(question))
            print(question)
        else:
            #replace values in outcome-specific scripts
            q = question
            if len(pain_leverage_statements) > 0:
                q = q.replace("#{PAIN_LEVER}", random.choice(pain_leverage_statements))
            if len(pleasure_leverage_statements) > 0:
                q = q.replace("#{PLEASURE_LEVER}", random.choice(pleasure_leverage_statements))
            q = q.replace("#{GOAL}", desired_outcome)
            if len(manifestation) > 0:
                q = q.replace("#{MANIFESTATION}", random.choice(manifestation))
            q = q.replace("  ", " ")
            
            #random volume
            volume = random.choice(volumes)
            #speak the statement,
            #this function randomizes TTS voice and speech rate
            print(q)
            if q != '':
                if display_text:
                    create_disappearing_label(random.choice(pain_leverage_statements+pleasure_leverage_statements+manifestation), destroy_label_after)
                speaker.text_to_speech(q, volume, rate) 

    count += 1
    
'''speaker.silence()'''