import streamlit as st
import pandas as pd
import plotly.express as px


def render_charts(income, expenses, savings, health):

    st.markdown("## 📊 Financial Analytics")

    chart_col, ai_col = st.columns([3, 1])

    # =====================================================
    # LEFT SIDE (CHARTS)
    # =====================================================

    with chart_col:

        col1, col2 = st.columns(2)

        # ---------------- Expense Distribution ---------------- #

        with col1:

            st.markdown("### 💸 Expense Distribution")

            if income > 0:

                pie_data = pd.DataFrame({
                    "Category": ["Expenses", "Savings"],
                    "Amount": [expenses, savings]
                })

                fig = px.pie(
                    pie_data,
                    names="Category",
                    values="Amount",
                    hole=0.65,
                    color="Category",
                    color_discrete_sequence=[
                        "#EF4444",
                        "#10B981"
                    ]
                )

                fig.update_traces(
                    textinfo="percent+label",
                    textposition="inside",
                    marker=dict(
                        line=dict(
                            color="#0F172A",
                            width=3
                        )
                    )
                )

                fig.update_layout(

                    paper_bgcolor="rgba(0,0,0,0)",

                    plot_bgcolor="rgba(0,0,0,0)",

                    font=dict(
                        color="white"
                    ),

                    margin=dict(
                        l=10,
                        r=10,
                        t=20,
                        b=20
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No financial data available.")

        # ---------------- Financial Overview ---------------- #

        with col2:

            st.markdown("### 📈 Financial Overview")

            if income > 0:

                df = pd.DataFrame({

                    "Category": [
                        "Income",
                        "Expenses",
                        "Savings"
                    ],

                    "Amount": [
                        income,
                        expenses,
                        savings
                    ]
                })

                fig = px.bar(

                    df,

                    x="Category",

                    y="Amount",

                    color="Category",

                    text="Amount",

                    color_discrete_sequence=[
                        "#3B82F6",
                        "#EF4444",
                        "#10B981"
                    ]
                )

                fig.update_traces(

                    texttemplate="₹%{y:,.0f}",

                    textposition="outside"

                )

                fig.update_layout(

                    paper_bgcolor="rgba(0,0,0,0)",

                    plot_bgcolor="rgba(0,0,0,0)",

                    font=dict(color="white"),

                    xaxis=dict(showgrid=False),

                    yaxis=dict(
                        gridcolor="rgba(255,255,255,.08)"
                    ),

                    margin=dict(
                        l=10,
                        r=10,
                        t=20,
                        b=20
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No financial data available.")

    # =====================================================
    # RIGHT SIDE (AI PANEL)
    # =====================================================

    with ai_col:

        st.markdown("### 🤖 AI Copilot")

        st.metric(
            "Financial Health",
            f"{health}/100"
        )

        if health >= 90:

            st.success("Excellent")

        elif health >= 75:

            st.warning("Good")

        else:

            st.error("Needs Attention")

        st.markdown("---")

        st.markdown("### 🧠 AI Insights")

        if income == 0:

            st.info(
                "Add your budget to unlock personalized insights."
            )

        else:

            savings_rate = (savings / income) * 100

            expense_rate = (expenses / income) * 100

            st.write(
                f"💰 Savings Rate: **{savings_rate:.1f}%**"
            )

            st.write(
                f"💸 Expense Rate: **{expense_rate:.1f}%**"
            )

            if savings_rate >= 20:

                st.success(
                    "Excellent savings habit."
                )

            else:

                st.warning(
                    "Increase savings to at least 20%."
                )

        st.markdown("---")

        st.markdown("### ⚡ Today's Advice")

        if health >= 90:

            st.success(
                "Continue your SIP investments and maintain your current financial discipline."
            )

        elif health >= 75:

            st.info(
                "Reduce discretionary spending slightly to improve your financial score."
            )

        else:

            st.error(
                "Prioritize reducing expenses before taking on new investments."
            )