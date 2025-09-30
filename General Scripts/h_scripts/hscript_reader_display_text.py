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
font_colors = ["red", "blue", "blue4",
               "brown4","burlywood4",
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
#file_path.append('r_memory.txt')
#file_path.append('r_goal.questions.txt')
#file_path.append('r_metaphysical.chakras.txt')
#file_path.append('r_manifestation.healing.txt')
#file_path.append('r_single.line.repeater.txt')
file_path.append('r_meditation.manifestation.coaching.txt')
multifile = file_path


desired_outcome = "to " + "come up with an idea for a business that would help my community"
manifestation = []
# manifestation.append(" I receive thirteen thousand dollars every month ")
# manifestation.append(" you have trained your shockras to get lighter and lighter until they can be lighter than air ")
# manifestation.append(" you explore more and more of the capabilities of your shockras ")
# manifestation.append(" you think about your living spaces in a way that allows you to keep them clean and natually organize them ")
# manifestation.append(" you have paid off your mortgage and own your home ")
# manifestation.append(" you explore and learn how to use the chee energy flowing through your body ")
# manifestation.append(" I have mastered my chee energy and use it like a master of sheenanjoo ")
# manifestation.append(" I control and direct my chee energy ")
# manifestation.append(" you have trained yourself to quickly and easily see and sense auras ")
# manifestation.append(" you take good care of the things you own and are responsible for maintaining ")
# manifestation.append(" you appreciate people and build stronger and healthier bonds with the people you connect with ")
# manifestation.append(" you learn and play music every day ")
# manifestation.append(" I reed peoples emotions easily whenever I want ")

manifestation.append(" I increase my strength, endurance, and dexterity every day ")
manifestation.append(" I increase my strength, dexterity, and endurance every day ")
manifestation.append(" I increase my endurance, strength, and dexterity every day ")
manifestation.append(" I increase my endurance, dexterity, and strength every day ")
manifestation.append(" I increase my dexterity, endurance, and strength every day ")
manifestation.append(" I increase my dexterity, strength, and endurance every day ")
manifestation.append(" I rest and heal in ways that increase my strength, endurance, and dexterity every day ")
manifestation.append(" I rest and heal in ways that increase my strength, dexterity, and endurance every day ")
manifestation.append(" I rest and heal in ways that increase my endurance, strength, and dexterity every day ")
manifestation.append(" I rest and heal in ways that increase my endurance, dexterity, and strength every day ")
manifestation.append(" I rest and heal in ways that increase my dexterity, endurance, and strength every day ")
manifestation.append(" I rest and heal in ways that increase my dexterity, strength, and endurance every day ")

#manifestation = " you are especially competent and detail oriented at work "

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
            q = question.replace("#{GOAL}", desired_outcome)
            q = question.replace("#{MANIFESTATION}", random.choice(manifestation))
            #random volume
            volume = random.choice(volumes)
            #speak the statement,
            #this function randomizes TTS voice and speech rate
            print(q)
            if q != '':
                if display_text:
                    create_disappearing_label(random.choice(manifestation), destroy_label_after)
                speaker.text_to_speech(q, volume, rate) 

    count += 1
    
'''speaker.silence()'''