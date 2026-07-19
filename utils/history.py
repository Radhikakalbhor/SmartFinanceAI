import pandas as pd
import os


def save_history(filename, data):

    filepath = os.path.join("data", filename)

    df = pd.DataFrame([data])

    if os.path.exists(filepath):
        df.to_csv(filepath, mode="a", header=False, index=False)
    else:
        df.to_csv(filepath, index=False)


def load_history(filename):

    filepath = os.path.join("data", filename)

    if os.path.exists(filepath):
        return pd.read_csv(filepath)

    return pd.DataFrame()