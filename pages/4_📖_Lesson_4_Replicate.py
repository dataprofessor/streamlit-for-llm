import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Lesson 4 - Using hosted open source LLM models from Replicate", page_icon="📖")

load_css()
md = read_md('Lesson-4.md')
st.markdown(md, unsafe_allow_html=True)
