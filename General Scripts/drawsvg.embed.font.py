# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:08:30 2025

@author: sucre
"""
import drawsvg as draw

d = draw.Drawing(400, 100, origin='center')
d.embed_google_font('Permanent Marker', text=set('Text with custom font'))

d.append(draw.Text('Text with custom font', 35, 0, 0, center=True,
                   font_family='Permanent Marker', font_style='italic'))

d.save_svg('font.svg')
d  # Custom fonts work in most browsers but not in rasterize(), save_png(), or save_video()