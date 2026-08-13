from pathlib import Path
import streamlit as st


def load_css():
    """
    Loads every css file inside assets/css
    """

    css_folder = Path("assets/css")

    css_files = [
        "theme.css",
        "layout.css",
        "components.css",
        "animations.css",
        "dashboard.css",
    ]

    css = ""

    for file in css_files:
        path = css_folder / file

        if path.exists():
            css += path.read_text(encoding="utf-8")

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )