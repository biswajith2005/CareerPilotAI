import streamlit as st


def render_header(title: str, subtitle: str = ""):
    """Simple reusable page header."""

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()