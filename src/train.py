# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import yaml

def load_params():
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    return params["train"]

def main():
    params = load_params()
    data_path = params["data_path"]
    model_path = params["model_path"]
    test_size = params["test_size"]
    random_state = params["random_state"]

    df = pd.read_csv(data_path)
    X = df[["Age"]]
    y = df["Gender"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    main()
