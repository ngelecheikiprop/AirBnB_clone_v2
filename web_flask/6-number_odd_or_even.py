#!/usr/bin/python3
'flask application that returns text on the home route'
from flask import Flask
from flask import render_template
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


@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    'display python then text given'
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    'display n only if number'
    return f"{n}  is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    'display template with number n'
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_even(n):
    'display a number and says if odd or even'
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
