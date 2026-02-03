# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:05:34 2025

@author: sucre
"""
import drawsvg as draw

d = draw.Drawing(1.4, 1.4, origin='center')

# Define clip path
clip = draw.ClipPath()
clip.append(draw.Rectangle(-.25, -.25, 1, 1))

# Draw a cropped circle
circle = draw.Circle(0, 0, 0.5,
        stroke_width='0.01', stroke='black',
        fill_opacity=0.3, clip_path=clip)
d.append(circle)

# Make a transparent copy, cropped again
g = draw.Group(opacity=0.5, clip_path=clip)
# Here, circle is not directly appended to the drawing.
# drawsvg recognizes that `Use` references `circle` and automatically adds
# `circle` to the <defs></defs> section of the SVG.
g.append(draw.Use(circle, 0.25, -0.1))
d.append(g)

# Display
d.set_render_size(400)
#d.rasterize()  # Display as PNG
d  # Display as SVG