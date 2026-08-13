import streamlit as st


def render_dashboard_hero():
    """Render the dashboard hero section with welcome message and stats."""
    
    with st.container(border=True):
        st.markdown("## 👋 Welcome Back")
        st.markdown("**AI Career Operating System**")
        
        st.divider()
        
        st.markdown("### 🚀 You're 82% Interview Ready")
        st.caption(
    "Complete today's mission to improve your career score and stay ahead of your placement goals."
)
        
        st.divider()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("🎯 Career", "82")
        
        with col2:
             st.metric("📄 Resume", "89%")
        
        with col3:
            st.metric("💼 Projects", "5")
        
        with col4:
            st.metric("🔥 Streak", "7 Days")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            st.button(
        "📄 Analyze Resume",
        use_container_width=True,
        key="hero_resume",
    )

        with col2:
            st.button(
         "🎤 Start Interview",
        use_container_width=True,
        key="hero_interview",
    )