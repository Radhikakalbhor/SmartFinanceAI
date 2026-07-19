import streamlit as st
import pandas as pd
import plotly.express as px
import os

from utils.history import load_history
from utils.gemini import ask_gemini

st.set_page_config(
    page_title="Reports & Analytics",
    page_icon="📊",
    layout="wide"
)

# ==========================
# Load CSS
# ==========================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================
# Sidebar
# ==========================

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

# ==========================
# Header
# ==========================

st.title("📊 Financial Reports & Analytics")

st.write(
    "Analyze all your financial records with detailed reports and visualizations."
)

st.markdown("---")

# ==========================
# Load Data
# ==========================

budget = load_history("budget_history.csv")
sip = load_history("sip_history.csv")
emi = load_history("emi_history.csv")
savings = load_history("savings_history.csv")

# ==========================
# Summary Cards
# ==========================

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Budget Records", len(budget))
c2.metric("📈 SIP Records", len(sip))
c3.metric("🏦 EMI Records", len(emi))
c4.metric("🎯 Savings Records", len(savings))

st.markdown("---")

# ==========================
# Budget Summary
# ==========================

st.subheader("💰 Budget Summary")

if not budget.empty:

    latest_budget = budget.iloc[-1]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Income",
        f"₹{latest_budget['Income']:,.0f}"
    )

    col2.metric(
        "Expenses",
        f"₹{latest_budget['Expenses']:,.0f}"
    )

    col3.metric(
        "Savings",
        f"₹{latest_budget['Savings']:,.0f}"
    )

    st.markdown("### 📊 Monthly Expense Distribution")

    expense_chart = pd.DataFrame({
        "Category": [
            "Rent",
            "Food",
            "Transport",
            "Shopping",
            "Other"
        ],
        "Amount": [
            latest_budget["Rent"],
            latest_budget["Food"],
            latest_budget["Transport"],
            latest_budget["Shopping"],
            latest_budget["Other"]
        ]
    })

    fig = px.bar(
        expense_chart,
        x="Category",
        y="Amount",
        title="Monthly Expense Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if len(budget) > 1:

        st.markdown("### 📈 Savings Trend")

        fig = px.line(
            budget,
            x="Date",
            y="Savings",
            markers=True,
            title="Savings Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info("No Budget data available.")

st.markdown("---")

# ==========================
# SIP Summary
# ==========================

st.subheader("📈 SIP Summary")

if not sip.empty:

    latest_sip = sip.iloc[-1]

    c1, c2 = st.columns(2)

    c1.metric(
        "Monthly SIP",
        f"₹{latest_sip['Monthly SIP']:,.0f}"
    )

    c2.metric(
        "Maturity Value",
        f"₹{latest_sip['Maturity Value']:,.0f}"
    )

    if len(sip) > 1:

        st.markdown("### 📈 SIP Growth Trend")

        fig = px.line(
            sip,
            x="Date",
            y="Maturity Value",
            markers=True,
            title="SIP Growth"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info("No SIP data available.")

st.markdown("---")
# ==========================
# EMI Summary
# ==========================

st.subheader("🏦 EMI Summary")

if not emi.empty:

    latest_emi = emi.iloc[-1]

    c1, c2 = st.columns(2)

    c1.metric(
        "Monthly EMI",
        f"₹{latest_emi['Monthly EMI']:,.0f}"
    )

    c2.metric(
        "Total Payment",
        f"₹{latest_emi['Total Payment']:,.0f}"
    )

    if len(emi) > 1:

        st.markdown("### 📈 EMI Trend")

        fig = px.line(
            emi,
            x="Date",
            y="Monthly EMI",
            markers=True,
            title="Monthly EMI History"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info("No EMI data available.")

st.markdown("---")

# ==========================
# Savings Goal Summary
# ==========================

st.subheader("🎯 Savings Goal Summary")

if not savings.empty:

    latest_goal = savings.iloc[-1]

    c1, c2 = st.columns(2)

    c1.metric(
        "Goal Amount",
        f"₹{latest_goal['Goal Amount']:,.0f}"
    )

    c2.metric(
        "Goal Progress",
        f"{latest_goal['Progress (%)']:.1f}%"
    )

    st.progress(float(latest_goal["Progress (%)"]) / 100)

    if len(savings) > 1:

        st.markdown("### 📈 Savings Goal Progress Trend")

        fig = px.line(
            savings,
            x="Date",
            y="Progress (%)",
            markers=True,
            title="Savings Goal Progress"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info("No Savings Goal data available.")

st.markdown("---")

# ==========================
# AI Financial Report
# ==========================

st.subheader("🤖 AI Overall Financial Report")

if st.button("Generate Overall Financial Report"):

    income = latest_budget["Income"] if not budget.empty else 0
    expenses = latest_budget["Expenses"] if not budget.empty else 0
    saving = latest_budget["Savings"] if not budget.empty else 0

    monthly_sip = latest_sip["Monthly SIP"] if not sip.empty else 0

    monthly_emi = latest_emi["Monthly EMI"] if not emi.empty else 0

    progress = latest_goal["Progress (%)"] if not savings.empty else 0

    prompt = f"""
You are a personal finance advisor.

Analyze the following financial information.

Income: ₹{income}

Expenses: ₹{expenses}

Savings: ₹{saving}

Monthly SIP: ₹{monthly_sip}

Monthly EMI: ₹{monthly_emi}

Savings Goal Progress: {progress}%

Give:

1. Overall Financial Health

2. Three strengths

3. Three weaknesses

4. Five practical recommendations

5. One motivational message

Keep the answer concise and beginner friendly.
"""

    with st.spinner("Generating AI Financial Report..."):
        report = ask_gemini(prompt)

    with st.expander("📄 View AI Financial Report", expanded=True):
        st.success(report)

st.markdown("---")

# ==========================
# Download Reports
# ==========================

st.subheader("📥 Download Reports")

files = [
    ("Budget Report", "budget_history.csv"),
    ("SIP Report", "sip_history.csv"),
    ("EMI Report", "emi_history.csv"),
    ("Savings Report", "savings_history.csv")
]

for title, filename in files:

    filepath = os.path.join("data", filename)

    if os.path.exists(filepath):

        with open(filepath, "rb") as file:

            st.download_button(
                label=f"📄 Download {title}",
                data=file,
                file_name=filename,
                mime="text/csv",
                key=filename
            )

st.markdown("---")

st.info(
    "These reports are automatically generated from your saved financial records."
)

st.markdown("---")

st.caption(
    "© 2026 SmartFinance AI • LLM-Based Personal Financial Assistant • Developed by Radhika Kalbhor"
)