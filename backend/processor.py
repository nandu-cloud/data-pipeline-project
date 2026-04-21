import pandas as pd

def process_data():
    df = pd.read_csv("../data/sample_data.csv")
    df["processed"] = df["value"] * 2
    print(df)

