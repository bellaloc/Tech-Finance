# generate_processed_data.py

import pandas as pd

# Generate sample processed data
processed_data = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'price': [100, 110, 105, 115, 120, 118, 122, 125, 130, 128],
    'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Example additional feature
    'feature2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]   # Example additional feature
})

# Save processed data to CSV
processed_data.to_csv('processed_data/processed_data.csv', index=False)
