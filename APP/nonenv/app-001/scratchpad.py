# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:36:01 2025

@author: BeRoberts
"""

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"