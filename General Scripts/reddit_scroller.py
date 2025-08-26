# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 20:18:55 2025

@author: sucre
"""
import pyautogui
import pydirectinput
import time, datetime
import win32gui, win32com.client
import re
import winsound
import random
t = True
f = False

pyautogui.PAUSE = 1
window_name = 'Reddit - ' #partial name of window title
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 250  # Set Duration To 1000 ms == 1 second

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        #win32gui.SetForegroundWindow(self._handle)
        
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._handle)

#chim = pyautogui.getWindowsWithTitle(window_name)[0]

def refresh_window():
    w = WindowMgr()
    w.find_window_wildcard(".*" + window_name + ".*")
    w.set_foreground()
    time.sleep(1)

def scrollDown(times = 1):
    right = 950
    down = 1028
    pydirectinput.click(x=right, y=down)
    pydirectinput.click(x=right, y=down)
    if times > 1:
        for x in range(0,times):
            time.sleep(random.randint( 0, 2))
            pydirectinput.click(x=right, y=down)

# def click_coordinates(key, xoffset=0, yoffset=0):
#     s1 = b[key]
#     pydirectinput.doubleClick(s1[0]+ xoffset, s1[1]+yoffset)

# def click_multiple_coordinates(coords):
#     for x in coords:
#         click_coordinates(x)
#         time.sleep(1)


def random_rightclick():
    right = 48
    down = random.randint(180, 1022)
    #pydirectinput.rightClick(x=right, y=down)
    pydirectinput.click(x=right, y=down)
    time.sleep(random.randint( 5, 30))
    scrollDown(random.randint( 1, 3))
    pydirectinput.click(x=16, y=51)

refresh_window()

time.sleep(5)

loop = 5
for x in range(0,loop):
    time.sleep(random.randint( 5, 25))
    scrollDown(random.randint( 1, 3))
    random_rightclick()



