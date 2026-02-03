# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 14:03:30 2025

@author: sucre
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#import urllib
import requests
import time
import shutil
import glob, os

#global vars
#url = 'https://comics.8muses.com/comics/picture/Various-Authors/NLT-Media/Aunt-Debs-Show/1'
#url = 'https://comics.8muses.com/comics/picture/Tufos-Comics/Gallery/I-Was-Blackmailed-By-A-Hacker/1'
working_folder = 'C:/temp/zipper/'
output_zip_folder = 'C:/temp/zipped/'
xpath_dd_list = '//*[@id="left-menu"]/ol/li[3]/div/a[2]/ul'
xpath_dd_list_li = '//*[@id="left-menu"]/ol/li[3]/div/a[2]/ul/li'

def run_download(url):
    #open the browser
    b = webdriver.Chrome()
    b.get(url)
    time.sleep(2)
    
    #local vars
    xpath_image = '//*[@id="content"]/div/div[1]/a/img'
    xpath_prev = '//*[@id="left-menu"]/ol/li[3]/div/a[1]'
    xpath_next = '//*[@id="left-menu"]/ol/li[3]/div/a[3]'
    xpath_page_list = '//*[@id="left-menu"]/ol/li[3]/div/a[2]/ul/li[1]' #'//*[@id="left-menu"]/ol/li[3]/div/a[2]'
    
    #get the count of images
    prev_btn = b.find_element(By.XPATH, xpath_prev)
    prev_img = prev_btn.get_attribute("href")
    last_img = int(prev_img[prev_img.rfind('/')+1:])
    
    for page in range(1, last_img + 1):
        #get the image and download it
        
        #find the image
        main_image = b.find_element(By.XPATH, xpath_image)
        dl_url = main_image.get_attribute("src")
            
        #get the image extension
        extension = '.jpg'
        extension = dl_url[dl_url.rfind('.'):]
        
        #do the download
        img_data = requests.get(dl_url).content
        image_name_and_path = working_folder + str(page) + extension
        with open(image_name_and_path, 'wb') as handler:
            handler.write(img_data)
            handler.close()
        
        #click next
        next_btn = b.find_element(By.XPATH, xpath_next)
        next_btn.click()
        time.sleep(2)
    
    #create the output file name from the url
    url_seg = url.split('/')
    cat = url_seg[len(url_seg)-4]
    if cat == 'picture':
        cat = "gallery"
    auth = url_seg[len(url_seg)-3]
    gallery = url_seg[len(url_seg)-2]
    output_filename = f'{cat} - {auth} - {gallery}'
    print(output_filename)
    
    #zip the files
    o_file = output_zip_folder + output_filename + '.zip'
    if os.path.exists(o_file):
        os.remove(o_file)
    shutil.make_archive(output_zip_folder + output_filename, 'zip',base_dir=working_folder)
    
    #delete the non-zip files
    gl = glob.glob(working_folder + '*')
    for i in gl:
        os.remove(i)
    
    b.close()
    b.quit()
    
    
"""
bottom of page spacer
"""
#ur = 'https://comics.8muses.com/comics/picture/Alison-Hale-Comics/Team-Players/Issue-1/1'

urls = []


#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
for ur in urls:
    print(ur)
    run_download(ur)