# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 21:48:18 2025

@author: sucre
"""
import re
import json
from selenium import webdriver	 

# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

# Creating an instance webdriver
browser = webdriver.Chrome()
browser.get('https://labyrinthos.co/blogs/tarot-card-meanings-list')

# Let's the user see and also load the element 
time.sleep(2)

cards = browser.find_elements(By.CLASS_NAME, 'grid__item')

card_dict = {}

reg = "<a\s+href=(?:\"([^\"]+)\"|'([^']+)').*?>(.*?)</a>"
card_count = 0
for card in cards:
    h3s = card.find_elements(By.TAG_NAME, 'h3')
    if len(h3s) > 0:
        h3 = h3s[0]
        title = h3.get_attribute('innerText')
        title = title.replace(' Meaning', '')
        print(title)
        card_divs = card.find_elements(By.TAG_NAME, 'div')
        if len(card_divs) > 2:
            keywords = card_divs[2]
            p = keywords.find_element(By.TAG_NAME, 'p')
            phtml = p.get_attribute("innerHTML")
            idx_span = phtml.find("</span>") + 7
            idx_a = phtml.find("<a href")
            stripped = phtml[idx_span:idx_a]
            stripped = stripped.replace('<strong>', '')
            stripped = stripped.replace('<strong data-processed="true">', '')
            stripped = stripped.replace('</strong>', '')
            stripped = stripped.strip()

            upsidedown = stripped[stripped.find('Reversed: ')+10:]
            upsidedown = upsidedown.replace('Reversed: ', '')

            upright = stripped[stripped.find('Upright: ')+9:]
            upright = stripped.replace('Upright: ', '')
            upright = upright[0:upright.find(':')-9]
            upright = upright.strip()
            upsidedown = upsidedown.strip()

            card_dict[card_count] = {title : [upright, upsidedown]}
            card_count += 1

with open("tarot_card_meanings_001.json", "w") as fp:
    json.dump(card_dict , fp) 

# # using the click function which is similar to a click in the mouse.
# login[0].click()

# print("Login in Twitter")

# user = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')

# # Enter User Name
# user[0].send_keys('USER-NAME')

# user = browser.find_element(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')

# # Reads password from a text file because
# # saving the password in a script is just silly.
# with open('test.txt', 'r') as myfile: 
# 	Password = myfile.read().replace('\n', '')
# user.send_keys(Password)

# LOG = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
# LOG[0].click()
# print("Login Successful")
# time.sleep(5)

# elem = browser.find_element(By.XPATH, "q")
# elem.click()
# elem.clear()

# elem.send_keys("Geeks for geeks ")

# # using keys to send special KEYS 
# elem.send_keys(Keys.RETURN) 

print("Search Successful")

# closing the browser
browser.close() 
