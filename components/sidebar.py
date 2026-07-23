# components/sidebar.py

import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("💰 SmartFinance AI")

        st.markdown("---")

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "📜 History",
                "📊 Reports"
            ]
        )

        st.markdown("---")

        st.subheader("💵 Financial Details")

        income = st.number_input(
            "Monthly Income (₹)",
            min_value=0,
            value=50000,
            step=1000
        )

        expenses = st.number_input(
            "Monthly Expenses (₹)",
            min_value=0,
            value=25000,
            step=1000
        )

        savings = st.number_input(
            "Current Savings (₹)",
            min_value=0,
            value=100000,
            step=1000
        )

        monthly_sip = st.number_input(
            "Monthly SIP (₹)",
            min_value=0,
            value=5000,
            step=500
        )

        monthly_emi = st.number_input(
            "Monthly EMI (₹)",
            min_value=0,
            value=0,
            step=500
        )

        age = st.slider(
            "Age",
            18,
            80,
            25
        )

        risk = st.selectbox(
            "Risk Profile",
            [
                "Low",
                "Medium",
                "High"
            ]
        )

        goal = st.selectbox(
            "Primary Goal",
            [
                "Emergency Fund",
                "Buy a House",
                "Retirement",
                "Wealth Creation",
                "Education",
                "Vacation"
            ]
        )

        st.markdown("---")

        analyze = st.button(
            "🚀 Analyze Financial Health",
            use_container_width=True
        )

        st.markdown("---")

        st.caption("SmartFinance AI v2.0")

    return (
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
    )