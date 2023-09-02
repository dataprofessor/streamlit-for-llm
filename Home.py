import streamlit as st
from PIL import Image
from utilities import load_css
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Welcome to the Streamlit for Generative AI course",
    page_icon="🏠",
)

load_css()

img = Image.open('img/streamlit-generative-ai-course-logo.png')
st.image(img)

# About
st.header('About')
st.info('The Streamlit for Generative AI course will show you how to use Streamlit to build large language model (LLM) powered apps. Finally you can deploy the Streamlit app to the cloud and share with the community.')

# Table of Contents
st.header('Table of Contents')
st.markdown('''
<ul style="list-style-type:square; margin: 5px;">
   <li>
      <a href="Lesson_0_Streamlit" target="_self" style="text-decoration: none;">
         <b>Lesson 0</b> - Getting up to speed with Streamlit
      </a>
   </li>

   <li>
      <a href="Lesson_1_Generative_AI" target="_self" style="text-decoration: none;">
         <b>Lesson 1</b> - An introduction to Generative AI
      </a>
   </li>

   <li>
      <a href="Lesson_2_OpenAI" target="_self" style="text-decoration: none;">
         <b>Lesson 2</b> - Using LLM models from OpenAI
      </a>
   </li>

   <li>
      <a href="Lesson_3_Hugging_Face_Hub" target="_self" style="text-decoration: none;">
         <b>Lesson 3</b> - Using open source LLM models from Hugging Face Hub
      </a>
   </li>

   <li>
      <a href="Lesson_4_Replicate" target="_self" style="text-decoration: none;">
         <b>Lesson 4</b> - Using hosted open source LLM models from Replicate
      </a>
   </li>

   <li>
      <a href="Lesson_5_LangChain" target="_self" style="text-decoration: none;">
         <b>Lesson 5</b> - Orchestrating an LLM workflow with LangChain
      </a>
   </li>

   <li>
      <a href="Project_1_ChatGPT_clone" target="_self" style="text-decoration: none;">
         <b>Project 1</b> - Build a ChatGPT clone
      </a>
   </li>

   <li>
      <a href="Project_2_Llama_2_chatbot" target="_self" style="text-decoration: none;">
         <b>Project 2</b> - Build a Llama 2 chatbot
      </a>
   </li>

   <li>
      <a href="Project_3_HugChat_chatbot" target="_self" style="text-decoration: none;">
         <b>Project 3</b> - Build a HugChat chatbot
      </a>
   </li>
   
   <li>
      <a href="Project_4_Code_Llama_chatbot" target="_self" style="text-decoration: none;">
         <b>Project 4</b> - Build a Code Llama chatbot
      </a>
   </li>
</ul>

''', unsafe_allow_html=True)


with st.expander('Testing ...'):
    if st.button('**Lesson 0** - Getting up to speed with Streamlit'):
        switch_page('Lesson_0_Streamlit')
        
    if st.button('**Lesson 1** - An introduction to Generative AI'):
        switch_page('Lesson_1_Generative_AI')


params = st.experimental_get_query_params()
if 'page' in params.keys():
    st.write(params.get('page')[0])
