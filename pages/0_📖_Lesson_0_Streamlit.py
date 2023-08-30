import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 0 - Getting up to speed with Streamlit", page_icon="📖")

load_css()

md = read_md('Lesson-00.md')
st.markdown(md, unsafe_allow_html=True)
