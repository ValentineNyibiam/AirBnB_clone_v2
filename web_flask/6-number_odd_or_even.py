#!/usr/bin/python3
""" This is a script that starts a Flask web application """
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_even(n):
    if n%2 == 0:
        ret = f"{n} is even"
    else:
        ret = f"{n} is odd"
    return render_template("6-number_odd_or_even.html", output=ret)



if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
