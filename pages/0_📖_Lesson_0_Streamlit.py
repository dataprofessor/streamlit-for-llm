import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 0 - Getting up to speed with Streamlit", page_icon="📖", layout="wide")

load_css()

md = read_md('Lesson-0.md')
st.markdown(md, unsafe_allow_html=True)

st.divider()
st.header('Examples')
st.warning('''
  Below you will see the code snippet to the left and the corresponding widget in app to the right. 
  
  Go ahead and interact with the widget and see its responsive output.
''')

st.subheader('st.text_input()')
col1, col2 = st.columns((2,1))
st.text('Display a single-line text input widget.')
with col1:
  st.markdown('**Code**')
  st.code('''
    import streamlit as st

    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)
  ''')
with col2:
  st.markdown('**App**')
  title = st.text_input('Movie title', 'Life of Brian')
  st.write('The current movie title is', title)


st.subheader('st.number_input()')
st.text('Display a numeric input widget.')
col1, col2 = st.columns((2,1))
with col1:
  st.markdown('**Code**')
  st.code('''
    import streamlit as st

    number = st.number_input('Insert a number')
    st.write('The current number is ', number)
  ''')
with col2:
  st.markdown('**App**')
  number = st.number_input('Insert a number', 10)
  st.write('The current number is ', number)
