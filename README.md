# Tech Finance Project

## Overview
The Tech Finance Project is a cutting-edge system designed to predict safe and valuable investments in real-time. Leveraging advanced technologies and machine learning models, this project aims to provide investors with actionable insights to optimize their investment strategies and maximize returns.

## Features

- **Data Collection:** Fetches real-time financial data from various sources, including stock market APIs, company financial reports, economic indicators, news sentiment analysis, and social media sentiment.

- **Data Processing:** Preprocesses raw data to clean, transform, and prepare it for analysis and modeling.

- **Machine Learning Models:** Trains predictive models using algorithms such as random forests, gradient boosting, LSTM networks, and sentiment analysis to forecast future investment performance.

- **Feature Engineering and Selection:** Identifies and engineers informative features from the data and selects the most relevant ones for model training.

- **Model Evaluation and Validation:** Evaluates model performance using metrics such as mean squared error and validates models on validation datasets.

- **Real-time Prediction and Deployment:** Deploys a scalable and efficient system for real-time investment prediction, providing users with recommendations based on their preferences and risk tolerance.

- **User Interface and Visualization:** Develops an intuitive web-based or mobile application with interactive data visualization features to display investment insights and predicted trends.

- **Continuous Monitoring and Improvement:** Implements mechanisms to monitor model performance, update models with new data, and continuously improve prediction accuracy and reliability.

## Installation

1. **Clone the repository:**
   
   git clone https://github.com/bellaloc/Tech-Finance.git

Install the required dependencies:

pip install -r requirements.txt

# Usage

Activate Virtual Environment (if not already activated):

source venv/bin/activate

Set Flask App Environment Variable:

export FLASK_APP=app.py

Set Flask Environment (Development, Production, etc.):

export FLASK_ENV=development

Run Flask Application:

flask run

This will start the Flask development server, and your application will be accessible at the specified address (usually http://127.0.0.1:5000/ by default).


Data Collection:

scripts: 

cd scripts: python3 data_collection.py 

to fetch raw financial data from APIs or data sources.

cd scripts: python3 data_preprocessing.py 

to preprocess the raw data for analysis.

Model Training and Prediction:

Train machine learning models using:

cd models - python3 ml_models.py.

Evaluate model performance and validate models using model_evaluation.py and model_validation.py.
Deploy the prediction API using prediction_api.py for real-time predictions.

User Interface and Visualization:

Develop a web-based or mobile application using frameworks like Flask, Django, or React.js with appropriate visualization libraries.

Continuous Monitoring and Improvement:

Implement monitoring mechanisms in model_monitoring.py to track model performance.

Update models periodically with new data using model_update.py to ensure continuous improvement.

Contributors

Christa Lococo
License

This project is licensed under the MIT License - see the LICENSE file for details.