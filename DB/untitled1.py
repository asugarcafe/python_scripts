# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:29:37 2024

@author: BeRoberts
"""
from PIL import Image, ImageDraw, ImageFont

width = 512
height = 512
message = "Hello boss!"
font = ImageFont.truetype("Tahoma.ttf", size=48)

img = Image.new('RGB', (width, height), color='blue')

imgDraw = ImageDraw.Draw(img)

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

imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))

img.save('result.png')
