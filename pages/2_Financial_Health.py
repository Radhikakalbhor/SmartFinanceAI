import streamlit as st
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
st.title("❤️ Financial Health Score")

st.write("Check your financial health based on your monthly income and expenses.")

st.markdown("---")

income = st.number_input(
    "💵 Monthly Income (₹)",
    min_value=0.0,
    step=1000.0
)

expenses = st.number_input(
    "💸 Total Monthly Expenses (₹)",
    min_value=0.0,
    step=1000.0
)

if st.button("Calculate Financial Health"):

    savings = income - expenses

    if income > 0:
        savings_percent = (savings / income) * 100
    else:
        savings_percent = 0

    if savings_percent >= 30:
        score = 100
        status = "🟢 Excellent"
        message = "Your financial health is excellent!"
    elif savings_percent >= 20:
        score = 80
        status = "🔵 Very Good"
        message = "You are managing your finances well."
    elif savings_percent >= 10:
        score = 60
        status = "🟡 Good"
        message = "You are doing okay, but there is room for improvement."
    elif savings_percent > 0:
        score = 40
        status = "🟠 Needs Improvement"
        message = "Try to increase your monthly savings."
    else:
        score = 20
        status = "🔴 Poor"
        message = "Your expenses are higher than your savings."

    st.markdown("---")

    st.subheader("📊 Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Savings", f"₹{savings:,.2f}")

    with col2:
        st.metric("Savings %", f"{savings_percent:.2f}%")

    with col3:
        st.metric("Health Score", f"{score}/100")

    st.progress(score / 100)

    st.success(status)

    st.info(message)

    st.markdown("---")

    st.subheader("🤖 AI Financial Recommendation")

    prompt = f"""
    A user has:

    Monthly Income: ₹{income}
    Monthly Expenses: ₹{expenses}
    Monthly Savings: ₹{savings}
    Financial Health Score: {score}/100

    Give:
    1. Four simple financial suggestions.
    2. One motivational tip.
    Keep the answer short and beginner-friendly.
    """

    with st.spinner("Analyzing your financial health..."):
        advice = ask_gemini(prompt)

    st.success(advice)