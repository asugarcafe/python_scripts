# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 13:28:02 2025

@author: sucre
"""
from selenium import webdriver	 

# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

# Creating an instance webdriver
browser = webdriver.Chrome()
browser.get('https://www.google.com')
browser.maximize_window()
time.sleep(2)

#
search_box = browser.find_elements(By.NAME, 'q')
search_box[0].send_keys('Some search here')

gmail_link = browser.find_elements(By.LINK_TEXT, 'Gmail')
gmail_link[0].click()

"""#wait for a download to complete
import time
import os

def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds
"""



"""
# Let's the user see and also load the element 
time.sleep(2)

login = browser.find_elements(By.XPATH, '//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')

# using the click function which is similar to a click in the mouse.
login[0].click()

print("Login in Twitter")

user = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')

# Enter User Name
user[0].send_keys('USER-NAME')

user = browser.find_element(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')

# Reads password from a text file because
# saving the password in a script is just silly.
with open('test.txt', 'r') as myfile: 
	Password = myfile.read().replace('\n', '')
user.send_keys(Password)

LOG = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()
print("Login Successful")
time.sleep(5)

elem = browser.find_element(By.XPATH, "q")
elem.click()
elem.clear()

elem.send_keys("Geeks for geeks ")

# using keys to send special KEYS 
elem.send_keys(Keys.RETURN) 

print("Search Successful")


"""

# closing the browser
browser.close() 





'''



'''