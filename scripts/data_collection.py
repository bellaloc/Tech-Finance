# data_collection.py

import pandas as pd

def fetch_raw_data():
    # Simulated function to fetch raw data
    raw_data = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                             'price': [100, 110, 105]})
    return raw_data

def save_raw_data(raw_data, file_path):
    raw_data.to_csv(file_path, index=False)

if __name__ == "__main__":
    raw_data = fetch_raw_data()
    save_raw_data(raw_data, "data/raw_data/raw_data.csv")
