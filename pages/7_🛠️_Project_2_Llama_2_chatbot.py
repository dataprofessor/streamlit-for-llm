import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Project 2 - Build a Llama 2 chatbot", page_icon="🛠️")

load_css()

md = read_md('Project-2.md')
st.markdown(md, unsafe_allow_html=True)
