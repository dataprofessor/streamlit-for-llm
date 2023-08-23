import streamlit as st
from utilities import load_css

st.set_page_config(page_title="Lesson 2 - Using LLM models from OpenAI", page_icon="📖")

load_css()

st.header("📖 Lesson 2")
st.header("Using LLM models from OpenAI")

url_path = 'https://github.com/dataprofessor/streamlit-for-generative-ai/blob/master'
url_suffix = '?raw=true'

st.markdown(f'''
In this lesson, we'll get you up to speed in using OpenAI for text generation and we'll start from scratch by showing you how to get an API key, installing the `openai` library in Python and up to generating text and build simple ChatGPT-like chatbot.

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

## 3. GPT for Text Generation

OpenAI refers to text generation simply as completions as in text completion. It is interesting to note the naming convention, which derives from  how these language models generate text via the use of word probability, one word at a time as it completes the initial starting words to form complete sentences.

An alternative to completions are chat completions that are GPT models that have been optimized for conversational text. We are probably most familiar with this GPT type as the underlying GPT 3.5 and their flagship GPT 4 are powering the vastly popular ChatGPT.

An added benefit of chat completions is that they are less prone to prompt injection attacks as user-provided content is separate from instruction prompt.

It is worthy to note that going forward, their completions API are in plans for deprecation and this stems from the higher usage of their chat completions API accounting for 97% of their GPT API usage. This comes at a time when GPT 4 is being rolled out to all paying API users. Further details are provided in this OpenAI blog released on July 6, 2023.

## 4. Getting your own OpenAI API key

Follow the following steps to get your own API key from OpenAI:
1. Go to https://openai.com/
2. Click on Menu > Developers > Overview
3. Click on your Profile image (top right) > View API keys
4. Click on `+ Create new secret key`
5. Enter an optional `Name` for the API key for future reference

That's all it takes to create your own OpenAI API key, which starts with `sk-`.

> **💡 Note**
>
> An alternative to steps 1-3 mentioned above, you can also:
> 1. Make sure that you're logged in to your OpenAI account
> 2. Go to https://platform.openai.com/account/api-keys

Let's have a look at a short recording showing how to get your own OpenAI API key:

<p align="center">
   <img src="{url_path}/img/lesson-2-getting-api-key.gif{url_suffix}" width="65%">
</p>

> **💡 Note**
>
> Make sure to not share your API key in public repositories as others may use your API key and in doing so consume your API credits.

Further information for safely using API keys is summarized in the blog, [8 tips for securely using API keys](https://blog.streamlit.io/8-tips-for-securely-using-api-keys/)

## 5. Installing OpenAI Python library

The OpenAI library can be installed via `pip` as follows:
```python
pip install openai
```

## 6. Setting the OpenAI API key on a local computer

Recall that in a prior step, we've generated our OpenAI API key and instead of having to explicitly hard code the API key each time that we code an LLM tool, rather we're going to literally save the API key to memory. 
To do this, we're saving the API key as an environment variable that is essentially the memory of our operating system that we can access from the command line or from our Python code.
Depending on which operating system that we're using, we can set the environmental variable using varying commands. The article entitled Best Practices for API Key Safety by Michael Schade provides a great coverage on how to do this on various operating systems such as Windows, Linux and Mac OSX.

1. Setting the API key - To set the API key as an environment variable OPENAI_API_KEY we would enter the following into the command line (this is what I did on my local installation on a Mac OSX):

```
echo "export OPENAI_API_KEY='sk-xxxxxxxxxx'" >> ~/.zshrc
```

In practical terms, what these commands are doing is literally telling the computer to set (using the command `export`) the API key `sk-xxxxxxxxxx` as a variable called `OPENAI_API_KEY`. In order to save the previous command to a file the `echo` command was used together with `>>` followed by the file path `~/.zshrc` (`~` refers to the path of the current working directory which would typically be located at `/home/username`).

2. Update with the newly defined variable - Next, we will now want to tell the shell to update with the newly defined variable by entering:

```
source ~/.zshrc
```

3. Calling the API key from environment variable - To verify that our API key is indeed in the environment variable we can call it from the command line as follows:

```
echo $OPENAI_API_KEY
```

You should be able to see the API key as the returned output:

```
sk-xxxxxxxxxx
```

To use it from your Python code, you can call it from the environment variable via the `os.environ['OPENAI_API_KEY']`:

```python
# Import prerequisite libraries
import os
import openai

# Setting the API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Perform tasks using OpenAI API
openai.Model.list() # List all OpenAI models
```

## 7. OpenAI for text generation

Of all available models, those that can be used for text generation in OpenAI includes:
1. Chat Completions (`gpt-4`, `gpt-3.5-turbo`)
2. Completions (`text-davinci-003`, `text-davinci-002`, `davinci`, `curie`, `babbage`, `ada`)
As already mentioned above, going forward the chat completions API will be used as the default for text generation while the completions API would be deprecated.

## 8. Using the Chat Completion API
### 8.1. Test
Let's now proceed to using the Chat Completions API by providing it with an input prompt, and in this example, we use **_Hello_**!

```python
# Import prerequisite libraries
import os
import openai

# Setting the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Define the user prompt message
prompt = "Hello!"
# Create a chatbot using ChatCompletion.create() function
completion = openai.ChatCompletion.create(
  # Use GPT 3.5 as the LLM
  model="gpt-3.5-turbo",
  # Pre-define conversation messages for the possible roles 
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)
# Print the returned output from the LLM model
print(completion.choices[0].message)
```

The above code snippet produces the following output where the generated response is **_Hello! How can I assist you today_**?

```
{
  "role": "assistant",
  "content": "Hello! How can I assist you today?"
}
```

It is worthy to note that in this example, only 2 input parameters were used namely `model` and `messages` that correspondingly allowed us to specify the LLM model to use (GPT 3.5) and the pre-defined conversation messages consisting of `system` and `user` (_i.e._ `assistant` was not specified in this example).

### 8.2. Creating a blog outline generator
With a little tweak to the system and prompt messages, we can create a blog outline generator.

```python
import os
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Please generate a blog outline on how a beginner can break into the field of data science."

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant with extensive experience in data science and technical writing."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
```

The code snippet mentioned above works in a Colab or Jupyter notebook environment, as well as in a command line interface. For the latter, if you save it as a file (for instance as `blog.py`)  you can run it in the command line by typing python `blog.py`

<p align="center">
   <img src="{url_path}/img/lesson-2-blog-py.gif{url_suffix}" width="65%">
</p>

## 9. Creating our simple ChatGPT-like chatbot 

With the OpenAI API, we can create our own ChatGPT chatbot using the same technology!

However, this chatbot is a simpler version without the fancy graphical user interface (GUI) and instead of entering prompts into a text box, we provide them in the form of an input argument to a function.

Let's consider the following example code snippet for a creating a simple ChatGPT-like chatbot along with a detailed explanation as in-line comments. 

The chatbot even has memory of the conversation history!

```python
import openai

# Initialize the chat messages history
messages = [{"role": "assistant", "content": "How can I help?"}]

# Function to display the chat history
def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")

# Function to get the assistant's response
def get_assistant_response(messages):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

# Main chat loop
while True:
    # Display chat history
    display_chat_history(messages)
    
    # Get user input
    prompt = input("User: ")
    messages.append({"role": "user", "content": prompt})
    
    # Get assistant response
    response = get_assistant_response(messages)
    messages.append({"role": "assistant", "content": response})
```

The above code snippet works in a Colab or Jupyter notebook and also works in the command line, when saved as a file such as chatbot.py and then running it via `python chatbot.py`

<p align="center">
   <img src="{url_path}/img/lesson-2-chatbot-py.gif{url_suffix}" width="65%">
</p>

## 10. Spicing up the LLM generated response

To spice up and add creativity to the LLM generated response, you can experiment with the temperature or top_p parameters.

Possible values of the temperature parameter is in the range of 0 and 1 where 0 would lead to a conservative response (i.e. selects the highest probable words) whereas values approaching 1 would lead to a more creative response (i.e. selects a less probable word).

Possible values of the top_p parameter is in the range of 0 and 1. The top_p value represents the cumulative probability of top-ranking probable words and it helps to reduce less probable words from the LLM generated response.

Suggested starting points to try out for these 2 parameters is rationalized in an OpenAI forum response entitled [_Mastering Temperature and Top_p in ChatGPT API_](https://medium.com/r/?url=https%3A%2F%2Fcommunity.openai.com%2Ft%2Fcheat-sheet-mastering-temperature-and-top-p-in-chatgpt-api-a-few-tips-and-tricks-on-controlling-the-creativity-deterministic-output-of-prompt-responses%2F172683).

## 11. Summary

In summary, this lesson have laid the groundwork for getting started with using the OpenAI Python library to create a useful LLM tool for blog ideation as well as a simple chatbot. Armed with this new knowledge and set of skills, you're now ready to build impactful generative AI tools for addressing any real-world problem that interests you.
''')

load_css()
