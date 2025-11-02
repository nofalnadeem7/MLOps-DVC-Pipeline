# src/feature.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import yaml

def load_params():
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    return params["features"]

def main():
    params = load_params()
    input_path = params["input_path"]
    output_path = params["output_path"]

    df = pd.read_csv(input_path)
    # Select relevant features
    df = df[["Age", "Gender"]]
    # Encode target variable
    encoder = LabelEncoder()
    df["Gender"] = encoder.fit_transform(df["Gender"])
    df.to_csv(output_path, index=False)
    print(f"Features saved to {output_path}")

if __name__ == "__main__":
    main()
