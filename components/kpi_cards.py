import streamlit as st


def render_kpis(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    health
):

    st.markdown("## 📊 Financial Snapshot")

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "💰 Monthly Income",
            f"₹{income:,.0f}"
        )

    with c2:
        st.metric(
            "💸 Monthly Expenses",
            f"₹{expenses:,.0f}"
        )

    with c3:
        st.metric(
            "💵 Total Savings",
            f"₹{savings:,.0f}"
        )

    st.write("")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "📈 Monthly SIP",
            f"₹{monthly_sip:,.0f}"
        )

    with c5:
        st.metric(
            "🏦 Monthly EMI",
            f"₹{monthly_emi:,.0f}"
        )

    with c6:
        st.metric(
            "❤️ Financial Health",
            f"{health}/100"
        )

    st.write("")

    st.markdown("### ⚡ Live Dashboard Status")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.success("💰 Income Loaded")

    with s2:
        st.success("📈 Analytics Ready")

    with s3:
        st.success("🤖 AI Online")

    with s4:
        st.success("🔒 Secure Session")

    st.write("")
    st.markdown("---")