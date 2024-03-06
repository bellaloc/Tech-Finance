# ml_models.py

from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def predict(model, X_test):
    predictions = model.predict(X_test)
    return predictions
