import streamlit as st

from components.header import render_header
from services.interview_service import evaluate_interview


def render_interview():

    render_header(
        "🎤 Interview Coach",
        "Practice technical and HR interviews with AI."
    )
    
    session = evaluate_interview()

    # ---------- Interview Setup ----------

    with st.container(border=True):

        st.subheader("⚙️ Interview Setup")

        col1, col2 = st.columns(2)

        with col1:
            st.selectbox(
                "Interview Type",
                [
                    "Technical",
                    "HR",
                    "Behavioral",
                    "System Design",
                ],
            )

        with col2:
            st.selectbox(
                "Difficulty",
                [
                    "Easy",
                    "Medium",
                    "Hard",
                ],
            )

    st.write("")

    # ---------- Question ----------

    with st.container(border=True):

        st.subheader("❓ Interview Question")

        st.write(session.question)

    st.write("")

    # ---------- Answer ----------

    with st.container(border=True):

        st.subheader("✍️ Your Answer")

        st.text_area(
            "Type your answer here...",
            height=180,
        )

    st.write("")

    # ---------- Feedback ----------

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📊 Evaluation")

            st.metric("Interview Score", session.score)

    with col2:

        with st.container(border=True):

            st.subheader("🤖 AI Feedback")

            for item in session.feedback:
                st.write(f"💬 {item}")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "▶️ Start Interview",
            use_container_width=True,
        )

    with col2:

        st.button(
            "📝 Evaluate Answer",
            use_container_width=True,
        )