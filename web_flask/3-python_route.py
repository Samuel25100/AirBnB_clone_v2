#!/usr/bin/python3
"""Start a Flask web application and return simple string."""
import web_flask

app = web_flask.Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
