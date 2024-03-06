# app.py (Flask web app)

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    processed_data = pd.read_csv("data/processed_data/processed_data.csv")
    return render_template("index.html", data=processed_data.to_html())

if __name__ == "__main__":
    app.run(debug=True)
