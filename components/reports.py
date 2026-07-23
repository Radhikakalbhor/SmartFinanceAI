# components/reports.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

HISTORY_FILE = "history.csv"


def render_reports():

    st.title("📊 Financial Reports")

    if not os.path.exists(HISTORY_FILE):
        st.warning("No history found.")
        return

    df = pd.read_csv(HISTORY_FILE)

    if df.empty:
        st.info("History is empty.")
        return

    st.markdown("## 📌 Report Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Average Income",
        f"₹{df['Income'].mean():,.0f}"
    )

    col2.metric(
        "Average Expenses",
        f"₹{df['Expenses'].mean():,.0f}"
    )

    col3.metric(
        "Average Savings",
        f"₹{df['Savings'].mean():,.0f}"
    )

    col4.metric(
        "Average Health",
        f"{df['Health Score'].mean():.1f}"
    )

    st.markdown("---")

    chart1 = px.line(
        df,
        x="Date",
        y=["Income", "Expenses", "Savings"],
        title="Income vs Expenses vs Savings",
        markers=True
    )

    st.plotly_chart(
        chart1,
        use_container_width=True
    )

    chart2 = px.bar(
        df,
        x="Date",
        y="Health Score",
        title="Financial Health Score"
    )

    st.plotly_chart(
        chart2,
        use_container_width=True
    )

    chart3 = px.area(
        df,
        x="Date",
        y="Savings",
        title="Savings Growth"
    )

    st.plotly_chart(
        chart3,
        use_container_width=True
    )

    chart4 = px.scatter(
        df,
        x="Income",
        y="Expenses",
        size="Savings",
        color="Health Score",
        hover_data=["Date"],
        title="Income vs Expenses"
    )

    st.plotly_chart(
        chart4,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📋 Complete Financial Report")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Financial Report",
        csv,
        "Financial_Report.csv",
        "text/csv",
        use_container_width=True
    )