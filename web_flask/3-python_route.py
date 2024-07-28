#!/usr/bin/python3
'flask application that returns text on the home route'
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    ' the home of the server'
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    ' displays hbnb '
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    'returns C and appends the text passed'
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    'display python then text given'
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
