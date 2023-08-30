import streamlit as st
from utilities import load_css


st.set_page_config(page_title="Lesson 3 - Using open source LLM models from Hugging Face Hub", page_icon="📖")
#st.header("📖 Lesson 3 - Using open source LLM models from Hugging Face Hub")

#####
import requests

img_url_path = 'https://github.com/dataprofessor/streamlit-for-generative-ai/blob/master'
img_url_suffix = '?raw=true'

md_url_path = 'https://raw.githubusercontent.com/dataprofessor/streamlit-for-generative-ai/master/content'
md_lesson_url = f'{md_url_path}/Lesson-3.md'
response = requests.get(md_lesson_url)
content = response.text
content = content.replace('<img src="..', f'<img src="..{img_url_path}').replace('" width', f'{img_url_suffix}" width')

st.markdown(content, unsafe_allow_html=True)

load_css()
