# 📓 Lesson 4 - Getting up to speed with LangChain

## Table of Contents
1. [What is LangChain?](#1-what-is-langchain)
2. [Installing LangChain](#2-installing-langchain)
3. [Using LangChain](#3-using-langchain)

## 1. What is LangChain?

[LangChain](https://langchain.com/?ref=blog.streamlit.io) is a framework that uses LLMs to build applications for various use cases. Created by Harrison Chase, it was first released as an open-source project in October 2022. To date, it has accumulated 41,900 stars on [GitHub](https://github.com/hwchase17/langchain?ref=blog.streamlit.io) and has over 800 contributors.

<p align="center">
   <img src="../img/lesson-4-langchain-star-history.png" width="65%">
</p>

At a high level, LangChain connects LLM models (such as OpenAI and HuggingFace Hub) to external sources like Google, Wikipedia, Notion, and Wolfram. It provides abstractions (chains and agents) and tools (prompt templates, memory, document loaders, output parsers) to interface between text input and output. LLM models and components are linked into a pipeline "chain," making it easy for developers to rapidly prototype robust applications. Simply put, LangChain orchestrates the LLM pipeline.

LangChain's power lies in its six key modules:

1. **Model I/O:** Facilitates the interface of model input (prompts) with the LLM model (closed or open-source) to produce the model output (output parsers)
2. **Data connection:** Enables user data to be loaded (document loaders), transformed (document transformers), stored (text embedding models and vector stores) and queried (retrievers)
3. **Memory:** Confer chains or agents with the capacity for short-term and long-term memory so that it remembers previous interactions with the user
4. **Chains:** A way to combine several components or other chains in a single pipeline (or “chain”)
5. **Agents:** Depending on the input, the agent decides on a course of action to take with the available tools/data that it has access to
6. **Callbacks:** Functions that are triggered to perform at specific points during the duration of an LLM run

> 💡 Note
> 
> Check out the [LangChain documentation](https://python.langchain.com/?ref=blog.streamlit.io) for further information on each of these modules.

## 2. Installing LangChain

The LangChain library can be installed via `pip` as follows:
```python
pip install langchain
```

## 3. Using LangChain

Let's now proceed to building a simple LLM workflow that makes use of both LangChain and OpenAI.

In the following example, we're going to use 2 LangChain features particularly:
1. Prompt template
2. Simple chain

```python
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# Prompt
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

# LLM chain
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)

# LLM generated response
question = "What NBA team won the Championship in the year Michael Jordan was born?"
llm_chain.run(question)
```

This gives the resulting output:

```
First, Michael Jordan was born in 1963.
Second, the National Basketball Association (NBA) was founded in 1946.
Therefore, in 1963, the NBA was in its 17th season.
Finally, the Boston Celtics won the NBA championship in 1963.
```

