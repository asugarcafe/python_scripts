# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 18:35:47 2025

@author: sucre
"""

import requests
import json
import pandas as pd
import time, datetime
from dateutil import parser

api_key = '9bf866e4bdb4436d8ea5b10d67d25649'
url = f"https://api.ipgeolocation.io/v2/astronomy?apiKey={api_key}&location=Kearns, Utah, %2C%20US&elevation=10"

start_dt = '2025-12-06'
end_dt = '2025-12-13'
lat = '40.65286'
lon = '-112.00462'
url = f"https://api.ipgeolocation.io/v2/astronomy/timeSeries?apiKey={api_key}&dateStart={start_dt}&dateEnd={end_dt}&lat={lat}&long={lon}"
payload = {}
headers = {

}

#response = requests.request("GET", url, headers=headers, data={})

#print(response.text) 

json_file = 'sample.sun.moon.cycle.json'

with open(json_file, 'r') as file:
    data = json.load(file)
    
astronomy = data["astronomy"]

dt = datetime.datetime.now()
for day in astronomy:
    print(day["date"])
    # print(day["moonrise"])
    # print(day["moonset"])
    # print(day["sunrise"])
    # print(day["sunset"])
    
    if day["moonrise"] != '-:-':
        start_moon = parser.parse(day["date"] + ' ' + day["moonrise"])
        print('moonrise:' + str(start_moon))
    if day["moonset"] != '-:-':
        stop_moon = parser.parse(day["date"] + ' ' + day["moonset"])
        print('moonset:' + str(stop_moon))
    
    if day["sunrise"] != '-:-':
        start_sun = parser.parse(day["date"] + ' ' + day["sunrise"])
        print('moonrise:' + str(start_sun))
    if day["sunset"] != '-:-':
        stop_sun = parser.parse(day["date"] + ' ' + day["sunset"])
        print('sunset:' + str(stop_sun))
    
#df = pd.read_json(json_file)











"""
spacer
"""