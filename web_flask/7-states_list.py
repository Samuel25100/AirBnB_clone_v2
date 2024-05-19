#!/usr/bin/python3
"""Start a Flask web application and return simple string."""
from models import storage
from models import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def State_list():
    dic = storage.all("State")
    result = {}
    for val in dic.values():
        result[val.name] = val.id
    sorted_dict = dict(sorted(result.items()))
    return render_template('7-states_list.html', dic=sorted_dict)


@app.teardown_appcontext
def clean(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
