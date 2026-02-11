# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os, time, random, sys
import pyttsx3
import pyttsx3.voice
import tkinter, win32api, win32con, pywintypes
from tkinter import ttk
sys.path.append(os.path.abspath("h_scripts/func_manifestations.py"))
from func_manifestations import *

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
    zira = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        # for voice in self.voices:
        #     print(voice.name)
        #     print(voice.id)
        
    def silence(self):
        self.engine.stop()
        
    def getRand(self, upper):
        return random.randint(1, upper)
        

    def text_to_speech(self, text, volume = .99, rate='fast', f_only = False):
        flip = 0
        
        uppers = [180,260,200]
        if rate == 'vfast':
            uppers = [255,305,355]
        if rate == 'slow':
            uppers = [110,130,150]
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
        if not f_only:
            self.engine.setProperty('voice', random.choice(self.voices).id)
        else:
            self.engine.setProperty('voice', self.zira)

    
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.startLoop(False)
        self.engine.iterate()
        self.engine.endLoop()
        return 0


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
#file_path.append('r_priming.telepathy.txt')
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
# file_path.append('r_psi.telekinesis.txt')
#file_path.append('sexual.thoughts.txt')


manifestation = []
manifestation.append(" I associate pain and deep displeasure to smoking ")
manifestation.append(" I have fully associated to the pain and deep displeasure caused by smoking ")
manifestation.append(" I associate deep displeasure to smoking ")
manifestation.append(" I associate strong displeasure to smoking ")
manifestation.append(" I associate powerful displeasure to smoking ")
manifestation.append(" I associate deep discomfort to smoking ")
manifestation.append(" I associate strong discomfort to smoking ")
manifestation.append(" I associate powerful discomfort to smoking ")
manifestation.append(" I feel deep displeasure at the idea of smoking ")
manifestation.append(" I feel strong displeasure at the idea of smoking ")
manifestation.append(" I feel powerful displeasure at the idea of smoking ")
manifestation.append(" I feel deep discomfort at the idea of smoking ")
manifestation.append(" I feel strong discomfort at the idea of smoking ")
manifestation.append(" I feel powerful discomfort at the idea of smoking ")
manifestation.append(" I associate pain to smoking ")
manifestation.append(" I dislike the act of smoking ")
manifestation.append(" I think about what I hate about smoking ")
manifestation.append(" I remember what I hate about smoking ")
manifestation.append(" I interrupt the train of thought when I think about smoking ")

# manifestation.append(" I reed peoples emotions easily whenever I want ")
# manifestation.append(" I consciously strengthen and focus my will throughout the day ")

# manifestation.append(" I can raise the energy and vibration of each of my shockras ")
# manifestation.append(" I empower each of my shockras by raising their energy and vibration ")
# manifestation.append(" I can consciously raise the energy and vibration of each of my shockras ")
# manifestation.append(" I have trained myself to raise the energy and vibration of each of my shockras ")
# manifestation.append(" I have trained myself to harness and engage my shockras for spells, blessings, and manifestations ")
file_path.append('r_meditation.manifestation.coaching.txt')

#add_dream_job(manifestation)
#add_chi_capabilities(file_path, manifestation)
#add_orgasm_without_ejaculation(file_path, manifestation)

#manifestation.append(" I have mastered the awareness and use of my chakras ")
#"""

desired_outcome = ""
# desired_outcome = "you strength train every week"
# desired_outcome = "you meditate every morning and every night"
# desired_outcome = "you have trained yourself to astrally pruhject whenever you will"
# desired_outcome = "you have trained yourself to scry and remotely observe while in the waking state"
# desired_outcome = "you train your balance, agility, flexibility, and dexterity every week"
# desired_outcome = "you have mastered the five basic shing yee movements"
# desired_outcome = "you have learned basic astrology"
# desired_outcome = "you have memorized the astrological signs and their natures"

# desired_outcome = "you have memorized the astrological houses and what they represent"
# desired_outcome = "you have memorized the astrological planets and bodies and their natures"
# desired_outcome = "you have memorized the astrological points and notations and their natures"
# desired_outcome = "you have memorized the astrological aspects and how they affect astrological situations"
# desired_outcome = "you have learned natal astrology"
# desired_outcome = "you have learned synastry astrology"
# desired_outcome = "you have learned electional astrology"
# desired_outcome = "you have learned business astrology"
# desired_outcome = "you have learned karmic astrology"
# desired_outcome = "you have learned how to use astrology to analyze a personal situation"
# desired_outcome = "you have learned how to use astrology to analyze decisions"
# desired_outcome = "you have learned basic chemistry"
# desired_outcome = "you have memorized the periodic table and all its elements and their properties"
# desired_outcome = "you have learned how to calculate chemistry formulas"
# desired_outcome = "you have learned chemistry stoichiometry"
# desired_outcome = "you have memorized and learned the laws of thermo dynamics"
# desired_outcome = "you train your oxygen capacity every week"
#desired_outcome = "you start every day with a to do list"
#file_path.append('r_goalviz.txt')

pain_leverage_statements = []
pleasure_leverage_statements = []


multifile = file_path
repeat = True
randomize = True
display_text = False
count = 0
loop = 1
speaker = textspeaker()
rate = 'vfast'
# rate = 'fast'
# rate = 'slow'
volumes = [.15, .20, .25, .30]
#volumes = [.60, .85, .5, .70]
destroy_label_after = 300
female_only = True
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
            if len(desired_outcome) > 0:
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
                speaker.text_to_speech(q, volume, rate, female_only) 

    count += 1
    
'''speaker.silence()'''