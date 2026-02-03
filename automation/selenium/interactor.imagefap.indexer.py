# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 09:35:20 2025

@author: sucre
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
import time
import shutil
import glob, os

keyword = 'spank'
search_base = f'https://www.imagefap.com/gallery.php?search={keyword}&submit=Search%21'