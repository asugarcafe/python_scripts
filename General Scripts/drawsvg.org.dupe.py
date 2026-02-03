# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:06:10 2025

@author: sucre
"""
import drawsvg as draw

d = draw.Drawing(300, 100)
d.set_pixel_scale(2)

# Use groups to contain other elements
# Children elements of groups inherit the coordinate system (transform)
# and attribute values
group = draw.Group(fill='orange', transform='rotate(-20)')
group.append(draw.Rectangle(0, 10, 20, 40))  # This rectangle will be orange
group.append(draw.Circle(30, 40, 10))  # This circle will also be orange
group.append(draw.Circle(50, 40, 10, fill='green'))  # This circle will not
d.append(group)

# Use the Use element to make duplicates of elements
# Each duplicate can be placed at an offset (x, y) location and any additional
# attributes (like fill color) are inherited if the element didn't specify them.
d.append(draw.Use(group, 80, 0, stroke='black', stroke_width=1))
d.append(draw.Use(group, 80, 20, stroke='blue', stroke_width=2))
d.append(draw.Use(group, 80, 40, stroke='red', stroke_width=3))

d.display_inline()