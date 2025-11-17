# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os, time, random
import pyttsx3
import pyttsx3.voice
import tkinter, win32api, win32con, pywintypes

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
        if rate == 'vslow':
            uppers = [40,80,60]
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


The stages:
-----------------------------------------------------

Mental Movement to Target:
Mental prep to RV, engaging with a target ID
tts_scripts/r_rv.prompts.movement.to.target.txt

Major Gestalt:
"Land surrounded by water, an island"
tts_scripts/r_rv.prompts.major.gestalt.txt

Sensory Contact:
"Cold sensation, wind-swept feeling"
tts_scripts/r_rv.prompts.sensory.contact.txt

Dimension, Motion, Mobility:
"Rising up, panoramic view, island outline"
tts_scripts/r_rv.prompts.dimension.motion.mobility.txt

General qualitative analytical aspects:
"Scientific research, live organisms"
tts_scripts/r_rv.prompts.general.qualitative.aspects.txt

Specific qualitative analytical aspects:
"Biological warfare (BW) preparation site"
tts_scripts/r_rv.prompts.specific.qualitative.aspects.txt

Three-dimensional contact,modeling:
Layouts, details, further analytical contact
tts_scripts/r_rv.prompts.modeling.txt
'''


file_path = []  
#file_path.append("r_single.line.repeater.txt")
file_path.append('tts_scripts/r_priming.psi.txt')
# file_path.append('r_meditation.manifestation.coaching.txt')
# file_path.append('dickens_leverage_pain.txt')
# file_path.append('dickens_leverage_pleasure.txt')
multifile = file_path


manifestation = []
# manifestation.append(" I feel passionate at my dream job ")


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
while count < loop or repeat:
    # Open the file in read mode ('r')
    file_text = get_file_text(multifile, randomize)

    q_list = [s.strip() for s in file_text.split('|')]
    for question in q_list:
        #if the value is numeric, wait that many seconds
        if question.isnumeric():
            time.sleep(int(question))
            print(question)
        else:
            #replace values in outcome-specific scripts
            q = question
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
                    create_disappearing_label(random.choice(q), destroy_label_after)
                speaker.text_to_speech(q, volume, rate) 

    count += 1
    



'''
'''