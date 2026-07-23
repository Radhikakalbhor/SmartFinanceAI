# components/chatbot.py

import streamlit as st
from utils.gemini import ask_gemini


def render_chatbot(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
    goal_progress
):

    # =====================================================
    # TITLE
    # =====================================================

    st.markdown("## 🤖 SmartFinance AI Copilot")

    st.caption("Powered by OpenRouter AI")

    # =====================================================
    # INITIALIZE CHAT HISTORY
    # =====================================================

    if "dashboard_chat_messages" not in st.session_state:
        st.session_state.dashboard_chat_messages = []

    # =====================================================
    # HEADER + CLEAR BUTTON
    # =====================================================

    title_col, clear_col = st.columns([4, 1])

    with title_col:
        st.markdown("### 💬 AI Conversation")

    with clear_col:

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True,
            key="clear_dashboard_chat"
        ):

            st.session_state.dashboard_chat_messages = []

            st.rerun()

    # =====================================================
    # SUGGESTED QUESTIONS
    # =====================================================

    st.markdown("### 💡 Suggested Questions")

    q1, q2 = st.columns(2)

    with q1:

        if st.button(
            "💰 How can I save more money?",
            use_container_width=True,
            key="save_more_question"
        ):
            st.session_state.dashboard_prompt = (
                "How can I save more money?"
            )

        if st.button(
            "📈 Should I increase my SIP?",
            use_container_width=True,
            key="sip_question"
        ):
            st.session_state.dashboard_prompt = (
                "Should I increase my SIP?"
            )

    with q2:

        if st.button(
            "🏦 Is my EMI healthy?",
            use_container_width=True,
            key="emi_question"
        ):
            st.session_state.dashboard_prompt = (
                "Is my EMI healthy?"
            )

        if st.button(
            "📊 Analyze my finances",
            use_container_width=True,
            key="finance_question"
        ):
            st.session_state.dashboard_prompt = (
                "Analyze my finances."
            )

    st.write("")

    # =====================================================
    # DISPLAY COMPLETE CONVERSATION HISTORY
    # =====================================================

    for message in st.session_state.dashboard_chat_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # =====================================================
    # CHAT INPUT
    # =====================================================

    question = st.chat_input(
        "Ask SmartFinance AI anything...",
        key="dashboard_chat_input"
    )

    # =====================================================
    # HANDLE SUGGESTED QUESTION
    # =====================================================

    suggested_question = st.session_state.pop(
        "dashboard_prompt",
        None
    )

    if not question and suggested_question:

        question = suggested_question

    # =====================================================
    # PROCESS QUESTION
    # =====================================================

    if question:

        # -------------------------------------------------
        # SAVE USER QUESTION
        # -------------------------------------------------

        st.session_state.dashboard_chat_messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        # Display current question immediately

        with st.chat_message("user"):

            st.markdown(question)

        # -------------------------------------------------
        # CREATE FINANCIAL CONTEXT
        # -------------------------------------------------

        prompt = f"""
You are SmartFinance AI, an intelligent Personal Financial Assistant.

The user's current financial information is:

Monthly Income: ₹{income:,.2f}
Monthly Expenses: ₹{expenses:,.2f}
Current Savings: ₹{savings:,.2f}
Monthly SIP: ₹{monthly_sip:,.2f}
Monthly EMI: ₹{monthly_emi:,.2f}
Savings Goal Progress: {goal_progress:.1f}%

INSTRUCTIONS:

1. Answer only in English.
2. Do not use Hindi, Urdu, Arabic or any other language.
3. Give practical and beginner-friendly financial guidance.
4. Use bullet points when useful.
5. Use Indian Rupees (₹) when discussing money.
6. Mention calculations and numbers whenever appropriate.
7. Keep the answer concise but informative.
8. Do not guarantee investment returns.
9. For investments, mention market risk whenever relevant.
10. Use the user's financial information when it is relevant to the question.

USER QUESTION:

{question}
"""

        # -------------------------------------------------
        # GET AI RESPONSE
        # -------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner(
                "🤖 SmartFinance AI is analyzing..."
            ):

                try:

                    answer = ask_gemini(prompt)

                except Exception as e:

                    answer = (
                        "⚠️ SmartFinance AI could not "
                        "generate a response.\n\n"
                        f"Error: {e}"
                    )

            st.markdown(answer)

        # -------------------------------------------------
        # SAVE AI RESPONSE
        # -------------------------------------------------

        st.session_state.dashboard_chat_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )