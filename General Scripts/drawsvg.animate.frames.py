# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:07:57 2025

@author: sucre
"""
import drawsvg as draw

# Draw a frame of the animation
def draw_frame(t):
    d = draw.Drawing(2, 6.05, origin=(-1, -5))
    d.set_render_size(h=300)
    d.append(draw.Rectangle(-2, -6, 4, 8, fill='white'))
    d.append(draw.Rectangle(-1, 1, 2, 0.05, fill='brown'))
    t = (t + 1) % 2 - 1
    y = t**2 * 4 - 4
    d.append(draw.Circle(0, y, 1, fill='lime'))
    return d

with draw.frame_animate_jupyter(draw_frame, delay=0.05) as anim:
# Or:
#with draw.frame_animate_video('example6.gif', draw_frame, duration=0.05) as anim:
# Or:
#with draw.frame_animate_spritesheet('example6.png', draw_frame, row_length=10) as anim:
    # Add each frame to the animation
    for i in range(20):
        anim.draw_frame(i/10)
    for i in range(20):
        anim.draw_frame(i/10)
    for i in range(20):
        anim.draw_frame(i/10)