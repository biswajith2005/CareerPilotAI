import streamlit as st


import streamlit as st


def metric_card(
    title: str,
    value: str,
    subtitle: str = "",
    icon: str = "📊"
):
    """
    Reusable KPI Card
    """

    with st.container(border=True):

        col1, col2 = st.columns([1, 5])

        with col1:
            st.markdown(f"## {icon}")

        with col2:
            st.caption(title)
            st.subheader(value)

            if subtitle:
                st.caption(subtitle)