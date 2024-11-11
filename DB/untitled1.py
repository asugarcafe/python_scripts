# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:29:37 2024

@author: BeRoberts
"""
from PIL import Image, ImageDraw, ImageFont

width = 200
height = 200
message = ''
output_path = 'C:/temp/data/svg/'

messages = ['ADMIN', 'Alta', 'ARCH', 'BCR',
'CCL', 'CUST','DBK','DRA',
'FAC','GRA','HER','HOL',
'HUN','IT','KEA','MAG',
'MCC','METRO','OXBO','RIV',
'SAN','SJO','SLCLS','SLCOS',
'SLC ARC','SMC','SMI','TAY',
'TRA','TSV','TYL','VEC',
'VIR','web','WHI','WJO','WVA']

purple = (155, 79, 150)
blue = (0,56,168)
pink = (214, 2, 112)

font = ImageFont.truetype("SHOWG.TTF", size=48)

for message in messages:

    #img = Image.new('RGB', (width, height), color='blue')
    img = Image.new('RGB',(width, height), purple)
    
    
    imgDraw = ImageDraw.Draw(img)
    
    imgDraw.rectangle([(5, 5), (195, 195)],fill=blue )
    
    #textWidth, textHeight
    #textwidth  = imgDraw.textlength(message, font=font)
    
    textWidth = font.getlength(message)
    x,y,wid,hei = font.getbbox(message)
    
    # print(x)
    # print(y)
    # print(hei)
    # print(wid)
    
    xText = (width - wid) / 2
    yText = (height - hei) / 2
    
    imgDraw.text((xText, yText), message, font=font, fill=pink)
    
    img.save(output_path + message + '.png')
