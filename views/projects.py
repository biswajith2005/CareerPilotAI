import streamlit as st

from components.header import render_header
from services.project_service import analyze_project


def render_projects():

    render_header(
        "💼 Project Analyzer",
        "Analyze your projects and GitHub portfolio."
    )

    analysis = analyze_project()

    # ---------- GitHub Input ----------

    with st.container(border=True):

        st.subheader("🔗 GitHub Repository")

        st.text_input(
            "Repository URL",
            placeholder="https://github.com/username/project"
        )

    st.write("")

    # ---------- Analysis ----------

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("⭐ Project Score")

            st.metric("Project Score", analysis.project_score)

    with col2:

        with st.container(border=True):

            st.subheader("📊 Complexity")

            st.write(analysis.complexity)

    st.write("")

    # ---------- Strengths ----------

    with st.container(border=True):

        st.subheader("✅ Strengths")

        for item in analysis.strengths:
            st.write(f"✅ {item}")

    st.write("")

    # ---------- Weaknesses ----------

    with st.container(border=True):

        st.subheader("⚠️ Weaknesses")

        for item in analysis.weaknesses:
            st.write(f"⚠️ {item}")

    st.write("")

    # ---------- Recommendations ----------

    with st.container(border=True):

        st.subheader("💡 AI Recommendations")

        for item in analysis.recommendations:
            st.write(f"💡 {item}")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "🚀 Analyze Project",
            use_container_width=True,
        )

    with col2:

        st.button(
            "📄 Generate Report",
            use_container_width=True,
        )