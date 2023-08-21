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
<ul style="list-style-type:square; margin: 5px;">
   <li>
      <a href="Getting_up_to_speed_with_Streamlit" target="_self" style="text-decoration: none;">
         <b>Lesson 1</b> - Getting up to speed with Streamlit
      </a>
   </li>

   <li>
      <a href="Using_LLM_models_from_OpenAI" target="_self" style="text-decoration: none;">
         <b>Lesson 2</b> - Using LLM models from OpenAI
      </a>
   </li>

   <li>
      <a href="Using_open_source_LLM_models_from_Hugging_Face_Hub" target="_self" style="text-decoration: none;">
         <b>Lesson 3</b> - Using open source LLM models from Hugging Face Hub
      </a>
   </li>

   <li>
      <a href="Using_hosted_open_source_LLM_models_from_Replicate" target="_self" style="text-decoration: none;">
         <b>Lesson 4</b> - Using hosted open source LLM models from Replicate
      </a>
   </li>

   <li>
      <a href="Orchestrating_an_LLM_workflow_with_LangChain" target="_self" style="text-decoration: none;">
         <b>Lesson 5</b> - Orchestrating an LLM workflow with LangChain
      </a>
   </li>

   <li>
      <a href="Build_a_ChatGPT_clone" target="_self" style="text-decoration: none;">
         <b>Project 1</b> - Build a ChatGPT clone
      </a>
   </li>

   <li>
      <a href="Build_a_Llama2_chatbot" target="_self" style="text-decoration: none;">
         <b>Project 2</b> - Build a Llama 2 chatbot
      </a>
   </li>

   <li>
      <a href="Build_a_HugChat_chatbot" target="_self" style="text-decoration: none;">
         <b>Project 3</b> - Build a HugChat chatbot
      </a>
   </li>
</ul>

''', unsafe_allow_html=True)

#- [**Lesson 1** - Getting up to speed with Streamlit](Getting_up_to_speed_with_Streamlit)
#- [**Lesson 2** - Using LLM models from OpenAI](Using_LLM_models_from_OpenAI)
#- [**Lesson 3** - Using open source LLM models from Hugging Face Hub](./content/Lesson-3.md)
#- [**Lesson 4** - Using hosted open source LLM models from Replicate](./content/Lesson-4.md)
#- [**Lesson 5** - Orchestrating an LLM workflow with LangChain](./content/Lesson-5.md)
#- [**Project 1** - Build a ChatGPT clone](./content/Project-1.md)
#- [**Project 2** - Build a Llama 2 chatbot](./content/Project-2.md)
#- [**Project 3** - Build a HugChat chatbot](./content/Project-3.md)

load_css()
