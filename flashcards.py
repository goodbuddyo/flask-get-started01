from flask import Flask, render_template, abort, jsonify

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template(
        'welcome.html',
        message="Here's a message from the view")


@app.route("/date")
def date():
    return "This page was served at: " + str(datetime.now())


counter = 0


@app.route('/count_views')
def count_demo():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times."
