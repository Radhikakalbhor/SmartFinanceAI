import streamlit as st
import plotly.express as px
import pandas as pd

from utils.history import load_history
from utils.gemini import ask_gemini
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

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

st.title("📊 SmartFinance AI Dashboard")
st.write("Your complete financial overview in one place.")

st.markdown("---")

# ==========================
# Load History
# ==========================

budget = load_history("budget_history.csv")
sip = load_history("sip_history.csv")
emi = load_history("emi_history.csv")
savings = load_history("savings_history.csv")

# ==========================
# Latest Data
# ==========================

income = expenses = savings_amt = 0
monthly_sip = maturity = 0
monthly_emi = 0
goal_progress = 0

if not budget.empty:
    latest = budget.iloc[-1]
    income = latest["Income"]
    expenses = latest["Expenses"]
    savings_amt = latest["Savings"]

if not sip.empty:
    latest = sip.iloc[-1]
    monthly_sip = latest["Monthly SIP"]
    maturity = latest["Maturity Value"]

if not emi.empty:
    latest = emi.iloc[-1]
    monthly_emi = latest["Monthly EMI"]

if not savings.empty:
    latest = savings.iloc[-1]
    goal_progress = latest["Progress (%)"]

# ==========================
# Financial Health Score
# ==========================

if income > 0:

    ratio = expenses / income

    if ratio < 0.50:
        health = 95

    elif ratio < 0.70:
        health = 80

    elif ratio < 0.90:
        health = 65

    else:
        health = 45

else:
    health = 0

# ==========================
# KPI Cards
# ==========================

c1, c2, c3 = st.columns(3)

c1.metric("💰 Income", f"₹{income:,.0f}")
c2.metric("💸 Expenses", f"₹{expenses:,.0f}")
c3.metric("💵 Savings", f"₹{savings_amt:,.0f}")

c4, c5, c6 = st.columns(3)

c4.metric("📈 Monthly SIP", f"₹{monthly_sip:,.0f}")
c5.metric("🏦 Monthly EMI", f"₹{monthly_emi:,.0f}")
c6.metric("❤️ Health Score", f"{health}/100")

st.markdown("---")

# ==========================
# Charts
# ==========================

col1, col2 = st.columns(2)

with col1:

    if income > 0:

        chart = pd.DataFrame({
            "Category": ["Expenses", "Savings"],
            "Amount": [expenses, savings_amt]
        })

        fig = px.pie(
            chart,
            names="Category",
            values="Amount",
            hole=0.45,
            title="Expense Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

with col2:

    if income > 0:

        chart = pd.DataFrame({
            "Category": ["Income", "Expenses", "Savings"],
            "Amount": [income, expenses, savings_amt]
        })

        fig = px.bar(
            chart,
            x="Category",
            y="Amount",
            title="Financial Overview"
        )

        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================
# Goal Progress
# ==========================

st.subheader("🎯 Savings Goal Progress")

st.progress(goal_progress / 100)

st.write(f"Goal Completed: **{goal_progress:.1f}%**")

st.markdown("---")

# ==========================
# Smart Alerts
# ==========================

st.subheader("🚨 Smart Financial Alerts")

if income == 0:
    st.info("No budget information available.")

else:

    if expenses > income * 0.80:
        st.error("⚠️ Your expenses are above 80% of your income.")

    elif expenses > income * 0.60:
        st.warning("⚠️ Your expenses are moderately high.")

    else:
        st.success("✅ Your spending is under control.")

if monthly_emi > income * 0.40:
    st.warning("🏦 Your EMI consumes a significant portion of your income.")

if savings_amt < income * 0.20:
    st.info("💡 Consider increasing your monthly savings.")

st.markdown("---")

# ==========================
# AI Financial Insight
# ==========================

st.subheader("🤖 AI Financial Insight")

if st.button("Generate AI Financial Summary"):

    prompt = f"""
    Analyze the user's financial situation.

    Income: ₹{income}
    Expenses: ₹{expenses}
    Savings: ₹{savings_amt}

    Monthly SIP: ₹{monthly_sip}

    Monthly EMI: ₹{monthly_emi}

    Savings Goal Progress: {goal_progress:.1f}%

    Give:

    1. Overall financial health

    2. Three suggestions

    3. One motivational message

    Keep it short.
    """

    with st.spinner("Generating AI summary..."):
        response = ask_gemini(prompt)

    st.success(response)

st.markdown("---")

st.caption("© 2026 SmartFinance AI | Professional Financial Dashboard")