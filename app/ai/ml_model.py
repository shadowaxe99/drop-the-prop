
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load

class MLModel:
    def __init__(self):
        self.model = None

    def train(self, data):
        X = data.drop('target', axis=1)
        y = data['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier(n_estimators=100)
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Model trained with accuracy: {accuracy}")

    def predict(self, data):
        if self.model is None:
            raise Exception("Model not trained yet")

        return self.model.predict(data)

    def save_model(self, path):
        if self.model is None:
            raise Exception("Model not trained yet")

        dump(self.model, path)

    def load_model(self, path):
        self.model = load(path)
