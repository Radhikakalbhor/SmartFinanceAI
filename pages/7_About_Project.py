import streamlit as st
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

st.title("ℹ️ About SmartFinance AI")

st.markdown("---")

st.header("📌 Project Overview")

st.write("""
**SmartFinance AI** is an LLM-based Personal Financial Assistant developed using
Python, Streamlit, and OpenRouter AI.

The application helps users understand and manage their personal finances
through AI-powered guidance and financial calculators.
""")

st.markdown("---")

st.header("🎯 Objectives")

st.markdown("""
- Help users improve financial literacy.
- Provide personalized AI financial advice.
- Assist with budgeting and savings.
- Calculate SIP and EMI instantly.
- Analyze expense data using AI.
""")

st.markdown("---")

st.header("✨ Features")

st.markdown("""
- 🤖 AI Financial Advisor
- 💰 Budget Planner
- ❤️ Financial Health Score
- 📈 SIP Calculator
- 🏦 EMI Calculator
- 🎯 Savings Goal Planner
- 📊 Expense Analyzer
""")

st.markdown("---")

st.header("🛠️ Technologies Used")

st.markdown("""
- Python
- Streamlit
- OpenRouter API
- GPT OSS 20B Model
- Plotly
- Pandas
- VS Code
""")

st.markdown("---")

st.header("🏗️ Project Workflow")

st.markdown("""
1. User enters financial information.
2. Financial calculations are performed.
3. Charts and summaries are generated.
4. AI analyzes the information.
5. Personalized recommendations are displayed.
""")

st.markdown("---")

st.header("🚀 Future Scope")

st.markdown("""
- Bank account integration
- Expense tracking using OCR
- Voice-based AI assistant
- Investment portfolio tracking
- Stock market insights
- Mobile application
""")

st.markdown("---")

st.header("👩‍💻 Developer")

st.write("""
**Name:** Radhika Kalbhor

**Department:** Information Technology

**College:** Shah and Anchor Kutchhi Engineering College (SAKEC)

**Project:** SmartFinance AI – An LLM-Based Personal Financial Assistant
""")

st.markdown("---")

st.success("Thank you for using SmartFinance AI!")