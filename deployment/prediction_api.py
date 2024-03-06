# prediction_api.py

from flask import Flask, request, jsonify
from ml_models import train_model, predict

app = Flask(__name__)
model = None

@app.route("/train", methods=["POST"])
def train():
    global model
    data = request.json
    X_train, y_train = data["X_train"], data["y_train"]
    model = train_model(X_train, y_train)
    return "Model trained successfully!"

@app.route("/predict", methods=["POST"])
def predict():
    global model
    data = request.json
    predictions = predict(model, data["X_test"])
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
