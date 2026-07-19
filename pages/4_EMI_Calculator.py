import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

from utils.gemini import ask_gemini
from utils.history import save_history
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

# ==========================
# Sidebar
# ==========================

st.sidebar.image("assets/logo.png", width=120)
st.sidebar.title("💰 SmartFinance AI")

# ==========================
# Header
# ==========================

st.title("🏦 EMI Calculator")
st.write("Calculate your monthly EMI and receive AI-powered loan advice.")

st.markdown("---")

# ==========================
# User Inputs
# ==========================

loan_amount = st.number_input(
    "💰 Loan Amount (₹)",
    min_value=10000,
    step=10000,
    value=500000
)

interest_rate = st.number_input(
    "📊 Annual Interest Rate (%)",
    min_value=1.0,
    max_value=25.0,
    value=9.0
)

loan_years = st.slider(
    "📅 Loan Tenure (Years)",
    1,
    30,
    10
)

# ==========================
# Calculate EMI
# ==========================

if st.button("Calculate EMI"):

    monthly_rate = interest_rate / 12 / 100
    months = loan_years * 12

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
    ) / ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - loan_amount

    # ==========================
    # Save History
    # ==========================

    history = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "Loan Amount": loan_amount,
        "Interest Rate": interest_rate,
        "Loan Years": loan_years,
        "Monthly EMI": emi,
        "Total Interest": total_interest,
        "Total Payment": total_payment
    }

    save_history("emi_history.csv", history)

    st.success("✅ EMI calculation saved successfully!")

    st.markdown("---")

    st.subheader("📊 Loan Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("💳 Monthly EMI", f"₹{emi:,.2f}")

    with c2:
        st.metric("💸 Total Interest", f"₹{total_interest:,.2f}")

    with c3:
        st.metric("🏦 Total Payment", f"₹{total_payment:,.2f}")

    st.markdown("---")

    # ==========================
    # Loan Breakdown Chart
    # ==========================

    chart = pd.DataFrame({
        "Category": ["Principal", "Interest"],
        "Amount": [loan_amount, total_interest]
    })

    fig = px.pie(
        chart,
        values="Amount",
        names="Category",
        title="🏦 Loan Breakdown",
        hole=0.45
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # AI Loan Advice
    # ==========================

    st.subheader("🤖 AI Loan Advice")

    prompt = f"""
A user wants a loan.

Loan Amount: ₹{loan_amount}

Interest Rate: {interest_rate}%

Loan Period: {loan_years} years

Monthly EMI: ₹{emi:.2f}

Total Interest: ₹{total_interest:.2f}

Give:

1. Four simple loan repayment tips.

2. Tell whether this loan looks affordable.

3. Suggest one way to reduce interest costs.

Keep the answer beginner-friendly.
"""

    with st.spinner("🤖 Analyzing your loan..."):
        advice = ask_gemini(prompt)

    st.success(advice)

st.markdown("---")

st.caption("SmartFinance AI | EMI Calculator")