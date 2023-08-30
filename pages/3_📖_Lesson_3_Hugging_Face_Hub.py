import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 3 - Using open source LLM models from Hugging Face Hub", page_icon="📖")

load_css()
md = read_md('Lesson-3.md')
st.markdown(md, unsafe_allow_html=True)
