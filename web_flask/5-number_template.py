#!/usr/bin/python3
"""Start a Flask web application and return simple string."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnh():
    return "HBNB"


@app.route("/c/<word>", strict_slashes=False)
def C(word):
    word = word.replace('_', ' ')
    return f"C {word}"


@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
@app.route("/python/<word>", strict_slashes=False)
def python(word='is cool'):
    word = word.replace('_', ' ')
    return f"Python {word}"


@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    return f"{num} is a number"


@app.route("/number_template/<int:num>", strict_slashes=False)
def num_temp(num):
    return render_template('5-number.html', num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
