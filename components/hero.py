import streamlit as st


def render_hero(health, income, expenses, savings):

    # ---------------- STATUS ---------------- #

    if health >= 90:
        status = "Excellent"
        color = "#22C55E"
        icon = "🟢"
        message = "Your financial health is excellent. Keep investing consistently."

    elif health >= 75:
        status = "Good"
        color = "#FACC15"
        icon = "🟡"
        message = "You're doing well. Small improvements can make your finances even stronger."

    else:
        status = "Needs Attention"
        color = "#EF4444"
        icon = "🔴"
        message = "Your spending pattern needs attention. Let's improve it together."

    # ---------------- HERO ---------------- #

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#0F172A,#111827,#1E293B);
padding:35px;
border-radius:24px;
border:1px solid rgba(255,255,255,.08);
box-shadow:0 10px 35px rgba(0,0,0,.35);
margin-bottom:25px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<h1 style="color:white;margin-bottom:10px;">
🤖 SmartFinance AI Copilot
</h1>

<p style="font-size:19px;color:#CBD5E1;">
Welcome back!
</p>

<p style="font-size:17px;color:#94A3B8;">
I've analyzed your latest financial activity.
</p>

</div>

<div style="
background:{color};
padding:12px 22px;
border-radius:14px;
font-size:18px;
font-weight:bold;
color:white;
">

AI ONLINE

</div>

</div>

<hr style="border:1px solid rgba(255,255,255,.08);">

<h2 style="color:white;">
❤️ Financial Health : {health}/100
</h2>

<p style="font-size:20px;color:{color};font-weight:bold;">
{icon} {status}
</p>

<p style="font-size:17px;color:#CBD5E1;">
{message}
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    # ---------------- KPI ROW ---------------- #

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "💰 Income",
            f"₹{income:,.0f}"
        )

    with c2:
        st.metric(
            "💸 Expenses",
            f"₹{expenses:,.0f}"
        )

    with c3:
        st.metric(
            "💵 Savings",
            f"₹{savings:,.0f}"
        )

    with c4:
        st.metric(
            "❤️ Health",
            f"{health}/100"
        )

    st.write("")

    left, right = st.columns([3,1])

    with left:

        st.info(
"""
🤖 **AI Daily Brief**

• Income successfully loaded.

• Expense analysis completed.

• Savings evaluated.

• Financial score calculated.

• AI recommendations are ready.

• Ask SmartFinance AI anything below.
"""
        )

    with right:

        st.metric(
            "AI Confidence",
            "98%"
        )

        st.metric(
            "Risk",
            "Low"
        )