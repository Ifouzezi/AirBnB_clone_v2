#!/usr/bin/python3
"""Simple Flask app"""
from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_airbnb():
    return "Hello, Airbnb One Page!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
