import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 2 - Using LLM models from OpenAI", page_icon="📖", layout="wide")

load_css()

md = read_md('Lesson-2.md')
st.markdown(md, unsafe_allow_html=True)
