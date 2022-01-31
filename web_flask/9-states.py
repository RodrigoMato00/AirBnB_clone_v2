#!/usr/bin/python3
"""
module script that starts Flask
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Displays an HTML page in a list of all States, states sorted by name
    Displays a HTML page with info about <id>, if it exists
    """
    sstates = storage.all(State)
    if state_id is not None:
        state_id = '{}.{}'.format('State', state_id)
    return render_template('9-states.html', states=sstates, state_id=state_id)


@app.teardown_appcontext
def teardown_close(self):
    """
    method teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
