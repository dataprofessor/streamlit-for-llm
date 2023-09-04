import streamlit as st
import numpy as np
import pandas as pd
import time
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

st.subheader('Output widgets')

with st.expander('See st.title() example', expanded=True):
  st.subheader('st.title()')
  st.text('Display text in title formatting.')
  col1, col2 = st.columns((3,2))
  with col1:
    st.markdown('**Code**')
    st.code('''
      import streamlit as st

      st.title('This is a title')
      st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    ''')
  with col2:
    st.markdown('**App**')
    st.title('This is a title')
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
  st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/text/st.title)')


with st.expander('See st.write() example'):
  st.subheader('st.write()')
  st.text('Write arguments to the app. This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it.')
  col1, col2 = st.columns((3,2))
  with col1:
    st.markdown('**Code**')
    st.code('''
      import streamlit as st
      import pandas as pd

      st.write('Hello, *World!* :sunglasses:')
      st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
      }))
      
    ''')
  with col2:
    st.markdown('**App**')
    st.write('Hello, *World!* :sunglasses:')
    st.write(pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40],
    }))
  st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/text/st.write)')


with st.expander('See st.latex() example'):
  st.subheader('st.latex()')
  st.text('Display mathematical expressions formatted as LaTeX.')
  col1, col2 = st.columns((3,2))
  with col1:
    st.markdown('**Code**')
    st.code('''
      import streamlit as st

      st.latex(r"E=mc^2")
    ''')
  with col2:
    st.markdown('**App**')
    st.latex(r"E=mc^2")
  st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/text/st.latex)')



st.subheader('Input widgets')

with st.expander('See st.text_input() example', expanded=True):
  st.subheader('st.text_input()')
  st.text('Display a single-line text input widget.')
  col1, col2 = st.columns((3,2))
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
  st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/widgets/st.text_input)')


with st.expander('See st.number_input() example'):
  st.subheader('st.number_input()')
  st.text('Display a numeric input widget.')
  col1, col2 = st.columns((3,2))
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
  st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/widgets/st.number_input)')


with st.expander('See st.selectbox() example'):
  st.subheader('st.selectbox()')
  st.text('Display a select widget.')
  col1, col2 = st.columns((3,2))
  with col1:
    st.markdown('**Code**')
    st.code('''
      import streamlit as st

      option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))
      st.write('You selected:', option)
    ''')
  with col2:
    st.markdown('**App**')
    option = st.selectbox(
      'How would you like to be contacted?',
      ('Email', 'Home phone', 'Mobile phone'))
    st.write('You selected:', option)
  st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)')


st.subheader('Chat elements')

with st.expander('See st.chat_message() example', expanded=True):
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



st.subheader('st.chat_input()')
st.text('Display a chat input widget.')

st.markdown('**Code**')
st.code('''
  import streamlit as st
  
  prompt = st.chat_input("Say something")
  if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
  ''')

if 'prompt' not in st.session_state:
  st.session_state.prompt = ""

st.markdown('**App**')
if st.button('See chat_input'):
  st.chat_input("Say something", key="prompt")
  st.write(f"User has sent the following prompt: {st.session_state.prompt}")

st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/chat/st.chat_input)')
