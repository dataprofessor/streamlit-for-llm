import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Lesson 2 - Using LLM models from OpenAI", page_icon="📖")

load_css()

st.header("📖 Lesson 2")
st.header("Using LLM models from OpenAI")

url_path = 'https://github.com/dataprofessor/streamlit-for-generative-ai/blob/master'
url_suffix = '?raw=true'

st.markdown(f'''
In this lesson, we will get you up to speed in using OpenAI for text generation and we will start from scratch by showing you how to get an API key, installing the `openai` library in Python and up to generating text and build simple ChatGPT-like chatbot.

## Table of Contents
1. [What is OpenAI?](#1-what-is-openai)
2. [Functionalities](#2-functionalities-of-openai)
3. [GPT for Text Generation](#3-gpt-for-text-generation)
4. [Getting your own OpenAI API key](#4-getting-your-own-openai-apikey)
5. [Installing OpenAI](#5-installing-openai-python-library)
6. [Setting the OpenAI API key on a local computer](6-setting-the-openai-api-key-on-a-local-computer)
7. [OpenAI for text generation](#7-openai-for-text-generation)
8. [Using the Chat Completion API](#8-using-the-chat-completion-api)
9. [Creating our simple ChatGPT-like chatbot](#9-creating-our-simple-chatgpt-like-chatbot)
10. [Spicing up the LLM generated response](#10-spicing-up-the-llm-generated-response)
11. [Summary](#11-summary)

## 1. What is OpenAI?

OpenAI is the company behind ChatGPT, which is a vastly popular chatbot that has an extraordinary ability for the generation of text response as a function of text input (known as prompts). Various news sources had even gone to the extreme of stating that ChatGPT would replace search engines as users could simply ask any question and the chatbot would be able to provide an impressive answer. Such generated response from large language models (LLM) is made possible due to the fact that these models are trained on an exhaustively large language data spanning the entirety of the internet.

LLMs have found immense utility for various tasks including but not limited to the following:
- Text generation, summarization, translation, etc.
- Code generation, refactoring, testing, etc.

## 2. Functionalities of OpenAI

OpenAI affords a wide range of functionalities through its API interface that developers can access via `curl` or the `openai` Python library.

The OpenAI API provides an interface to the following:
1. **Text** - Generative Pre-Trained Transformers (GPT) can accept user-provided inputs (prompts) in order to produce LLM generated responses in the form of document text, computer code, answers to questions, conversational text, etc. OpenAI provide different flavors of GPT particularly GPT3, GPT3.5 (the engine driving ChatGPT) and GPT4.
2. **Image** - Generate, manipulate or create variations of images using the DALL·E model as guided by input prompts.
3. **Embeddings** - Text embeddings are essentially a numerical representation of text that can be used to perform semantic search, clustering, recommendations, classification, anomaly detection, etc. OpenAI's text-embedding-ada-002 provides this capability.
4. **Speech to text** - The Whisper model enables transcription and translation of user-provided audio file through its API endpoints.
5. **Fine-tuning** - OpenAI models can be fine-tuned in order to achieve better results. This is accomplished by supplying a foundational model with a compilation of training instances, effectively offering a larger volume of examples than what can be achieved by few-shot learning (i.e. prompts with a few training examples).

''', unsafe_allow_html=True)
