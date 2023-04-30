import os

from flask import Flask
from db import get

app = Flask(__name__)


@app.route("/")
def hello_world():
    return get()

if __name__ == "__main__":
    app.run()