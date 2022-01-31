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
@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """
    Displays an HTML page in a list of all States, states sorted by name
    Displays a HTML page with info about <id>, if it exists
    """
    sstates = storage.all(State)
    if id is not None:
        id = '{}.{}'.format('State', id)
        return render_template('9-states.html', states=sstates, id=id)

    elif id is None:
        return render_template("9-states.html", states=sstates, id=id)


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
