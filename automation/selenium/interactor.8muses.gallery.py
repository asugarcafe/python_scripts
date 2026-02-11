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


urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Tab109/Halloween-Whores/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Blacked/Issue-4/Story/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Blacked/Issue-1/Text/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Blacked/Issue-2/Story/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Blacked/Issue-3/Text/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Fantasyland-Deep-Dive/Issue-1/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Fantasyland-Deep-Dive/Issue-2/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Fantasyland-Deep-Dive/Issue-3/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Pandora/Episode-1/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Pandora/Episode-2/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Pandora/Episode-3/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Pandora/Episode-4/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Pandora/Episode-5/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Pandora/Episode-6/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Raunchy-Business/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-0-Prequel/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-1/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-2/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-3/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-4/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-5/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gonzo-Sexy3DComics/Them/Episode-6/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/3DSimon/High-Socks-and-Rollerblades/1')
urls.append('https://comics.8muses.com/comics/picture/IncestBDSM_com-Comics/Nosy-teeny-punished-by-mommy/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gator3D/Closing-Time/Issue-2/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Gator3D/Closing-Time/Issue-1/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Pwishmonger/Teamwork/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Nenet/Tutor-2/1')
urls.append('https://comics.8muses.com/comics/picture/Affect3D-Comics/Nenet/Tutor/1')
urls.append('https://comics.8muses.com/comics/picture/Y3DF-Your3DFantasy_com-Comics/Like-Whores/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/3DZen/Chezara-Street-Whore/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/3DZen/Toys-in-the-Attic/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/3DZen/Ashley-Bus-Stop/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/3DZen/Jessica/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Romirom/Attention-Whore/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Tab109/The-Corporate-Whore/1')
urls.append('https://comics.8muses.com/comics/picture/Melkormancin_com-Comics/Slutty-Misty/1')
urls.append('https://comics.8muses.com/comics/picture/HermitMoth-Comics/Summers-late-night-visit/1')
urls.append('https://comics.8muses.com/comics/picture/HermitMoth-Comics/Summers-Hot-night/1')
urls.append('https://comics.8muses.com/comics/picture/SodomSluts_com-Comics/Galleries/Candi-Does-Summer/1')
urls.append('https://comics.8muses.com/comics/picture/SodomSluts_com-Comics/Galleries/Random-Pictures/1')
urls.append('https://comics.8muses.com/comics/picture/SodomSluts_com-Comics/Galleries/Candi-Wantsmore-in-Electric-Blue/1')
urls.append('https://comics.8muses.com/comics/picture/SodomSluts_com-Comics/Galleries/Candi-Wantsmore-in-High-Heel-Lover/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Aprils-Fools/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Back-to-college/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/City-Life/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/In-bed-of-her-son/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Midlife-crisis/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Mom-a-night-to-remember/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Mom-and-son-home-alone/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Mom-I-need-some-help-in-the-kitchen/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Monday-Routine/Text/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/New-model/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/No-way/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Personal-tutoring/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Some-old-renders/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Spot-the-easter-eggs/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/Strange-noises-on-the-train/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/The-party/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/The-Reunion/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/The-Tenant/Issue-1/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/LBW/The-Tenant/Issue-2/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Ugaromix/LustinVille-Slutty-Saturdays/1')
urls.append('https://comics.8muses.com/comics/picture/IncestIncestIncest_com-Comics/Slutty-Daughter-Caught-by-Daddy/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Smegmarip/The-Club-Slut-Pt_-I/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Tidy_Fox/The-Slut-Mirror/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Tidy_Fox/Pink-Orb-BillMay-3/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Asmodean/Slut-street/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Asmodean/Lady-of-the-Ring/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Asmodean/A-price-to-pay/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Ferocious-Gnat/Eugenes-Escapades/Issue-3-Phys-EdHome-work/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Ferocious-Gnat/Eugenes-Escapades/Issue-1-Detention/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Ferocious-Gnat/Eugenes-Escapades/Issue-2-Study-Group/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/BottomAllTheWay/Adam-The-Bully-Screws-My-Sister/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/BottomAllTheWay/Adam-The-Bully-Screws-My-Mom/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Fightgirl2004/Home-Invasion/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Fightgirl2004/The-Capture-Game/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Bazoongas-Workshop/Colton-and-Maxine/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/UnderTheHood/Stacys-Revenge/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/UnderTheHood/Bellas-Secret/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Psmike/Locker-Room-Story/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Jessica1222/Meanwhile-in-Norway/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/Jessica1222/The-Wedding-Pictures/1')
urls.append('https://comics.8muses.com/comics/picture/Various-Authors/NLT-Media/A-Sunday-Schooling/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Arcanjo_Fel/School-Love/1')
urls.append('https://comics.8muses.com/comics/picture/Daniel40-Comics/School-Gals/1')
urls.append('https://comics.8muses.com/comics/picture/Xide-Comics/Kali-Schools-Out/1')
urls.append('https://comics.8muses.com/comics/picture/Xide-Comics/Chloe-Restroom/1')
urls.append('https://comics.8muses.com/comics/picture/Xide-Comics/Triniti/1')
urls.append('https://comics.8muses.com/comics/picture/Xide-Comics/Chloe-In-her-studio/1')
urls.append('https://comics.8muses.com/comics/picture/Xide-Comics/Chloe-Photoshoot/1')
urls.append('https://comics.8muses.com/comics/picture/Xide-Comics/Nikkita/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/High-School-Pleasure/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Interrogation/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Lucrative-Deal/Issue-3/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Lucrative-Deal/Issue-1/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Lucrative-Deal/Issue-2/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Prisoners-of-Desire/Issue-1/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Prisoners-of-Desire/Issue-2/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Prisoners-of-Desire/Issue-3/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/Prisoners-of-Desire/Issue-4/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/SedesDis/S_I_-Mental-Facility/Text/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/Klon/Old-school/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/AsprinPS/Hard-lesson-in-old-school/1')
urls.append('https://comics.8muses.com/comics/picture/Renderotica-Comics/A_B_Dearheart/School-Girls-Evil-Games/1')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
#urls.append('')
for ur in urls:
    print(ur)
    run_download(ur)