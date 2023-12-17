# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:29:34 2020

@author: sucre
"""

import requests
import pyttsx3
import time
import xmltodict

class Newscasters:
    engine = None
    voice = 0
    voices = ['HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0',
              'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0']

    def __init__(self):
        self.voice = 0
        self.engine = self.init_engine()
    
    def init_engine(self):
        # One time initialization
        engine = pyttsx3.init()
        
        # Set properties _before_ you add things to say
        engine.setProperty('rate', 150)    # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1
        return engine
        
    def get_voice(self):
        if self.voice == 0:
            self.voice = 1
            return self.voices[self.voice]
        else:
            self.voice = 0
            return self.voices[self.voice]
    
    def report(self, txt):
        self.engine.setProperty('voice', self.get_voice())  # 
        self.engine.say(txt)
        self.engine.runAndWait()


feeds = {'CNN US News': 'http://rss.cnn.com/rss/cnn_us.rss',
         'CNN Top Stories' : 'http://rss.cnn.com/rss/cnn_topstories.rss',
         'Google US News' : 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en',
         'Reuters VIA Google' : 'https://news.google.com/rss/search?q=when:24h+allinurl:reuters.com&ceid=US:en&hl=en-US&gl=US',}

newscasters = Newscasters()

for feed in feeds:
    newscasters.say(feed)
    time.sleep(2)

    response = requests.get(feeds[feed])
    data = xmltodict.parse(response.content)
    
    seed = 0
    for datum in data['rss']['channel']['item']:
        title = datum['title']
        print(title)
        newscasters.report(title)
        time.sleep(4)
        seed = seed +1
        if seed > 5:
            break
    

