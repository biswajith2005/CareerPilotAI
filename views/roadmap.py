import streamlit as st

from components.header import render_header
from services.roadmap_service import generate_roadmap


def render_roadmap():

    render_header(
        "🗺️ Career Roadmap",
        "Generate a personalized learning roadmap."
    )

    roadmap = generate_roadmap()

    # ---------- Target Role ----------

    with st.container(border=True):

        st.subheader("🎯 Target Role")

        st.selectbox(
            "Choose your target role",
            [
                "Software Engineer",
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "AI/ML Engineer",
                "Data Scientist",
            ],
        )

    st.write("")

    # ---------- Roadmap ----------

    with st.container(border=True):

        st.subheader("🛣️ Learning Roadmap")

        for milestone in roadmap.milestones:
            st.write(f"✅ {milestone}")

    st.write("")

    # ---------- Skills ----------

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📚 Skills to Learn")

            for skill in roadmap.skills:
                st.write(f"📘 {skill}")

    with col2:

        with st.container(border=True):

            st.subheader("⏳ Estimated Timeline")

            st.metric("Duration", roadmap.duration)

    st.write("")

    # ---------- Progress ----------

    with st.container(border=True):

        st.subheader("📈 Progress Tracker")

        st.progress(0)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "🚀 Generate Roadmap",
            use_container_width=True,
        )

    with col2:

        st.button(
            "💾 Save Roadmap",
            use_container_width=True,
        )