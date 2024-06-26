#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_html():
    """ renders states created """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def handle_teardown(self):
    """  Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
