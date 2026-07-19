import streamlit as st
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

st.title("🎯 Savings Goal Planner")

st.write(
    "Plan your savings and find out how much you need to save every month to achieve your financial goal."
)

st.markdown("---")

# ==========================
# User Inputs
# ==========================

goal_amount = st.number_input(
    "🎯 Target Amount (₹)",
    min_value=1000,
    step=1000,
    value=500000
)

years = st.slider(
    "📅 Time to Achieve Goal (Years)",
    1,
    30,
    5
)

current_savings = st.number_input(
    "💰 Current Savings (₹)",
    min_value=0,
    step=1000,
    value=0
)

# ==========================
# Calculate
# ==========================

if st.button("Calculate Savings Plan"):

    remaining_amount = goal_amount - current_savings

    if remaining_amount < 0:
        remaining_amount = 0

    months = years * 12

    monthly_saving = remaining_amount / months

    progress = (current_savings / goal_amount) * 100

    if progress > 100:
        progress = 100

    # ==========================
    # Save History
    # ==========================

    history = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "Goal Amount": goal_amount,
        "Current Savings": current_savings,
        "Remaining Amount": remaining_amount,
        "Years": years,
        "Monthly Saving": monthly_saving,
        "Progress (%)": progress
    }

    save_history("savings_history.csv", history)

    st.success("✅ Savings plan saved successfully!")

    st.markdown("---")

    st.subheader("📊 Savings Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🎯 Goal Amount", f"₹{goal_amount:,.2f}")

    with c2:
        st.metric("💵 Remaining Amount", f"₹{remaining_amount:,.2f}")

    with c3:
        st.metric("📅 Monthly Savings Needed", f"₹{monthly_saving:,.2f}")

    st.markdown("### 📈 Goal Progress")

    st.progress(progress / 100)

    st.write(f"Current Progress: **{progress:.2f}%**")

    st.markdown("---")

    # ==========================
    # AI Advice
    # ==========================

    st.subheader("🤖 AI Savings Advice")

    prompt = f"""
A user has:

Goal Amount: ₹{goal_amount}

Current Savings: ₹{current_savings}

Remaining Amount: ₹{remaining_amount}

Time: {years} years

Required Monthly Saving: ₹{monthly_saving:.2f}

Give:

1. Four practical savings tips.

2. Suggest simple ways to achieve the goal faster.

3. Keep the advice short and beginner-friendly.
"""

    with st.spinner("🤖 Preparing your savings plan..."):
        advice = ask_gemini(prompt)

    st.success(advice)

st.markdown("---")

st.caption("SmartFinance AI | Savings Goal Planner")