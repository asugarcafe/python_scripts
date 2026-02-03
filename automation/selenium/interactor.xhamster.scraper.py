# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 09:26:17 2025

@author: sucre
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
import time
import shutil
import glob, os

faves_url = 'https://xhamster.com/my/favorites/videos/59c32daf8b9753087f268308-default-playlist'