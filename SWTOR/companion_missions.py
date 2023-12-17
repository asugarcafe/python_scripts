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
window_name = ' The Old Republic' #partial name of window title
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

b = {
    "Dip1":[220,232],
    "Dip2":[220,320],
    "Dip3":[220,410],
    "Dip4":[220,500],
    "dd":[772,64],
    "dd1":[772,86],
    "dd2":[772,106],
    "dd3":[772,124],
    "dd4":[772,142],
    "dd5":[772,152],
    "dd6":[772,176],
    "dd7":[772,197],
    "dd8":[772,214],
    "dd9":[772,234],
    "dd10":[772,252],
    "dd11":[772,266],
    "Return":[300,1045],    
    "ReturnFail":[300,1014],    
    "SendComp":[847,647],
    "TopDip":[658,142],
    "ScrollCharTop":[433,182],
    "ScrollCharBottom":[433,568],
    "Scroll1":[435,228],
    "Scroll2":[435,223],
    "SysMenu":[1015,20],
    "ContentMenu":[900,15],
    "CrewSkills":[970,205],
    "MissionScrollBottom":[895,493],
    "SysLogout":[1015,175],
    "ConfirmLogout":[910,575],
    "BottomChar":[1520,555],
    "CraftButton":[1280,655],
    }

lev_time = {
    "1": 68,
    "2": 94,
    "3": 140,
    "4": 180,
    "5": 207,
    "6": 256,
    "7": 293,
    "8": 360,
    "9": 414,
    "10": 460,
    "11": 805,
    }

lev_tim2influence = {
     "1":[67, 28],
     "2":[103, 36],
     "3":[139, 46],
     "4":[180, 58],
     "5":[207, 72],
     "6":[256, 91],
     "7":[292, 112],
     "8":[360, 135],
     "9":[414, 166],
     "10":[459, 203],
     "11":[805, 280],
     }

def sendTopFourGathering(level = 2, DoMiddleSkill=False, OffsetFromBottom=0):
    dips = ["Dip1","Dip2","Dip3","Dip4"]
    for dip in dips:
        acceptReward()
        b1 = b[dip]
        offset = 0
        if DoMiddleSkill:
            offset = - 50
        click_coordinates(dip, xoffset=offset, yoffset=OffsetFromBottom)
        selectLevel(level)
        click_coordinates("TopDip", xoffset=offset, yoffset=OffsetFromBottom)
        time.sleep(.5)

def openCrewSkills():    
    click_multiple_coordinates(["ContentMenu", "CrewSkills"])

def acceptReward():
    click_multiple_coordinates(["Return", "ReturnFail"])
    
def logOut():
    click_multiple_coordinates(["SysMenu", "SysLogout", "ConfirmLogout"])

def logInBottom():    
    logins = ["BottomChar", "BottomChar"]
    click_multiple_coordinates(logins)
    
def logoutAndSwtichCharacters():
    logOut()
    time.sleep(45)
    logInBottom()
    time.sleep(45)

def selectLevel(level):
    dd = b["dd"]
    td = b["dd" + str(level)]
    click_coordinates("dd")
    time.sleep(.5)
    click_coordinates("dd" + str(level))
    time.sleep(.5)

def scroll_top():
    click_coordinates("ScrollCharTop")

def scroll_bottom():
    click_coordinates("ScrollCharBottom")

def mission_scroll_bottom():
    click_coordinates("MissionScrollBottom")

def click_down_four():
    click_multiple_coordinates(["Scroll1", "Scroll2"])

def click_coordinates(key, xoffset=0, yoffset=0):
    s1 = b[key]
    pydirectinput.doubleClick(s1[0]+ xoffset, s1[1]+yoffset)

def click_multiple_coordinates(coords):
    for x in coords:
        click_coordinates(x)
        time.sleep(1)

def run_missions(mission_levels, minutes_to_run, pad_time_multiplier = 1, 
                 fullRun = False, runMiddleMissions = False, levelMode=False):
    use_pad = (pad_time_multiplier != 1)
    for x in mission_levels:
        print('level ' + str(x) + ' ' + str(datetime.datetime.now()))
        
        timeout = time.time() + (60 * minutes_to_run)   
        while True:
            test = 0

            if fullRun:
                scroll_top()

            sendTopFourGathering(x, runMiddleMissions)

            if fullRun:
                scroll_bottom()
                #click_down_four()
                sendTopFourGathering(x, runMiddleMissions)

            print('companions away!')

            if levelMode:
                time.sleep(30)
            elif use_pad:
                time.sleep(lev_time[str(x)] * pad_time_multiplier)
            else:
                time.sleep(lev_time[str(x)])

            for y in range(1,10):
                time.sleep(.5)
                acceptReward()
        
            if test == 5 or time.time() > timeout:
                break
            test = test - 1
            print('level ' + str(x) + ' missions run: ' + str(datetime.datetime.now()))
        #winsound.Beep(frequency, duration)
    winsound.Beep(frequency, 750)
    print('execution complete')

def run_tops_and_bottoms(level, DoMiddleSkill=f):
    refresh_window()
    scroll_top()
    time.sleep(1)
    sendTopFourGathering(level,DoMiddleSkill)
    time.sleep(1)
    scroll_bottom()
    time.sleep(1)
    sendTopFourGathering(level,DoMiddleSkill,OffsetFromBottom=15)


def runAll(levels_to_grind, DoMiddleSkill=False):
    levels = []
    for l in levels_to_grind:
        for x in range(0,6):
            levels.append(l)

    while True:
        for x in levels:
            print('Running loop')
            refresh_window()
            print('acceptReward()')
            for y in range(1,8):
                time.sleep(.5)
                acceptReward()
            print('openCrewSkills()')
            time.sleep(1)
            openCrewSkills()
            time.sleep(1)
            print('run_tops_and_bottoms(' + str(x)+','+str(DoMiddleSkill)+')')
            time.sleep(1)
            # refresh_window()
            # if RunBottoms:
            #     print('scroll_bottom()')
            #     scroll_bottom()
            # sendTopFourGathering(x,DoMiddleSkill)
            run_tops_and_bottoms(x, DoMiddleSkill)
            time.sleep(.5)
            print('logoutAndSwtichCharacters()')
            time.sleep(60)
            logoutAndSwtichCharacters()
            time.sleep(60)
            print('time.sleep(40)')
            time.sleep(40)
            time.sleep(.5)
            print('End loop')
            print(str(datetime.datetime.now()))
    

refresh_window()


runAll([1,2,3,5,6,7,8,9,10], f)

#run_tops_and_bottoms(5, f)

#run_missions([2,3,4,5,6,7], 180, fullRun=f, runMiddleMissions=f)#, levelMode=t)
# t = b["ScrollCharTop"]
# pydirectinput.click(t[0],t[1] + 5)
# pyautogui.scroll(-10)


#click_down_four()
# level = 7
# DoMiddleSkill=False
# levels = [3]
# both = [t,f]
# while True:    
#     refresh_window()
#     time.sleep(1)
#     run_tops_and_bottoms(random.choice(levels),random.choice(both))
#     time.sleep(120)
#     print(str(datetime.datetime.now()))
# scroll_bottom()
# time.sleep(1)
#sendTopFourGathering(5,f)

#time.sleep(2)
