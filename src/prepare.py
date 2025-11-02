# src/prepare.py
import pandas as pd
import sys
import yaml

def load_params():
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    return params["prepare"]

def main():
    params = load_params()
    input_path = params["input_path"]
    output_path = params["output_path"]

    df = pd.read_csv(input_path)
    # You may do some optional cleaning or transformation here
    df.to_csv(output_path, index=False)
    print(f"Data prepared and saved to {output_path}")

if __name__ == "__main__":
    main()
