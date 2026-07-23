import streamlit as st
import time

st.set_page_config(
    page_title="SmartFinance AI",
    page_icon="🏦",
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
# Loading Screen
# ==========================

with st.spinner("🚀 Launching SmartFinance AI..."):
    time.sleep(2)

# ==========================
# Sidebar
# ==========================

st.sidebar.image("assets/logo.png", width=140)

st.sidebar.title("💰 SmartFinance AI")

st.sidebar.markdown("### Personal Finance Assistant")

st.sidebar.success("🚀 Version 3.0")

st.sidebar.markdown("---")

st.sidebar.info("""
### 📌 About

SmartFinance AI is an LLM-powered personal finance assistant designed to help users manage budgeting, investments, loans, savings and financial planning.

Navigate through the pages using the sidebar.
""")

st.sidebar.markdown("---")

st.sidebar.success("Developed by")

st.sidebar.write("**Radhika Kalbhor**")

st.sidebar.write("Department of Information Technology")

st.sidebar.write("SAKEC")

# ==========================
# Logo
# ==========================

st.image(
    "assets/logo.png",
    width=180
)

# ==========================
# Title
# ==========================

st.title("💰 SmartFinance AI")

st.subheader("Your AI-Powered Personal Financial Assistant")

st.markdown("---")

# ==========================
# Hero Section
# ==========================

left, right = st.columns([2,1])

with left:

    st.header("👋 Welcome")

    st.write("""
SmartFinance AI is a Large Language Model (LLM) based Personal Financial Assistant developed to simplify personal finance management.

The application combines Artificial Intelligence with financial planning tools to help users:

- Manage monthly budgets
- Track expenses
- Calculate EMI
- Plan SIP investments
- Set savings goals
- Analyze financial health
- Receive AI-powered financial advice

The goal is to improve financial awareness through an easy-to-use intelligent assistant.
""")

with right:

    st.info("""
### 🛠 Technology Stack

- Python

- Streamlit

- OpenRouter AI

- GPT OSS 20B

- Plotly

- Pandas

- CSV Database
""")

st.markdown("---")

# ==========================
# Quick Navigation
# ==========================

st.header("🚀 Explore SmartFinance AI")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
### 💰 Budget Planner

✔ Track Income

✔ Manage Expenses

✔ Monthly Savings

✔ Financial Health
""")

with col2:

    st.success("""
### 📈 Investment Tools

✔ SIP Calculator

✔ EMI Calculator

✔ Savings Goal Planner

✔ Smart Reports
""")

with col3:

    st.success("""
### 🤖 AI Assistant

✔ Financial Advice

✔ AI Insights

✔ Expense Analysis

✔ Personalized Guidance
""")

st.markdown("---")

# ==========================
# Features
# ==========================

st.header("✨ Key Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
### 🤖 AI Advisor

✔ Ask Finance Questions

✔ AI Investment Guidance

✔ Smart Recommendations

✔ Personalized Responses
""")

with c2:

    st.success("""
### 💰 Financial Tools

✔ Budget Planner

✔ Financial Health Score

✔ SIP Calculator

✔ EMI Calculator

✔ Savings Planner
""")

with c3:

    st.success("""
### 📊 Analytics

✔ Interactive Charts

✔ Expense Reports

✔ Financial Dashboard

✔ AI Report Generator

✔ Download Reports
""")

st.markdown("---")

# ==========================
# Why Choose SmartFinance AI
# ==========================

st.header("🌟 Why Choose SmartFinance AI?")

a, b = st.columns(2)

with a:

    st.markdown("""
✅ AI-powered Financial Planning

✅ Modern User Interface

✅ Interactive Visualizations

✅ Real-Time Calculations

✅ Beginner Friendly
""")

with b:

    st.markdown("""
✅ Personalized AI Advice

✅ Expense Analysis

✅ Savings Tracking

✅ Secure Local Data Storage

✅ Professional Reports
""")

st.markdown("---")
# ==========================
# Project Statistics
# ==========================

st.header("📊 Project Statistics")

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric("📄 Pages", "10")

with p2:
    st.metric("🤖 AI Features", "6")

with p3:
    st.metric("📊 Charts", "12+")

with p4:
    st.metric("🛠 Modules", "8")

st.markdown("---")

# ==========================
# Technology Stack
# ==========================

st.header("🛠 Detailed Technology Stack")

t1, t2 = st.columns(2)

with t1:

    st.markdown("""
### 💻 Frontend

- Streamlit
- HTML/CSS
- Plotly Charts
""")

    st.markdown("""
### ⚙ Backend

- Python
- Pandas
- CSV Storage
""")

with t2:

    st.markdown("""
### 🤖 Artificial Intelligence

- OpenRouter API
- GPT OSS 20B
- Prompt Engineering
""")

    st.markdown("""
### 📊 Data Visualization

- Plotly Express
- Interactive Charts
- Financial Dashboard
""")

st.markdown("---")

# ==========================
# Project Objective
# ==========================

st.header("🎯 Project Objective")

st.write("""
SmartFinance AI combines the capabilities of Large Language Models (LLMs)
with practical financial planning tools.

The application helps users:

- Plan monthly budgets
- Analyze spending habits
- Improve financial health
- Calculate loans and investments
- Track savings goals
- Receive AI-powered financial recommendations

The primary objective is to improve financial literacy using an intelligent,
interactive and beginner-friendly platform.
""")

st.markdown("---")

# ==========================
# Future Scope
# ==========================

st.header("🚀 Future Scope")

f1, f2 = st.columns(2)

with f1:

    st.success("""
✅ Voice Assistant

✅ Tax Calculator

✅ PDF Financial Reports

✅ Credit Score Analysis
""")

with f2:

    st.success("""
✅ Bank Account Integration

✅ Mobile Application

✅ Investment Portfolio Tracker

✅ Cloud Database Support
""")

st.markdown("---")

# ==========================
# Developer Information
# ==========================

st.header("👩‍💻 Developer")

d1, d2 = st.columns([1, 3])

with d1:
    st.image("assets/logo.png", width=120)

with d2:
    st.markdown("""
### Radhika Kalbhor

**Department of Information Technology**

Shah & Anchor Kutchhi Engineering College (SAKEC)

Mumbai, Maharashtra

**Project:** SmartFinance AI – An LLM-Based Personal Financial Assistant
""")

st.markdown("---")

# ==========================
# Get Started
# ==========================

st.success(
    "👈 Use the sidebar to explore Budget Planner, AI Advisor, Dashboard, Reports, History, SIP Calculator, EMI Calculator and Savings Planner."
)

st.markdown("---")

# ==========================
# Disclaimer
# ==========================

st.warning("""
### ⚠ Disclaimer

This application has been developed for educational purposes only.

The financial advice generated by the AI model is informational and should
not be considered professional financial or investment advice.

Always consult a qualified financial advisor before making investment or
loan decisions.
""")

st.markdown("---")

# ==========================
# Footer
# ==========================

st.markdown(
"""
<div style='text-align:center; padding:20px;'>

<h4>💰 SmartFinance AI</h4>

<p>
An LLM-Based Personal Financial Assistant
</p>

<p>
Developed by <b>Radhika Kalbhor</b><br>
Department of Information Technology<br>
Shah & Anchor Kutchhi Engineering College (SAKEC)
</p>

<p>
© 2026 SmartFinance AI | All Rights Reserved
</p>

</div>
""",
unsafe_allow_html=True
)