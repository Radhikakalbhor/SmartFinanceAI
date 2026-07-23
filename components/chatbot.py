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

    st.markdown("## 🤖 SmartFinance AI Copilot")

    st.caption("Powered by OpenRouter AI")

    # ---------------------------------------
    # Suggested Questions
    # ---------------------------------------

    st.markdown("### 💡 Suggested Questions")

    q1, q2 = st.columns(2)

    with q1:

        if st.button(
            "💰 How can I save more money?",
            use_container_width=True
        ):
            st.session_state["prompt"] = (
                "How can I save more money?"
            )

        if st.button(
            "📈 Should I increase my SIP?",
            use_container_width=True
        ):
            st.session_state["prompt"] = (
                "Should I increase my SIP?"
            )

    with q2:

        if st.button(
            "🏦 Is my EMI healthy?",
            use_container_width=True
        ):
            st.session_state["prompt"] = (
                "Is my EMI healthy?"
            )

        if st.button(
            "📊 Analyze my finances",
            use_container_width=True
        ):
            st.session_state["prompt"] = (
                "Analyze my finances."
            )

    st.write("")

    # ---------------------------------------
    # Conversation History
    # ---------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            st.markdown(msg["content"])

    # ---------------------------------------
    # User Input
    # ---------------------------------------

    default_prompt = st.session_state.get(
        "prompt",
        ""
    )

    question = st.chat_input(
        placeholder="Ask SmartFinance AI anything..."
    )

    if not question and default_prompt:
        question = default_prompt
        st.session_state["prompt"] = ""

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        prompt = f"""
You are SmartFinance AI.

User Financial Data

Income: ₹{income}

Expenses: ₹{expenses}

Savings: ₹{savings}

Monthly SIP: ₹{monthly_sip}

Monthly EMI: ₹{monthly_emi}

Savings Goal Progress: {goal_progress:.1f}%

Rules

1. Give practical advice.

2. Use bullet points.

3. Mention numbers whenever possible.

4. Keep answers concise.

User Question

{question}
"""

        with st.spinner(
            "🤖 SmartFinance AI is analyzing your finances..."
        ):

            try:

                answer = ask_gemini(prompt)

            except Exception as e:

                answer = (
                    "Unable to contact the AI model.\n\n"
                    f"Error: {e}"
                )

        with st.chat_message("assistant"):

            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )