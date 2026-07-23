# utils/csv_manager.py

import os
import pandas as pd

CSV_FILE = "history.csv"


def initialize_csv():
    """
    Creates history.csv if it does not exist.
    """
    if not os.path.exists(CSV_FILE):

        df = pd.DataFrame(
            columns=[
                "Date",
                "Income",
                "Expenses",
                "Savings",
                "SIP",
                "EMI",
                "Health Score"
            ]
        )

        df.to_csv(CSV_FILE, index=False)


def load_history():
    """
    Returns complete history dataframe.
    """
    initialize_csv()

    return pd.read_csv(CSV_FILE)


def save_record(record):

    initialize_csv()

    df = pd.read_csv(CSV_FILE)

    df = pd.concat(
        [
            df,
            pd.DataFrame([record])
        ],
        ignore_index=True
    )

    df.to_csv(CSV_FILE, index=False)


def delete_history():

    initialize_csv()

    df = pd.DataFrame(
        columns=[
            "Date",
            "Income",
            "Expenses",
            "Savings",
            "SIP",
            "EMI",
            "Health Score"
        ]
    )

    df.to_csv(CSV_FILE, index=False)


def total_records():

    df = load_history()

    return len(df)


def latest_record():

    df = load_history()

    if df.empty:
        return None

    return df.iloc[-1]


def average_income():

    df = load_history()

    if df.empty:
        return 0

    return round(df["Income"].mean(), 2)


def average_expenses():

    df = load_history()

    if df.empty:
        return 0

    return round(df["Expenses"].mean(), 2)


def average_savings():

    df = load_history()

    if df.empty:
        return 0

    return round(df["Savings"].mean(), 2)


def average_health():

    df = load_history()

    if df.empty:
        return 0

    return round(df["Health Score"].mean(), 2)


def highest_income():

    df = load_history()

    if df.empty:
        return 0

    return df["Income"].max()


def highest_savings():

    df = load_history()

    if df.empty:
        return 0

    return df["Savings"].max()


def export_csv():

    df = load_history()

    return df.to_csv(index=False).encode("utf-8")