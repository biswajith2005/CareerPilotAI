import streamlit as st


def render_sidebar():
    """Render the CareerPilot AI sidebar."""

    with st.sidebar:

        # ---------- Brand ----------

        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-brand-name">🚀 CareerPilot AI</div>
                <div class="sidebar-brand-subtitle">
                    AI Career Operating System
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # ---------- Navigation ----------

        st.markdown(
            '<div class="sidebar-section-title">Navigation</div>',
            unsafe_allow_html=True,
        )

        navigation = [
         "🏠 Dashboard",
        "📄 Resume Intelligence",
        "💼 Project Analyzer",
        "🗺️ Career Roadmap",
        "🎤 Interview Coach",
        ]

        selected_page = st.radio(
    "",
    navigation,
    label_visibility="collapsed",
)

    return selected_page