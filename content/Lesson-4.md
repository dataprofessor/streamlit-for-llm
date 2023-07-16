# 📓 Lesson 4 - Getting up to speed with LangChain

## Table of Contents
1. [What is LangChain?](#1-what-is-langchain)
2. [Installing LangChain](#2-installing-langchain)


## 1. What is LangChain?

[LangChain](https://langchain.com/?ref=blog.streamlit.io) is a framework that uses LLMs to build applications for various use cases. Created by Harrison Chase, it was first released as an open-source project in October 2022. To date, it has accumulated 41,900 stars on [GitHub](https://github.com/hwchase17/langchain?ref=blog.streamlit.io) and has over 800 contributors.

<p align="center">
   <img src="../img/lesson-4-langchain-star-history.png" width="65%">
</p>

At a high level, LangChain connects LLM models (such as OpenAI and HuggingFace Hub) to external sources like Google, Wikipedia, Notion, and Wolfram. It provides abstractions (chains and agents) and tools (prompt templates, memory, document loaders, output parsers) to interface between text input and output. LLM models and components are linked into a pipeline "chain," making it easy for developers to rapidly prototype robust applications. Simply put, Langchain orchestrates the LLM pipeline.

LangChain's power lies in its six key modules:

1. **Model I/O:** Facilitates the interface of model input (prompts) with the LLM model (closed or open-source) to produce the model output (output parsers)
2. **Data connection:** Enables user data to be loaded (document loaders), transformed (document transformers), stored (text embedding models and vector stores) and queried (retrievers)
3. **Memory:** Confer chains or agents with the capacity for short-term and long-term memory so that it remembers previous interactions with the user
4. **Chains:** A way to combine several components or other chains in a single pipeline (or “chain”)
5. **Agents:** Depending on the input, the agent decides on a course of action to take with the available tools/data that it has access to
6. **Callbacks:** Functions that are triggered to perform at specific points during the duration of an LLM run

## 2. Installing LangChain

The LangChain library can be installed via `pip` as follows:
```python
pip install langchain
```
> 💡 Note
> 
> Check out the LangChain documentation for further information on each of these modules.
