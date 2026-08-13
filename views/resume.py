import streamlit as st

from components.header import render_header
from services.resume_service import analyze_resume
from services.report_service import generate_resume_report


def render_resume():

    render_header(
        "📄 Resume Intelligence",
        "Analyze and optimize your resume with AI."
    )

    # ---------------- Session State ---------------- #

    if "resume_analysis" not in st.session_state:
        st.session_state.resume_analysis = None

    if "uploaded_resume_name" not in st.session_state:
        st.session_state.uploaded_resume_name = None
    
    analysis = st.session_state.resume_analysis

    # ---------------- Resume Upload ---------------- #

    with st.container(border=True):

        st.subheader("📤 Resume Upload")

        uploaded_resume = st.file_uploader(
            "Upload your Resume",
            type=["pdf", "docx"],
        )

        if uploaded_resume is not None:

            st.success(f"Selected: {uploaded_resume.name}")

            if st.session_state.uploaded_resume_name != uploaded_resume.name:

                st.session_state.resume_analysis = None
                st.session_state.uploaded_resume_name = uploaded_resume.name
    st.write("")

    # ---------------- Action Buttons ---------------- #

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True,
        ):

            if uploaded_resume is None:

                st.warning("Please upload a resume first.")

            else:

                try:

                    with st.spinner("Analyzing resume..."):

                        analysis = analyze_resume(uploaded_resume)

                    st.session_state.resume_analysis = analysis

                    st.rerun()

                except Exception as e:

                    message = str(e)

                    if "503" in message:
                        st.error("⚠️ Gemini is currently experiencing high demand. Please try again in a few moments.")

                    elif "404" in message:
                        st.error("⚠️ AI model is currently unavailable.")

                    elif "Invalid AI response" in message:
                        st.error("⚠️ AI returned an unexpected response. Please try again.")

                    else:
                        st.error("⚠️ Failed to analyze the resume. Please try again.")

    with col2:

        if analysis:

            pdf = generate_resume_report(analysis)

            st.download_button(
                label="📥 Export Report",
                data=pdf,
                file_name="CareerPilot_Resume_Report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

        else:

            st.button(
                "📥 Export Report",
                use_container_width=True,
                disabled=True,
            )

    st.write("")

    # ---------------- ATS + Skills ---------------- #

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📊 ATS Score")

            if analysis:

                st.metric("ATS Score", analysis.ats_score)

            else:

                st.metric("ATS Score", "--")

    with col2:

        with st.container(border=True):

            st.subheader("🎯 Skills Gap")

            if analysis:

                for item in analysis.weaknesses:
                    st.write(f"• {item}")

            else:

                st.info("No analysis available.")

    st.write("")

    # ---------------- AI Analysis ---------------- #

    with st.container(border=True):

        st.subheader("🤖 AI Resume Analysis")

        if analysis:

            for item in analysis.strengths:
                st.write(f"✅ {item}")

        else:

            st.info("Upload a resume and click Analyze Resume.")

    st.write("")

    # ---------------- Suggestions ---------------- #

    with st.container(border=True):

        st.subheader("💡 Improvement Suggestions")

        if analysis:

            for item in analysis.suggestions:
                st.write(f"💡 {item}")

        else:

            st.info("Suggestions will appear after analysis.")