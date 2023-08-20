import streamlit as st
from PIL import Image
from utilities import load_css

st.set_page_config(
    page_title="Hello",
    page_icon="🏠",
)

img = Image.open('img/streamlit-generative-ai-course-logo.png')
st.image(img)

st.markdown('''
<p align="center">
  <img src="./app/img/streamlit-generative-ai-course-logo.png" width="60%">
</p>
''', unsafe_allow_html=True)

st.metric(label="Active developers", value=123, delta=None)

st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet lacus nulla, vitae faucibus erat cursus ut. Nullam quam lorem, semper eu nulla sit amet, pharetra viverra mi. Donec suscipit ligula metus, nec venenatis orci pellentesque et. Quisque ac sem eros. Duis non tellus vel est dictum interdum. Nam pulvinar mattis rhoncus. In sit amet ante ut odio scelerisque ullamcorper. Aliquam hendrerit facilisis purus eu mollis. Maecenas iaculis eget turpis nec mollis.')

load_css()
