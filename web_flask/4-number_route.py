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
def display_C(text):
    formatted = text.replace('_', ' ')
    return "C " + formatted


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def display_Python(text="is cool"):
    formatted = text.replace('_', ' ')
    return "Python " + formatted


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
