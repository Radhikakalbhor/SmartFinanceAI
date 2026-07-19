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

st.title("📈 SIP Investment Calculator")

st.write("Calculate your future investment value and receive AI-powered investment advice.")

st.markdown("---")

# ==========================
# User Inputs
# ==========================

monthly_investment = st.number_input(
    "💰 Monthly SIP Amount (₹)",
    min_value=500,
    step=500,
    value=5000
)

annual_rate = st.number_input(
    "📊 Expected Annual Return (%)",
    min_value=1.0,
    max_value=30.0,
    value=12.0
)

years = st.slider(
    "📅 Investment Period (Years)",
    1,
    40,
    10
)

# ==========================
# Calculate SIP
# ==========================

if st.button("Calculate SIP"):

    monthly_rate = annual_rate / 12 / 100
    months = years * 12

    maturity_value = (
        monthly_investment *
        (((1 + monthly_rate) ** months - 1) / monthly_rate) *
        (1 + monthly_rate)
    )

    invested_amount = monthly_investment * months
    wealth_gained = maturity_value - invested_amount

    # ==========================
    # Save History
    # ==========================

    history = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "Monthly SIP": monthly_investment,
        "Annual Return": annual_rate,
        "Years": years,
        "Total Investment": invested_amount,
        "Wealth Gained": wealth_gained,
        "Maturity Value": maturity_value
    }

    save_history("sip_history.csv", history)

    st.success("✅ SIP calculation saved successfully!")

    st.markdown("---")

    st.subheader("📊 Investment Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💵 Total Investment", f"₹{invested_amount:,.2f}")

    with col2:
        st.metric("📈 Wealth Gained", f"₹{wealth_gained:,.2f}")

    with col3:
        st.metric("🏆 Maturity Value", f"₹{maturity_value:,.2f}")

    st.markdown("---")

    # ==========================
    # Year-wise Growth
    # ==========================

    st.subheader("📈 Year-wise Growth")

    values = []

    for year in range(1, years + 1):

        months_completed = year * 12

        value = (
            monthly_investment *
            (((1 + monthly_rate) ** months_completed - 1) / monthly_rate) *
            (1 + monthly_rate)
        )

        values.append({
            "Year": year,
            "Investment Value": value
        })

    df = pd.DataFrame(values)

    fig = px.line(
        df,
        x="Year",
        y="Investment Value",
        markers=True,
        title="SIP Growth Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # AI Advice
    # ==========================

    st.subheader("🤖 AI Investment Advice")

    prompt = f"""
A user invests ₹{monthly_investment} every month.

Expected Return: {annual_rate}%

Investment Period: {years} years.

Total Investment: ₹{invested_amount:.2f}

Maturity Value: ₹{maturity_value:.2f}

Give:
1. Four beginner-friendly SIP tips.
2. Explain whether this is a good investment.
3. Suggest one improvement.

Keep the answer simple.
"""

    with st.spinner("🤖 Analyzing your SIP..."):
        advice = ask_gemini(prompt)

    st.success(advice)

st.markdown("---")

st.caption("SmartFinance AI | SIP Calculator")