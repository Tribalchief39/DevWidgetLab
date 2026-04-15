import streamlit as st
import random

st.set_page_config(layout="wide")

# ---------------------------
# SESSION STATE
# ---------------------------
if "sections" not in st.session_state:
    st.session_state.sections = ["Deals", "Electronics"]

# ---------------------------
# SIDEBAR CONTROLS
# ---------------------------
st.sidebar.title("DevWidget Lab")

cols = st.sidebar.slider("Columns", 2, 6, 4)
nav_bg = st.sidebar.color_picker("Navbar BG", "#131921")
nav_text = st.sidebar.color_picker("Navbar Text", "#ffffff")
search_text = st.sidebar.text_input("Search Placeholder", "Search DevWidget")
btn_color = st.sidebar.color_picker("Button Color", "#febd69")
hero_text = st.sidebar.text_input("Hero Text", "Big Sale 🔥")
card_bg = st.sidebar.color_picker("Card BG", "#ffffff")

# ---------------------------
# SECTION BUILDER
# ---------------------------
st.sidebar.subheader("🧩 Sections")

new_sections = []
for i, sec in enumerate(st.session_state.sections):
    col1, col2, col3, col4 = st.sidebar.columns([3,1,1,1])

    new_val = col1.text_input(f"Section {i}", sec, key=f"sec_{i}")
    
    if col2.button("↑", key=f"up_{i}") and i > 0:
        st.session_state.sections[i], st.session_state.sections[i-1] = st.session_state.sections[i-1], st.session_state.sections[i]
    
    if col3.button("↓", key=f"down_{i}") and i < len(st.session_state.sections)-1:
        st.session_state.sections[i], st.session_state.sections[i+1] = st.session_state.sections[i+1], st.session_state.sections[i]
    
    if col4.button("❌", key=f"del_{i}"):
        st.session_state.sections.pop(i)
        st.rerun()

    new_sections.append(new_val)

st.session_state.sections = new_sections

if st.sidebar.button("➕ Add Section"):
    st.session_state.sections.append("New Section")
    st.rerun()

# ---------------------------
# PRODUCTS FUNCTION
# ---------------------------
def products_html(cols, card_bg):
    html = f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:15px;">'
    for i in range(8):
        html += f"""
        <div style="background:{card_bg};padding:10px;border-radius:14px;">
            <img src="https://picsum.photos/200?{i}" style="width:100%;height:150px;object-fit:cover;">
            <p>Product {i+1}</p>
            <b>₹{random.randint(100,999)}</b>
        </div>
        """
    html += "</div>"
    return html

# ---------------------------
# GENERATE HTML
# ---------------------------
sections_html = ""
for sec in st.session_state.sections:
    sections_html += f"""
    <div style="margin:20px;background:white;padding:15px;border-radius:16px;">
        <h2>{sec}</h2>
        {products_html(cols, card_bg)}
    </div>
    """

html_code = f"""
<html>
<body style="margin:0;font-family:sans-serif;background:#eaeded;">

<div style="background:{nav_bg};color:{nav_text};padding:10px;display:flex;gap:15px;">
<b>DevWidget Lab</b>

<div style="flex:1;display:flex;">
<input placeholder="{search_text}" style="flex:1;padding:8px;">
<button style="background:{btn_color};padding:8px;">🔍</button>
</div>

<div>Account</div>
<div>Cart</div>
</div>

<div style="height:300px;position:relative;">
<img src="https://picsum.photos/1200/300" style="width:100%;height:100%;object-fit:cover;">
<h1 style="position:absolute;bottom:20px;left:20px;color:white;">{hero_text}</h1>
</div>

{sections_html}

</body>
</html>
"""

# ---------------------------
# UI LAYOUT
# ---------------------------
col1, col2 = st.columns([2,1])

with col1:
    st.subheader("🖥️ Live Preview")
    st.components.v1.html(html_code, height=700, scrolling=True)

with col2:
    st.subheader("📄 Generated Code")
    st.code(html_code, language="html")
