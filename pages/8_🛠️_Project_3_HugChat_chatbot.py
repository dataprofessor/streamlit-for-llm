import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Project 3 - Build a HugChat chatbot", page_icon="🛠️")

load_css()

md = read_md('Project-3.md')
st.markdown(md, unsafe_allow_html=True)
