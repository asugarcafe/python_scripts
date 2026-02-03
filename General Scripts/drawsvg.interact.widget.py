# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 20:07:27 2025

@author: sucre
"""
import drawsvg as draw
from drawsvg.widgets import DrawingWidget
import hyperbolic.poincare as hyper  # python3 -m pip install hyperbolic
from hyperbolic import euclid

# Create drawing
d = draw.Drawing(2, 2, origin='center', context=draw.Context(invert_y=True))
d.set_render_size(500)
d.append(draw.Circle(0, 0, 1, fill='orange'))
group = draw.Group()
d.append(group)

# Update the drawing based on user input
click_list = []
def redraw(points):
    group.children.clear()
    for x1, y1 in points:
        for x2, y2 in points:
            if (x1, y1) == (x2, y2): continue
            p1 = hyper.Point.from_euclid(x1, y1)
            p2 = hyper.Point.from_euclid(x2, y2)
            if p1.distance_to(p2) <= 2:
                line = hyper.Line.from_points(*p1, *p2, segment=True)
                group.draw(line, hwidth=0.2, fill='white')
    for x, y in points:
        p = hyper.Point.from_euclid(x, y)
        group.draw(hyper.Circle.from_center_radius(p, 0.1),
                   fill='green')
redraw(click_list)

# Create interactive widget and register mouse events
widget = DrawingWidget(d)
@widget.mousedown
def mousedown(widget, x, y, info):
    if (x**2 + y**2) ** 0.5 + 1e-5 < 1:
        click_list.append((x, y))
    redraw(click_list)
    widget.refresh()
@widget.mousemove
def mousemove(widget, x, y, info):
    if (x**2 + y**2) ** 0.5 + 1e-5 < 1:
        redraw(click_list + [(x, y)])
    widget.refresh()
widget