# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 10:41:48 2025

@author: sucre
"""
import tkinter, win32api, win32con, pywintypes
import time, random

fonts = ["Aharoni","Arial",
         "Bahnschrift","Calibri",
         "Comic Sans MS","Corbel",
         "David","Georgia",
         "Segoe UI","Tahoma",]
sizes = [24,72]
font_colors = ["red", "blue", "blue4",
               "brown4","burlywood4",
               "cadetblue4","cadmiumorange",
               "green", "aquamarine4",
               "darkolivegreen4", "darkgreen",
               "black", "bisque4"]

def get_random_font_color():
    return random.choice(font_colors)

def quit_label(lbl):
    lbl.master.destroy()
    lbl.quit()

def create_disappearing_label(caption, dur_ms):
    label = tkinter.Label(text=caption, 
                          wraplength=1200,
                          font=get_random_font(), 
                          fg=get_random_font_color(), 
                          bg='white')
    label.master.overrideredirect(True)
    label.master.geometry(get_random_position())
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")
    
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
    top = random.randrange(1,700)
    left = random.randrange(1,500)
    return "+{0}+{1}".format(left,top)
    


create_disappearing_label("I increase my strength, endurance, and dexterity every day, and I tell myself often that I increase my strength, endurance, and dexterity every day", 500)