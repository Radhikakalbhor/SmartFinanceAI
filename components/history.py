import streamlit as st
import pandas as pd
import os
from datetime import datetime

HISTORY_FILE = "history.csv"


def initialize_history():
    if not os.path.exists(HISTORY_FILE):
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
        df.to_csv(HISTORY_FILE, index=False)


def save_history(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    health
):

    initialize_history()

    df = pd.read_csv(HISTORY_FILE)

    new_data = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Income": income,
        "Expenses": expenses,
        "Savings": savings,
        "SIP": monthly_sip,
        "EMI": monthly_emi,
        "Health Score": health
    }

    df = pd.concat(
        [df, pd.DataFrame([new_data])],
        ignore_index=True
    )

    df.to_csv(HISTORY_FILE, index=False)


def render_history():

    initialize_history()

    st.title("📜 History Center")

    df = pd.read_csv(HISTORY_FILE)

    if df.empty:
        st.info("No history available.")
        return

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    col1, col2 = st.columns(2)

    with col1:

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download History",
            data=csv,
            file_name="history.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:

        if st.button(
            "🗑 Clear History",
            use_container_width=True
        ):

            os.remove(HISTORY_FILE)

            initialize_history()

            st.success("History Cleared")

            st.rerun()

    st.markdown("---")

    st.subheader("📈 Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Total Records",
            len(df)
        )

    with c2:
        st.metric(
            "Highest Income",
            f"₹{df['Income'].max():,.0f}"
        )

    with c3:
        st.metric(
            "Average Health",
            f"{df['Health Score'].mean():.1f}"
        )

    st.markdown("---")

    st.subheader("📊 Income Trend")

    st.line_chart(df["Income"])

    st.subheader("📊 Expense Trend")

    st.line_chart(df["Expenses"])

    st.subheader("📊 Savings Trend")

    st.line_chart(df["Savings"])