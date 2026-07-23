# pages/0_Dashboard.py

import streamlit as st

from components.sidebar import render_sidebar
from components.hero import render_hero
from components.kpi_cards import render_kpis
from components.charts import render_charts
from components.recommendations import render_recommendations
from components.chatbot import render_chatbot
from components.footer import render_footer
from components.history import save_history

from components.financial_health import generate_financial_report


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SmartFinance AI",
    page_icon="💰",
    layout="wide"
)


# =========================================================
# SIDEBAR
# =========================================================

(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    age,
    risk,
    goal,
    analyze
) = render_sidebar()


# =========================================================
# GENERATE FINANCIAL REPORT
# =========================================================

report = generate_financial_report(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi
)

health = report["health_score"]

status = report["status"]


# =========================================================
# HERO SECTION
# =========================================================

render_hero(
    health,
    income,
    expenses,
    savings
)

st.markdown("---")


# =========================================================
# KPI CARDS
# =========================================================

render_kpis(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    health
)

st.markdown("---")


# =========================================================
# FINANCIAL CHARTS
# =========================================================

render_charts(
    income,
    expenses,
    savings,
    health
)

st.markdown("---")


# =========================================================
# SAVINGS GOAL PROGRESS
# =========================================================

goal_progress = min(
    (savings / 500000) * 100,
    100
)


# =========================================================
# SMART RECOMMENDATIONS
# =========================================================

render_recommendations(
    income,
    expenses,
    savings,
    monthly_emi,
    goal_progress
)

st.markdown("---")


# =========================================================
# AI COPILOT
# =========================================================

render_chatbot(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    goal_progress
)

st.markdown("---")


# =========================================================
# SAVE FINANCIAL REPORT
# =========================================================

if analyze:

    save_history(
        income,
        expenses,
        savings,
        monthly_sip,
        monthly_emi,
        health
    )

    st.success(
        "✅ Financial report saved successfully."
    )


# =========================================================
# FOOTER
# =========================================================

render_footer(
    health
)