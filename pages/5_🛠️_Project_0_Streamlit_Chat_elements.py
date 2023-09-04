import streamlit as st
import numpy as np
import time
from utilities import load_css, read_md
from streamlit_extras.sandbox import sandbox
from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title="Project 0 - Streamlit Chat elements", page_icon="🛠️", layout="wide")

load_css()

md = read_md('Project-0.md')
st.markdown(md, unsafe_allow_html=True)

st.divider()

st.header('Building blocks of chat elements', divider='red')

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

def embedded_app():
    import streamlit as st
    
    prompt = st.chat_input("Say something")

    if prompt:
      st.write(f"User has sent the following prompt: {prompt}")

sandbox(embedded_app)

st.markdown('[More info on the Docs page](https://docs.streamlit.io/library/api-reference/chat/st.chat_input)')


st.divider()


st.header('Building an Echo bot', divider='red')
st.markdown('''
    In this example app, we are going to build a simple Echo bot that simply returns the exact message that we entered.
    
    This example app is from the [Build conversational apps](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-bot-that-mirrors-your-input) article.
''')

st.code('''
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
''')

def echo_bot():
    import streamlit as st

    st.title("Echo Bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
    
        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
sandbox(echo_bot)

st.header('Code explanation of the Echo bot')
st.markdown("""
In this section, we'll build a bot that mirrors or echoes your input. More specifically, the bot will respond to your input with the same message. We'll use `st.chat_message` to display the user's input and `st.chat_input` to accept user input. We'll also use session state to store the chat history so we can display it in the chat message container.



""")
