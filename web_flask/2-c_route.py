#!/usr/bin/python3
""" This is a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    formatted = text.replace('_', ' ')
    return "C " + formatted


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
