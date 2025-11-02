# src/evaluate.py
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import pickle
import yaml

def load_params():
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    return params["evaluate"]

def main():
    params = load_params()
    data_path = params["data_path"]
    model_path = params["model_path"]

    df = pd.read_csv(data_path)
    X = df[["Age"]]
    y = df["Gender"]

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X)

    print(f"Accuracy: {accuracy_score(y, y_pred)}")
    print("\nClassification Report:\n")
    print(classification_report(y, y_pred))

if __name__ == "__main__":
    main()
