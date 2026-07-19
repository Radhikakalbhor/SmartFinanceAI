import streamlit as st
import pandas as pd
import os
from utils.history import load_history
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.sidebar.image("assets/logo.png", width=120)

st.sidebar.title("💰 SmartFinance AI")

st.sidebar.markdown("---")

st.sidebar.success("AI Powered Personal Finance Assistant")

st.sidebar.markdown("---")

st.sidebar.info("""
Developed By

**Radhika Kalbhor**

Department of Information Technology

SAKEC
""")

st.sidebar.image("assets/logo.png", width=120)
st.sidebar.title("💰 SmartFinance AI")

st.title("📜 Financial History Center")
st.write("View and manage all your saved financial calculations.")

st.markdown("---")

tabs = st.tabs([
    "💰 Budget",
    "📈 SIP",
    "🏦 EMI",
    "🎯 Savings"
])


def show_history(tab, filename, title):

    with tab:

        history = load_history(filename)

        if history.empty:
            st.info(f"No {title.lower()} history available.")
            return

        history = history.iloc[::-1].reset_index(drop=True)

        st.subheader(title)

        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        csv = history.to_csv(index=False)

        st.download_button(
            f"📥 Download {title}",
            csv,
            file_name=filename,
            mime="text/csv",
            key=f"download_{filename}"
        )

        st.markdown("---")

        c1, c2 = st.columns(2)

        c1.metric("📄 Total Records", len(history))
        c2.metric("🕒 Latest Entry", history.iloc[0]["Date"])

        st.markdown("---")

        if st.button(
            f"🗑 Clear {title}",
            key=f"clear_{filename}"
        ):

            filepath = os.path.join("data", filename)

            if os.path.exists(filepath):
                os.remove(filepath)

            st.success(f"{title} history cleared!")

            st.rerun()


show_history(
    tabs[0],
    "budget_history.csv",
    "Budget History"
)

show_history(
    tabs[1],
    "sip_history.csv",
    "SIP History"
)

show_history(
    tabs[2],
    "emi_history.csv",
    "EMI History"
)

show_history(
    tabs[3],
    "savings_history.csv",
    "Savings History"
)

st.markdown("---")

st.caption("SmartFinance AI | History Center")