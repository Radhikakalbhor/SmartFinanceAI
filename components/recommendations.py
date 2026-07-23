import streamlit as st


def render_recommendations(
    income,
    expenses,
    savings,
    monthly_emi,
    goal_progress
):

    st.markdown("## 🎯 Smart Recommendations")

    # =====================================================
    # SAVINGS GOAL
    # =====================================================

    st.markdown("### 🎯 Savings Goal Progress")

    left, right = st.columns([4, 1])

    with left:

        st.progress(goal_progress / 100)

    with right:

        st.metric(
            "Completed",
            f"{goal_progress:.1f}%"
        )

    st.markdown("---")

    # =====================================================
    # SMART ALERTS
    # =====================================================

    st.markdown("### 🚨 Smart Financial Alerts")

    if income == 0:

        st.info(
            "No financial history found. Add your budget to unlock AI insights."
        )

    else:

        expense_ratio = expenses / income
        emi_ratio = monthly_emi / income
        savings_ratio = savings / income

        if expense_ratio > 0.80:

            st.error(
                "🔴 High Spending Alert\n\n"
                "Your expenses are above 80% of your monthly income."
            )

        elif expense_ratio > 0.60:

            st.warning(
                "🟠 Moderate Spending Alert\n\n"
                "Your expenses are increasing."
            )

        else:

            st.success(
                "🟢 Excellent spending discipline."
            )

        if emi_ratio > 0.40:

            st.warning(
                "🏦 EMI Alert\n\n"
                "Your EMI exceeds the recommended limit."
            )

        if savings_ratio < 0.20:

            st.info(
                "💡 Try saving at least 20% of your monthly income."
            )

    st.markdown("---")

    # =====================================================
    # AI RECOMMENDATION ENGINE
    # =====================================================

    st.markdown("## 🧠 AI Recommendation Engine")

    c1, c2, c3 = st.columns(3)

    # ---------------- CARD 1 ---------------- #

    with c1:

        if income > 0 and savings / income < 0.20:

            st.warning("""
### 💰 Savings

Increase your monthly savings.

**Priority:** High

**Recommendation**

Increase SIP or reduce discretionary spending.
""")

        else:

            st.success("""
### 💰 Savings

Excellent savings habit.

Keep maintaining consistency.
""")

    # ---------------- CARD 2 ---------------- #

    with c2:

        if income > 0 and monthly_emi / income > 0.40:

            st.error("""
### 🏦 EMI

High EMI Burden

Avoid taking additional loans.

Focus on debt reduction.
""")

        else:

            st.success("""
### 🏦 EMI

Healthy EMI Ratio

Current debt level is safe.
""")

    # ---------------- CARD 3 ---------------- #

    with c3:

        if income > 0 and expenses / income > 0.70:

            st.warning("""
### 📊 Spending

Monthly spending is increasing.

Review subscriptions.

Reduce unnecessary purchases.

Potential Monthly Saving:

₹2,000+
""")

        else:

            st.success("""
### 📊 Spending

Excellent spending discipline.

Keep following your current budget.
""")