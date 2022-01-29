#!/usr/bin/python3
"""
start a flask web application
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def function():
    """
    return a string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def function_HBNB():
    """
    return HBNB
    """

    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def function_c(text):
    """
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    tx = text.replace("_", " ")
    return "C {}".format(tx)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def function_python(text="is cool"):
    """
    python/(<text>): display “Python ”,
    followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    tx = text.replace("_", " ")
    return "Python {}".format(tx)


@app.route("/number/<int:n>", strict_slashes=False)
def function_number(n):
    """
    Displays 'n is a number' if n is an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def function_number_template(n):
    """
    /number_template/<n>:
    display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def function_number_odd_or_even(n):
    """
    /number_odd_or_even/<n>: display a
    HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2 == 0:
            even = 'even'
    else:
        even = 'odd'
    return render_template("6-number_odd_or_even.html", n=n, even=even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
