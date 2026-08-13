import streamlit as st

from components.cards import metric_card
from components.dashboard_hero import render_dashboard_hero

def render_dashboard():
    """Render the Mission Control Dashboard."""

    render_dashboard_hero()

    
    # ---------- Main Dashboard ----------

    left, right = st.columns([2, 1])

    with left:

        with st.container(border=True):

            st.subheader("🎯 Today's Mission")

        task1 = st.checkbox(
            "Solve 2 LeetCode Problems",
            value=True
        )

        task2 = st.checkbox(
            "Improve Resume Summary"
        )

        task3 = st.checkbox(
            "Apply to 2 Companies"
        )

        completed = sum([task1, task2, task3])

        progress = completed / 3

        st.progress(progress)

        st.caption(
            f"{completed}/3 tasks completed"
        )
    with right:

        with st.container(border=True):

            st.subheader("🤖 AI Recommendation")

            st.write(
                "Your resume is strong, but your projects need more measurable impact."
            )

            st.info("Priority: Improve Project Portfolio")

    st.write("")

    # ---------- Progress ----------

    with st.container(border=True):

        st.subheader("📈 Career Progress")

        st.line_chart(
            {
                "Career Score": [60, 65, 69, 72, 78, 82]
            }
        )

    st.write("")


    # ---------- Quick Actions ----------

    with st.container(border=True):

        st.subheader("⚡ Quick Actions")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "📄 Analyze Resume",
                use_container_width=True,
                key="quick_resume",
            ):
                st.session_state.selected_page = "📄 Resume Intelligence"
                st.rerun()

            if st.button(
                "🗺️ Generate Roadmap",
                use_container_width=True,
                key="quick_roadmap",
            ):
                st.session_state.selected_page = "🗺️ Career Roadmap"
                st.rerun()

        with col2:

            if st.button(
                "💼 Analyze Projects",
                use_container_width=True,
                key="quick_projects",
            ):
                st.session_state.selected_page = "💼 Project Analyzer"
                st.rerun()

            if st.button(
                "🎤 Mock Interview",
                use_container_width=True,
                key="quick_interview",
            ):
                st.session_state.selected_page = "🎤 Interview Coach"
                st.rerun()