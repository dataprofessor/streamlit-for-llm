import streamlit as st
from PIL import Image
from utilities import load_css

st.set_page_config(
    page_title="Hello",
    page_icon="🏠",
)

img = Image.open('img/streamlit-generative-ai-course-logo.png')
st.image(img)

# About
st.header('About')
st.write('The Streamlit for Generative AI course will show you how to use Streamlit to build large language model (LLM) powered apps. Finally you can deploy the Streamlit app to the cloud and share with the community.')



load_css()
