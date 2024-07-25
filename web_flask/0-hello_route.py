#!/usr/bin/python3
'flask application that returns text on the home route'
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    ' the home of the server'
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
