
# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data):
        df = pd.DataFrame(data)
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        return df.to_dict(orient='records')
