#!/usr/bin/python3
"""scripty"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """comment"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """comment"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """sea"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """poithin"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """numpy"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n=None):
    """numby"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
