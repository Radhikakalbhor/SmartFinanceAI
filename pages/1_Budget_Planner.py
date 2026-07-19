import streamlit as st
import plotly.express as px
from utils.gemini import ask_gemini
from utils.history import save_history
from datetime import datetime
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(page_title="Budget Planner", page_icon="💰")

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

st.title("💰 Monthly Budget Planner")
st.write("Plan your monthly budget and receive AI-powered financial advice.")

st.markdown("---")

# ==========================
# User Inputs
# ==========================

income = st.number_input("💵 Monthly Income (₹)", min_value=0.0, step=1000.0)

rent = st.number_input("🏠 Rent (₹)", min_value=0.0, step=500.0)

food = st.number_input("🍔 Food (₹)", min_value=0.0, step=500.0)

transport = st.number_input("🚌 Transport (₹)", min_value=0.0, step=500.0)

shopping = st.number_input("🛍️ Shopping (₹)", min_value=0.0, step=500.0)

other = st.number_input("📦 Other Expenses (₹)", min_value=0.0, step=500.0)

# ==========================
# Calculate
# ==========================

if st.button("Calculate Budget"):

    total_expense = rent + food + transport + shopping + other
    savings = income - total_expense

    # Save History
    history = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "Income": income,
        "Expenses": total_expense,
        "Savings": savings,
        "Rent": rent,
        "Food": food,
        "Transport": transport,
        "Shopping": shopping,
        "Other": other
    }

    save_history("budget_history.csv", history)

    st.success("✅ Budget saved successfully!")

    st.subheader("📊 Budget Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("💸 Total Expenses", f"₹{total_expense:,.2f}")

    with col2:
        st.metric("💰 Remaining Savings", f"₹{savings:,.2f}")

    if income > 0:

        savings_percent = (savings / income) * 100

        st.metric("📈 Savings Percentage", f"{savings_percent:.2f}%")

        if savings_percent >= 20:
            st.success("🎉 Excellent! You are saving a healthy portion of your income.")
        elif savings_percent >= 10:
            st.warning("🙂 Good! Try increasing your savings a little more.")
        elif savings >= 0:
            st.info("⚠️ Your savings are quite low. Consider reducing unnecessary expenses.")
        else:
            st.error("❌ Your expenses are higher than your income!")

        # ==========================
        # Expense Chart
        # ==========================

        expense_data = {
            "Category": ["Rent", "Food", "Transport", "Shopping", "Other"],
            "Amount": [rent, food, transport, shopping, other]
        }

        fig = px.pie(
            values=expense_data["Amount"],
            names=expense_data["Category"],
            title="📊 Expense Distribution",
            hole=0.45
        )

        st.plotly_chart(fig, use_container_width=True)

        # ==========================
        # Highest Expense
        # ==========================

        expenses = {
            "🏠 Rent": rent,
            "🍔 Food": food,
            "🚌 Transport": transport,
            "🛍️ Shopping": shopping,
            "📦 Other": other
        }

        highest = max(expenses, key=expenses.get)

        st.subheader("💸 Highest Expense")

        st.info(f"{highest}: ₹{expenses[highest]:,.2f}")

        # ==========================
        # AI Advice
        # ==========================

        st.subheader("🤖 AI Financial Advice")

        prompt = f"""
My monthly income is ₹{income}.

My monthly expenses are:

Rent: ₹{rent}

Food: ₹{food}

Transport: ₹{transport}

Shopping: ₹{shopping}

Other: ₹{other}

My savings are ₹{savings}.

Give me:
1. Five simple financial tips.
2. Tell me whether my savings are good.
3. Suggest one expense I should reduce.
Keep the answer simple and beginner-friendly.
"""

        with st.spinner("🤖 Analyzing your budget..."):
            advice = ask_gemini(prompt)

        st.success(advice)

st.markdown("---")

st.caption("SmartFinance AI | Budget Planner")