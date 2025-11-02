# src/evaluate.py
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import json
import pickle
import yaml
import os

def load_params():
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    return params["evaluate"]

def main():
    params = load_params()
    data_path = params["data_path"]
    model_path = params["model_path"]
    metrics_path = params["metrics_path"]

    df = pd.read_csv(data_path)
    X = df[["Age"]]
    y = df["Gender"]

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X)

    accuracy = accuracy_score(y, y_pred)
    report = classification_report(y, y_pred, output_dict=True)

    print(f"Accuracy: {accuracy}")
    print("\nClassification Report:\n")
    print(classification_report(y, y_pred))

    # ✅ Save metrics to JSON file
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)
    with open(metrics_path, "w") as f:
        json.dump({"accuracy": accuracy, "classification_report": report}, f, indent=4)

if __name__ == "__main__":
    main()
