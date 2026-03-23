import streamlit as st

st.set_page_config(page_title="Button Generator", layout="wide")

st.title("CSS Button Generator")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Controls")

    button_text = st.text_input("Button Text", "Click Me")

    bg_color = st.color_picker("Background Color", "#38bdf8")
    text_color = st.color_picker("Text Color", "#000000")

    radius = st.slider("Border Radius", 0, 50, 10)
    padding = st.slider("Padding", 5, 30, 12)

    hover_color = st.color_picker("Hover Color", "#0ea5e9")

with col2:
    st.subheader("Preview")

    button_css = f"""
    <style>
    .custom-btn {{
        background-color: {bg_color};
        color: {text_color};
        border: none;
        border-radius: {radius}px;
        padding: {padding}px {padding*2}px;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
    }}

    .custom-btn:hover {{
        background-color: {hover_color};
    }}
    </style>
    """

    st.markdown(button_css, unsafe_allow_html=True)

    st.markdown(
        f'<button class="custom-btn">{button_text}</button>',
        unsafe_allow_html=True
    )

    css_code = f"""
.custom-btn {{
  background-color: {bg_color};
  color: {text_color};
  border-radius: {radius}px;
  padding: {padding}px {padding*2}px;
  border: none;
  cursor: pointer;
}}

.custom-btn:hover {{
  background-color: {hover_color};
}}
"""

    st.code(css_code, language="css")

    st.download_button(
        "Download CSS",
        css_code,
        file_name="button_style.css"
    )