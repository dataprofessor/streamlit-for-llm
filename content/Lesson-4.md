# 📓 Lesson 4 - Getting up to speed with LangChain

In this lesson, we'll get you started by providing a high-level overview of LangChain, a popular LLM framework that provides several auxilliary tools that helps creating LLM-based tools much easier. You'll also get your first hands-on experience by building simple LLM workflow using LangChain. Additional examples will be covered in the series of projects provided in the course.

## Table of Contents
1. [What is LangChain?](#1-what-is-langchain)
2. [Installing LangChain](#2-installing-langchain)
3. [Setting your OpenAI API key](#3-setting-your-openai-api-key)
4. [Using LangChain](#4-using-langchain)

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

> **💡 Note**
> 
> Check out the [LangChain documentation](https://python.langchain.com/?ref=blog.streamlit.io) for further information on each of these modules.

## 2. Installing LangChain

The LangChain library can be installed via `pip` as follows:
```python
pip install langchain
```

## 3. Setting your OpenAI API key

When using the LLM model from OpenAI, we're going to need an API key.

> **💡 Note**
>
> To get an API key, please refer to [Getting your own OpenAI API key](Lesson-2.md#4-getting-your-own-openai-apikey) from Lesson 2 of this course.

Once we have an API key, make sure to set the API key `sk-xxxxxxxxxx` to the environment variable `OPENAI_API_KEY`.

In a Colab notebook:
1. I've started by saving the API key to an `openai.txt` file, then upload that to the Colab notebook (clicking on the left sidebar).
2. Run the following code cell:

```python
import os

with open('openai.txt', 'r') as f: # Reading the text file
  os.environ['OPENAI_API_KEY'] = f.readline() # Assigning the API key
  f.close()
```

Now, we're good to go!

## 4. Using LangChain

### Building a simple LLM chain

Let's now proceed to building a simple LLM workflow that makes use of both LangChain and OpenAI.

In the following example, we're going to use 2 LangChain features particularly:
1. Prompt template
2. Simple chain

These 2 features were intentionally selected to show the use of LLMs with the chains feature. Particularly, we're chaining together a _prompt_ component with an _LLM_ component.

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

We can see that the output is thinking step by step before deriving the final answer, which is what we explicitly told the LLM to do in the provided prompt.

### Code explanation

Let's slow down a bit and dissect the code.

**Import libraries**
Initially, we'll import the prerequisite libraries:

```python
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
```
**Dynamically creating the prompt**
Next, we apply the `PromptTemplate()` method on the two prompt components: 1) `template` and `input_variables`.

First, we'll create the content of the prompt template and assign it to the `template` variable, which we'll use as an input argument for the subsequent line.

Second, we'll dynamically create the `prompt` using the `PromptTemplate()` method using two prompt components: 1) `template` and `input_variables`. The first component is already explained above as for the second component the user-provided question that we'll use in a forthcoming step, will be assigned as an input argument to the `input_variables` parameter.

```python
# Prompt
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
```

**Creating a simple LLM chain**

Here, we'll create the chain using the `LLMChain()` method and assign this to the `llm_chain` variable. As input arguments, we're defining the `prompt` and `llm`, which corresponds to the prompt template defined earlier and the newly defined LLM model using the `OpenAI()` method.

```python
# LLM chain
llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
```

**Generate LLM response**

Finally, we'll generate the LLM response by running `llm_chain.run()` while using the newly defined `question` as an input argument. Remember the prompt template that we mentioned earlier? Well, the question will be appended to the prompt template as 
```python
# LLM generated response
question = "What NBA team won the Championship in the year Michael Jordan was born?"
llm_chain.run(question)
```

## 5. Summary

In this lesson, we've seen how we can leverage the LangChain library to orchestrate a simple LLM chain by fusing a prompt template and the LLM model together in generating the LLM response. There are several other features that LangChain provides and examples for doing so are provided in the [LangChain documentation](https://python.langchain.com/). Additionally, we'll also get to see other LangChain features in action in subsequent Project sections of this course.

