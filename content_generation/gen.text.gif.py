# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

'''
images = []

width = 200
height = 200
center_w = width // 2
center_h = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center_w * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center_w - i, center_w - i, center_w + i, center_w + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center_w - i, center_w - i, center_w + i, center_w + i), fill=color_1)
    images.append(im)

images[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
'''

from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))

draw = ImageDraw.Draw(img)
draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

img.save('test.gif', 'GIF', transparency=0)