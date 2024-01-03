# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:45:56 2023

@author: sucre

This needs to be run as an admin

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
window_name = 'glorp' #partial name of window title
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
        print(str(win32gui.GetWindowText(hwnd)))
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        print(wildcard)
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

'''
pydirectinput.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
pydirectinput.click() # Click the mouse at its current location.
pydirectinput.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
pydirectinput.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
pydirectinput.doubleClick() # Double click the mouse at the
pydirectinput.press('esc') # Simulate pressing the Escape key.
pydirectinput.keyDown('shift')
pydirectinput.keyUp('shift')
'''


refresh_window()

