# components/sidebar.py

import streamlit as st
from utils.history import load_history


def get_latest_budget():

    try:
        history = load_history("budget_history.csv")

        if not history.empty:

            latest = history.iloc[-1]

            return {
                "income": float(latest.get("Income", 50000)),
                "expenses": float(latest.get("Expenses", 25000)),
                "savings": float(latest.get("Savings", 25000))
            }

    except Exception:
        pass

    return {
        "income": 50000.0,
        "expenses": 25000.0,
        "savings": 25000.0
    }


def render_sidebar():

    # =====================================================
    # LOAD LATEST BUDGET DATA
    # =====================================================

    latest_budget = get_latest_budget()

    latest_income = latest_budget["income"]
    latest_expenses = latest_budget["expenses"]
    latest_savings = latest_budget["savings"]

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.title("💰 SmartFinance AI")

        st.markdown("---")

        st.subheader("💵 Financial Details")

        st.caption("Latest values from Budget Planner")

        # =================================================
        # INCOME
        # =================================================

        income = st.number_input(
            "Monthly Income (₹)",
            min_value=0.0,
            value=float(latest_income),
            step=1000.0,
            key="dashboard_income"
        )

        # =================================================
        # EXPENSES
        # =================================================

        expenses = st.number_input(
            "Monthly Expenses (₹)",
            min_value=0.0,
            value=float(latest_expenses),
            step=1000.0,
            key="dashboard_expenses"
        )

        # =================================================
        # SAVINGS
        # =================================================

        savings = st.number_input(
            "Current Savings (₹)",
            min_value=0.0,
            value=float(latest_savings),
            step=1000.0,
            key="dashboard_savings"
        )

        # =================================================
        # SIP
        # =================================================

        monthly_sip = st.number_input(
            "Monthly SIP (₹)",
            min_value=0.0,
            value=5000.0,
            step=500.0,
            key="dashboard_sip"
        )

        # =================================================
        # EMI
        # =================================================

        monthly_emi = st.number_input(
            "Monthly EMI (₹)",
            min_value=0.0,
            value=0.0,
            step=500.0,
            key="dashboard_emi"
        )

        # =================================================
        # AGE
        # =================================================

        age = st.slider(
            "Age",
            min_value=18,
            max_value=80,
            value=25,
            key="dashboard_age"
        )

        # =================================================
        # RISK PROFILE
        # =================================================

        risk = st.selectbox(
            "Risk Profile",
            [
                "Low",
                "Medium",
                "High"
            ],
            key="dashboard_risk"
        )

        # =================================================
        # PRIMARY GOAL
        # =================================================

        goal = st.selectbox(
            "Primary Goal",
            [
                "Emergency Fund",
                "Buy a House",
                "Retirement",
                "Wealth Creation",
                "Education",
                "Vacation"
            ],
            key="dashboard_goal"
        )

        st.markdown("---")

        # =================================================
        # ANALYZE
        # =================================================

        analyze = st.button(
            "🚀 Analyze Financial Health",
            use_container_width=True
        )

        st.markdown("---")

        if latest_income > 0:

            st.success(
                "✅ Latest Budget Planner data loaded"
            )

        else:

            st.info(
                "💡 Add a budget in Budget Planner "
                "to update your Dashboard."
            )

        st.caption("SmartFinance AI v3.0")

    return (
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