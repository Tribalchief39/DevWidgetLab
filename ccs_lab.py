import streamlit as st

st.set_page_config(page_title="CSS Visual Lab", layout="wide")

st.title("CSS Visual Lab")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Controls")

    radius = st.slider("Border Radius", 0, 50, 12)
    shadow = st.slider("Box Shadow Blur", 0, 40, 15)
    opacity = st.slider("Opacity", 0.1, 1.0, 1.0, step=0.1)
    bg_color = st.color_picker("Background Color", "#38bdf8")

with col2:
    st.subheader("Preview")

    # CSS for preview card
    card_css = f"""
    <style>
    .card {{
        width:250px;
        height:150px;
        margin:auto;
        display:flex;
        align-items:center;
        justify-content:center;
        font-weight:bold;
        color:#020617;
        border-radius:{radius}px;
        box-shadow:0px 10px {shadow}px rgba(0,0,0,0.3);
        opacity:{opacity};
        background-color:{bg_color};
    }}
    </style>
    """

    st.markdown(card_css, unsafe_allow_html=True)

    st.markdown('<div class="card">Preview Card</div>', unsafe_allow_html=True)

    css_code = f"""
.card {{
  border-radius: {radius}px;
  box-shadow: 0px 10px {shadow}px rgba(0,0,0,0.3);
  opacity: {opacity};
  background-color: {bg_color};
}}
"""

    st.code(css_code, language="css")

    st.download_button(
        label="Download CSS",
        data=css_code,
        file_name="styles.css",
        mime="text/css"
    )