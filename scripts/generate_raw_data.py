# generate_raw_data.py

import os
import pandas as pd

# Create the directory if it does not exist
os.makedirs('data/raw_data', exist_ok=True)

# Generate sample raw data
raw_data = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'price': [100, 110, 105, 115, 120, 118, 122, 125, 130, 128]
})

# Save raw data to CSV
raw_data.to_csv('data/raw_data/raw_data.csv', index=False)
