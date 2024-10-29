# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:01:23 2024

@author: Lab
"""
from datetime import datetime
from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    now=datetime.now()
    return render_template("index.html")


app.run(debug=True)