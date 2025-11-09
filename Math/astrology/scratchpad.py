# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 13:29:07 2025

@author: sucre
"""
from kerykeion import AstrologicalSubjectFactory
from kerykeion.chart_data_factory import ChartDataFactory
from kerykeion.charts.chart_drawer import ChartDrawer

# Step 1: Create subject
john = AstrologicalSubjectFactory.from_birth_data("John Lennon", 1940, 10, 9, 18, 30, "Liverpool", "GB")
ben = AstrologicalSubjectFactory.from_birth_data("Ben Roberts", 1973, 8, 27, 20, 20, "Ogden, UT", "USA")

# Step 2: Pre-compute chart data
chart_data = ChartDataFactory.create_natal_chart_data(ben)

# Step 3: Create visualization
birth_chart_svg = ChartDrawer(chart_data=chart_data)
birth_chart_svg.save_svg()