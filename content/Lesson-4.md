# 📖 Lesson 4 - Using hosted open source LLM models from Replicate

In this lesson, we'll be taking a look at how we can use a remotely hosted LLM model.

## Table of Contents
1. [What is Replicate?](#1-what-is-replicate)
2. [Installing Replicate](#2-installing-replicate)
3. [Getting your own Replicate API token](#3-getting-your-own-replicate-api-token)
4. [Setting the Replicate API token](#4-setting-the-replicate-api-token)
5. [Run an LLM model](#5-run-an-llm-model)
6. [Summary](#6-summary)

## 1. What is Replicate?

Replicate is an online platform that lets user run machine learning models in a few lines of code without the need to understand how machine learning works. This is particularly helpful for integrating machine learning functionality in any websites with no overhead on the model training and maintenance aspects. 

<p align="center">
   <img src="../img/lesson-4-replicate-explore-language-models.png" width="90%">
</p>

Such models are accessible via a simple API call and Replicate's model page provide code snippets (available in Node.js, Python and HTTP) to get users started in provisioning their own projects.

<p align="center">
   <img src="../img/lesson-4-replicate-model-page.png" width="90%">
</p>

In addition, to code snippets, another notable feature on the model page is the Demo that allows the user to play with the LLM model. Go ahead, try adjusting the prompt and model parameters and see how it works.

<p align="center">
   <img src="../img/lesson-4-replicate-demo-page.png" width="90%">
</p>

## 2. Installing Replicate

Of the above mentioned methods of using Replicate, we're going to use it via a Python library. 

Let's install the `replicate` library via `pip` as follows:

```Python
pip install replicate
```

Now, we're good to go!

## 3. Getting your own Replicate API token

Watch the following screencast to get your own Replicate API token.
<p align="center">
   <img src="../img/lesson-4-replicate-api-token.gif" width="90%">
</p>

## 4. Setting the Replicate API token

In order to allow our Python script access to the forthcoming LLM model, we'll need to assign the Replicate API token as an environment variable so that it is in memory for subsequent authorization by the Replicate platform.

```Python
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_xxxxxxxxxxxxxxxxxxx"
```

## 5. Running an LLM model

To perform an LLM response generation, we'll need to:
- Import the `replicate` library
- Define our system prompt (i.e. herein defined as the `pre_prompt` variable) and prompt input
- Generate the LLM response by calling the `replicate.run()` method along with specifying the LLM model to use, the prompt input as well as model parameters.

```Python
import replicate

# Prompts
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "What is Streamlit?"

# Generate LLM response
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters
```

## 6. Summary

In this lesson, you've learned how to use a remotely hosted LLM model.
