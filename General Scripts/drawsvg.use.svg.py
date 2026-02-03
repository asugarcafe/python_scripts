# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:06:35 2025

@author: sucre
"""
import drawsvg as draw

# Subclass DrawingBasicElement if it cannot have child nodes
# Subclass DrawingParentElement otherwise
# Subclass DrawingDef if it must go between <def></def> tags in an SVG
class Hyperlink(draw.DrawingParentElement):
    TAG_NAME = 'a'
    def __init__(self, href, target=None, **kwargs):
        # Other init logic...
        # Keyword arguments to super().__init__() correspond to SVG node
        # arguments: stroke_width=5 -> <a stroke-width="5" ...>...</a>
        super().__init__(href=href, target=target, **kwargs)

d = draw.Drawing(1, 1.2, origin='center')

# Create hyperlink
hlink = Hyperlink('https://www.python.org', target='_blank',
                  transform='skewY(-30)')
# Add child elements
hlink.append(draw.Circle(0, 0, 0.5, fill='green'))
hlink.append(draw.Text('Hyperlink', 0.2, 0, 0, center=0.6, fill='white'))

# Draw and display
d.append(hlink)
d.set_render_size(200)