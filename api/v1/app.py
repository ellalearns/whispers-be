#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
def letsgo():
    """
    """
    return {
        "greeting": "welcome, sailor :)"
    }



if __name__ == "__main__":
    app.run(debug=True)
