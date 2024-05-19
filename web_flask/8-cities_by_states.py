#!/usr/bin/python3
"""Start a Flask web application and return simple string."""
from models import storage
from models import State, City
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def State_list():
    dic = storage.all(State).values()
    return render_template('8-cities_by_states.html', dic=dic)


@app.teardown_appcontext
def clean(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
