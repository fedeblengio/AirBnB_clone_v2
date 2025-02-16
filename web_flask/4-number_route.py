#!/usr/bin/python3
"""Task-4"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """bnbn"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def replaceTexT(text):
    """text"""
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def replaceTexT_2(text='is cool'):
    """text2"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Number"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
