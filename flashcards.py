from flask import Flask, render_template, abort, jsonify
# from datetime import datetime

from model import db

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template(
        'welcome.html',
        message="Here's a message from the view!!")


@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route("/api/card/")
def api_card_list():
    return jsonify(db)


# @app.route("/date")
# def date():
#    return "This page was served at: " + str(datetime.now())


# counter = 0


# @app.route('/count_views')
# def count_demo():
#    global counter
#    counter += 1
#    return "This page was served " + str(counter) + " times."
