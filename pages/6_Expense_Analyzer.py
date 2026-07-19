import streamlit as st
import pandas as pd
import plotly.express as px
from utils.gemini import ask_gemini
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.sidebar.image("assets/logo.png", width=120)

st.sidebar.title("💰 SmartFinance AI")

st.sidebar.markdown("---")

st.sidebar.success("AI Powered Personal Finance Assistant")

st.sidebar.markdown("---")

st.sidebar.info("""
Developed By

**Radhika Kalbhor**

Department of Information Technology

SAKEC
""")

st.title("📊 Expense Analyzer")

st.write("Upload your monthly expense CSV and get AI-powered insights.")

st.markdown("---")

uploaded_file = st.file_uploader(
    "📂 Upload Expense CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data")

    st.dataframe(df)

    if "Category" in df.columns and "Amount" in df.columns:

        st.markdown("---")

        category_total = df.groupby("Category")["Amount"].sum().reset_index()

        st.subheader("📈 Expense Distribution")

        fig = px.pie(
            category_total,
            values="Amount",
            names="Category",
            hole=0.4,
            title="Expenses by Category"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        st.subheader("📊 Category-wise Expenses")

        bar = px.bar(
            category_total,
            x="Category",
            y="Amount",
            title="Expense by Category"
        )

        st.plotly_chart(bar, use_container_width=True)

        highest = category_total.loc[
            category_total["Amount"].idxmax()
        ]

        st.success(
            f"💰 Highest Spending Category: {highest['Category']} (₹{highest['Amount']:.2f})"
        )

        total = category_total["Amount"].sum()

        st.info(f"💵 Total Monthly Expenses: ₹{total:,.2f}")

        st.markdown("---")

        st.subheader("🤖 AI Expense Insights")

        prompt = f"""
        Expense Summary:

        {category_total.to_string(index=False)}

        Total Expenses: ₹{total}

        Highest Spending Category: {highest['Category']}

        Give:

        1. Four suggestions to reduce expenses.

        2. Identify unnecessary spending if possible.

        3. Give one budgeting tip.

        Keep the answer simple.
        """

        with st.spinner("Analyzing expenses..."):
            advice = ask_gemini(prompt)

        st.success(advice)

    else:
        st.error("CSV must contain 'Category' and 'Amount' columns.")