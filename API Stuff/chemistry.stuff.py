# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:10:28 2023

@author: sucre
"""
import requests

def fetch_periodic_table_data():
    url = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
    response = requests.get(url)
    data = response.json()
    return data

periodic_table_data = fetch_periodic_table_data()

# Accessing the data for specific elements
hydrogen = periodic_table_data["elements"][0]
helium = periodic_table_data["elements"][1]
carbon = periodic_table_data["elements"][5]

# Example usage
# print(hydrogen) 
# print(helium)
print(carbon)
