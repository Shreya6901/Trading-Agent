import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

class Predictor:
    def __init__(self, model_path: str = "model.pkl"):
        self.model_path = model_path

    def train(self, df: pd.DataFrame):
        df = df.copy()
        df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
        X = df.drop(columns=["Target"])
        y = df["Target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        joblib.dump(model, self.model_path)
        print(f"Test accuracy: {model.score(X_test, y_test):.2f}")

    def predict(self, df: pd.DataFrame) -> int:
        model = joblib.load(self.model_path)
        features = df.dropna().iloc[-1:]
        return int(model.predict(features)[0])