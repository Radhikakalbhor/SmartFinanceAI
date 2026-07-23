# 0_Dashboard.py

import streamlit as st

from components.sidebar import render_sidebar
from components.hero import render_hero
from components.kpi_cards import render_kpis
from components.charts import render_charts
from components.recommendations import render_recommendations
from components.chatbot import render_chatbot
from components.footer import render_footer
from components.history import render_history, save_history
from components.reports import render_reports

from components.financial_health import generate_financial_report


st.set_page_config(
    page_title="SmartFinance AI",
    page_icon="💰",
    layout="wide"
)


(
    page,
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


if page == "🏠 Dashboard":

    report = generate_financial_report(
        income,
        expenses,
        savings,
        monthly_sip,
        monthly_emi
    )

    health = report["health_score"]

    status = report["status"]

    render_hero(
        health,
        income,
        expenses,
        savings
    )

    st.markdown("---")

    render_kpis(
        income,
        expenses,
        savings,
        monthly_sip,
        monthly_emi,
        health
    )

    st.markdown("---")

    render_charts(
        income,
        expenses,
        savings,
       health
    )

    st.markdown("---")

    goal_progress = min((savings / 500000) * 100, 100)

    render_recommendations(
        income,
        expenses,
        savings,
        monthly_emi,
        goal_progress
    )

    st.markdown("---")

    render_chatbot(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    goal_progress
)

    st.markdown("---")

    if analyze:

        save_history(
            income,
            expenses,
            savings,
            monthly_sip,
            monthly_emi,
            health
        )

        st.success("Financial report saved successfully.")

    render_footer(
    health
)


elif page == "📜 History":

    render_history()


elif page == "📊 Reports":

    render_reports()