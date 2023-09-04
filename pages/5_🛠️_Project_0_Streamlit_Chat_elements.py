import streamlit as st
import time
from utilities import load_css, read_md

st.set_page_config(page_title="Project 0 - Streamlit Chat elements", page_icon="🛠️", layout="wide")

load_css()

md = read_md('Project-0.md')
st.markdown(md, unsafe_allow_html=True)

st.divider()

st.subheader('st.chat_message()')
st.text('Insert a chat message container.')
col1, col2 = st.columns((3,2))
with col1:
    st.markdown('**Code**')
    st.code('''
      import streamlit as st
      import numpy as np

      with st.chat_message("user"):
        st.write("Hello 👋")
        st.line_chart(np.random.randn(30, 3))
    ''')
with col2:
    st.markdown('**App**')
    with st.chat_message("user"):
      st.write("Hello 👋")
      st.line_chart(np.random.randn(30, 3))
st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/chat/st.chat_message)')

st.divider()

st.subheader('st.status()')
st.text('Insert a status container to display output from long-running tasks.')
col1, col2 = st.columns((3,2))
with col1:
    st.markdown('**Code**')
    st.code('''
      import streamlit as st
      import time

      if st.button('Start'):
        with st.status("Downloading data..."):
          st.write("Searching for data...")
          time.sleep(2)
          st.write("Found URL.")
          time.sleep(1)
          st.write("Downloading data...")
          time.sleep(1)
    ''')
with col2:
    st.markdown('**App**')
    if st.button('Start'):
      with st.status("Downloading data..."):
        st.write("Searching for data...")
        time.sleep(2)
        st.write("Found URL.")
        time.sleep(1)
        st.write("Downloading data...")
        time.sleep(1)
st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/chat/st.chat_message)')

st.divider()

st.subheader('st.chat_input()')
st.text('Display a chat input widget.')

st.markdown('**Code**')
st.code('''
  import streamlit as st
  
  prompt = st.chat_input("Say something")
  if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
  ''')

st.markdown('**App**')
prompt = st.chat_input("Say something")

if prompt:
  st.write(f"User has sent the following prompt: {prompt}")

st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/chat/st.chat_input)')

