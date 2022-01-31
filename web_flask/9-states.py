#!/usr/bin/python3
"""
module script that starts Flask
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays an HTML page in a list of all States, states sorted by name
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)



@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with info about
    <id>, if it exists
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
