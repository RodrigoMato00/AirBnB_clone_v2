#!/usr/bin/python3
"""
module script that starts Flask
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    """
    display a HTML page
    list of all states and related cities
    """
    storage_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=storage_states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities(id):
    """
    display a HTML page
    list of all states and related cities
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """
    Displays the filters in HTML page
    """
    states = storage.all(State)
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
