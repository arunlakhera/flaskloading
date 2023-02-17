#!/usr/bin/python
from flask import Flask, render_template, request
import time
import urllib.parse
from flask import Flask, render_template

app = Flask(__name__)
my_msg = "Wow this worked"


@app.route('/')
def loading():
    return render_template("loading.html")


@app.route('/map')
def show_map():
    return render_template("success.html")


@app.route('/create_map')
def create_map():
    time.sleep(5)
    return "Map created"


if __name__ == '__main__':
    app.run()