import streamlit as st

st.set_page_config(page_title="X-ray Analyzer", page_icon="./app/static/logo.jpg", layout="wide", menu_items={
    })
st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

with open("static/base.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
st.markdown("""this is the documentation page""")