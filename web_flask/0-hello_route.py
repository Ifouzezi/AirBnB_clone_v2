#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask, return_template


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return render_template("100-hbnb.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
