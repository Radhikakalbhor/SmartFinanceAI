import streamlit as st
from datetime import datetime


def render_footer(health):

    st.markdown("---")

    # ==========================================================
    # DASHBOARD STATUS
    # ==========================================================

    st.markdown("## ⚡ Dashboard Status")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🟢 AI Engine Online")

    with c2:
        st.success("📊 Financial Data Loaded")

    with c3:
        st.success("🔒 Secure Session")

    st.write("")

    # ==========================================================
    # AI TIMELINE
    # ==========================================================

    st.markdown("## 🤖 AI Activity Timeline")

    current = datetime.now().strftime("%I:%M %p")

    timeline = [

        ("📂", "Financial history loaded"),

        ("📊", "Analytics generated"),

        ("🧠", "AI recommendations updated"),

        ("💬", "AI Assistant ready"),

        ("❤️", f"Financial Health : {health}/100")

    ]

    for icon, text in timeline:

        st.markdown(
            f"""
<div style="
background:rgba(255,255,255,.04);
padding:12px;
border-radius:12px;
margin-bottom:10px;
border-left:4px solid #3B82F6;
">
<b>{current}</b><br>
{icon} {text}
</div>
""",
            unsafe_allow_html=True
        )

    st.write("")

    # ==========================================================
    # SMART FINANCE TIPS
    # ==========================================================

    st.markdown("## 💡 Smart Finance Tips")

    tips = [

        "Save at least 20% of your monthly income.",

        "Keep your EMI below 40% of income.",

        "Review subscriptions every month.",

        "Invest consistently through SIP.",

        "Maintain an emergency fund.",

        "Track your expenses weekly.",

        "Avoid impulse purchases."

    ]

    for tip in tips:

        st.info(tip)

    st.write("")

    # ==========================================================
# DEVELOPER
# ==========================================================

    # ==========================================================
    # DEVELOPER
    # ==========================================================

    st.markdown("## 👩‍💻 Developer")

    st.markdown("""
<div style="
background:linear-gradient(135deg,#111827,#1E293B);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,.08);
color:white;
">

<h2 style="margin-bottom:15px; color:white;">
👩‍💻 Radhika Kalbhor
</h2>

<p style="font-size:17px; color:#E5E7EB; margin:6px 0;">
<b>Information Technology</b>
</p>

<p style="font-size:16px; color:#D1D5DB; margin:6px 0;">
Shah & Anchor Kutchhi Engineering College
</p>

<p style="font-size:16px; color:#60A5FA; margin:6px 0;">
SmartFinance AI
</p>

<p style="font-size:16px; color:#F9FAFB; margin:6px 0;">
LLM-Based Personal Financial Assistant
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    # ==========================================================
    # FOOTER
    # ==========================================================

    st.markdown("---")

    st.markdown(
        """
<div style="
text-align:center;
padding:30px;
">

<h2 style="color:#60A5FA;">
🤖 SmartFinance AI
</h2>

<p>
AI Powered Personal Financial Assistant
</p>

<p>
Built using

Python • Streamlit • Plotly • OpenRouter AI
</p>

</div>
""",
        unsafe_allow_html=True
    )

    st.caption(
        "© 2026 SmartFinance AI | Empowering Smarter Financial Decisions"
    )