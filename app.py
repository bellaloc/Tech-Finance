from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Read processed data from CSV file
    processed_data = pd.read_csv("data/processed_data/processed_data.csv")
    
    # Convert processed data to a list of dictionaries for easy rendering in template
    data_list = processed_data.to_dict(orient='records')
    
    # Pass the processed data to the template for rendering
    return render_template("index.html", data=data_list)

if __name__ == "__main__":
    app.run(debug=True)
