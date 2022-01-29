#!/usr/bin/python3
"""
start a flask web application
"""

from flask import Flask
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
def number_template(n):
    """
    /number_template/<n>:
    display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
