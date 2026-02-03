# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:05:04 2025

@author: sucre
"""
import drawsvg as draw

d = draw.Drawing(1.5, 0.8, origin='center')

# Background pattern (not supported by Cairo, d.rasterize() will not show it)
pattern = draw.Pattern(width=0.13, height=0.23)
pattern.append(draw.Rectangle(0, 0, .1, .1, fill='yellow'))
pattern.append(draw.Rectangle(0, .1, .1, .1, fill='orange'))
d.draw(draw.Rectangle(-0.75, -0.5, 1.5, 1, fill=pattern, fill_opacity=0.4))

# Create gradient
gradient = draw.RadialGradient(0, 0.35, 0.7*10)
gradient.add_stop(0.5/0.7/10, 'green', 1)
gradient.add_stop(1/10, 'red', 0)

# Draw a shape to fill with the gradient
p = draw.Path(fill=gradient, stroke='black', stroke_width=0.002)
p.arc(0, 0.35, 0.7, -30, -120, cw=False)
p.arc(0, 0.35, 0.5, -120, -30, cw=True, include_l=True)
p.Z()
d.append(p)

# Draw another shape to fill with the same gradient
p = draw.Path(fill=gradient, stroke='red', stroke_width=0.002)
p.arc(0, 0.35, 0.75, -130, -160, cw=False)
p.arc(0, 0.35, 0, -160, -130, cw=True, include_l=True)
p.Z()
d.append(p)

# Another gradient
gradient2 = draw.LinearGradient(0.1, 0.35, 0.1+0.6, 0.35+0.2)
gradient2.add_stop(0, 'green', 1)
gradient2.add_stop(1, 'red', 0)
d.append(draw.Rectangle(0.1, 0.15, 0.6, 0.2,
                        stroke='black', stroke_width=0.002,
                        fill=gradient2))

# Display
d.set_render_size(w=600)
d