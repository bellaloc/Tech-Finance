from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import io
import base64
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Function to generate a line plot using Matplotlib and return it as a base64-encoded image
def generate_line_plot(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Value'], marker='o')
    plt.title('Tech-Finance Data')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    
    # Convert the plot to a base64-encoded image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return plot_data

@app.route("/")
def index():
    # Read processed data from CSV file
    processed_data = pd.read_csv("data/processed_data/processed_data.csv")
    
    # Convert processed data to a list of dictionaries for easy rendering in template
    data_list = processed_data.to_dict(orient='records')
    
    # Generate line plot using Matplotlib
    line_plot_data = generate_line_plot(processed_data)
    
    # Pass the processed data and line plot data to the template for rendering
    return render_template("index.html", data=data_list, line_plot=line_plot_data)

@app.route("/scatter")
def scatter_plot():
    # Read processed data from CSV file
    processed_data = pd.read_csv("data/processed_data/processed_data.csv")
    
    # Generate scatter plot using Plotly
    scatter_plot = px.scatter(processed_data, x='Date', y='Value', title='Tech-Finance Scatter Plot')
    
    # Convert scatter plot to HTML format
    scatter_plot_html = scatter_plot.to_html()
    
    return scatter_plot_html

if __name__ == "__main__":
    # Get the value of DEBUG from environment variables, defaulting to False if not set
    debug = os.getenv("DEBUG", False)

    # Run the app with debug mode enabled/disabled based on the value in the .env file
    app.run(debug=debug)
