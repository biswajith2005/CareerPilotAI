import streamlit as st
from utils.ui import load_css
from components.cards import metric_card
from views.dashboard import render_dashboard
from views.resume import render_resume
from views.projects import render_projects
from views.roadmap import render_roadmap
from views.interview import render_interview

from components.sidebar import render_sidebar

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
)

load_css()

selected_page = render_sidebar()

if selected_page == "🏠 Dashboard":
    render_dashboard()

elif selected_page == "📄 Resume Intelligence":
    render_resume()

elif selected_page == "💼 Project Analyzer":
    render_projects()

elif selected_page == "🗺️ Career Roadmap":
    render_roadmap()

elif selected_page == "🎤 Interview Coach":
    render_interview()