#!/usr/bin/env python3
"""A Flask app that has a single route
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == "__main__":
    0-app.run(debug=True)
