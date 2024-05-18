#!/usr/bin/python3
"""Start a Flask web application and return simple string."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnh():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
