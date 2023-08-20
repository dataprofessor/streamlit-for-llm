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

# Table of Contents
st.header('Table of Contents')
st.markdown('''
<ul style="list-style-type:square;">
   <li>
      <a href="Apples" target="_self">
         Lesson 1 - Getting up to speed with Streamlit
      </a>
   </li>
</ul>


''', unsafe_allow_html=True)

#- [**Lesson 1** - Getting up to speed with Streamlit](Apples)
#- [**Lesson 2** - Using LLM models from OpenAI](./content/Lesson-2.md)
#- [**Lesson 3** - Using open source LLM models from Hugging Face Hub](./content/Lesson-3.md)
#- [**Lesson 4** - Using hosted open source LLM models from Replicate](./content/Lesson-4.md)
#- [**Lesson 5** - Orchestrating an LLM workflow with LangChain](./content/Lesson-5.md)
#- [**Project 1** - Build a ChatGPT clone](./content/Project-1.md)
#- [**Project 2** - Build a Llama 2 chatbot](./content/Project-2.md)
#- [**Project 3** - Build a HugChat chatbot](./content/Project-3.md)

load_css()
