#!/usr/bin/python3
"""Start a Flask web application and return simple string."""
import web_flask

app = web_flask.Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
    return ("Hello HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
