import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 0 - Getting up to speed with Streamlit", page_icon="📖")

load_css()

md = read_md('Lesson-0.md')
st.markdown(md, unsafe_allow_html=True)


st.header('Examples')

st.subheader('st.text_input()')
col1, col2 = st.columns(2)
with col1:
  st.markdown('### Code')
  st.code('''
    import streamlit as st

    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)
  ''')
with col2:
  st.markdown('### App')
  title = st.text_input('Movie title', 'Life of Brian')
  st.write('The current movie title is', title)
