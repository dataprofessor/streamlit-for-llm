# 📓 Lesson 3 - Getting up to speed with Hugging Face Hub

In this lesson, we'll be introducing the Hugging Face Hub and focus on the Models feature. Particularly, we'll explore the use of LLM models that are hosted on the Hugging Face Hub platform for building LLM tools.

## Table of Contents
1. [What is Hugging Face Hub?](#1-what-is-hugging-face-hub)
2. [Using Hugging Face Hub](#2-using-hugging-face-hub)
3. [Using a Hugging Face Model](#3-using-a-hugging-face-model)
4. [Summary](#4-summary)

## 1. What is Hugging Face Hub?

The Hugging Face Hub is an open-source platform that hosts over 120,000 models, 20,000 datasets, and 50,000 demo apps, where all have been designed to facilitate collaboration and innovation in machine learning. Particularly, models can be uploaded to the platform, models can then be fine-tuned and models can be accessed via API inference calls as well as via the `transformers` library in Python.

## 2. Hugging Face Models

Hugging Face Models is available at https://huggingface.co/models and a screenshot is shown below:

<p align="center">
  <img src="../img/lesson-3-hugging-face-hub-models.png" width="65%">
</p>

As we can see in the left side panel, models are conveniently categorized into various Tasks and in this lesson we'll focus on LLMs which can be found in _Text2Text Generation_ under the *Natural Language Processing* sub-heading.


Let's say that we want to use Google's [FLAT-T5 base](https://huggingface.co/google/flan-t5-base) model, we can navigate to its model page (see screenshot below).

**Model card**

The model card provides an extensive coverage on further information about the model as follows:
- TL;DR
- Model Details
- Usage
- Uses
- Bias, Risks, and Limitations
- Training Details
- Evaluation
- Environmental Impact
- Citation
- Model Card Authors

**Tune/Deploy/Use model**

In addition to using models as originally provided, you can also fine-tune the model and deploying the model (via inference API, Spaces app, etc.).

**Hosted inference API**

We can test the model by experimenting with the _Hosted inference API_ found on the right panel. Additionally, we can see example apps using the FLAN-T5 model in _Spaces using google/flan-t5-base_.

**Spaces using the model**

Example apps using the model as deployed on Spaces is listed and would serve as a good source of inspiration.

<p align="center">
  <img src="../img/lesson-3-huggingface.co_google_flan-t5-base.png" width="75%">
</p>

[//]: # (Hugging Face Model Page Diagram https://excalidraw.com/#json=Wk098OU44goApcrItbIlT,NZpeTWLp1EbrU96obSt9IQ)



## 3. Using a Hugging Face Model

Let's proceed to using the model. 

Particularly, instructions for using the model is provided in two places:
1. **</> Use in Transformers** - A button located in the top-right hand corner, provides information on how to use the model via the `transformers` Python library.
2. **_Usage_ section in the _Model card_** - Example scripts on using the model via the `transformers` Python library are also provided here.

### Installing the transformers library

The `transformers` library can be installed in Python as follows:

```
pip install transformers
```

### Running the model

There are several ways of running the model:
1. Run model directly
2. Run model via a pipeline
3. Access model from an inference API

**Run model directly**

In the first instance, models can be run directly as follows:

```python
# Load libraries
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Instantiate tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# Define input text and apply tokenizer
input_text = "The square root of x is the cube root of y. What is y to the power of 2, if x = 4?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# Run the model
outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))
```

**Run model via a pipeline**

In the second instance, models can be run via a pipeline as follows:

```python
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-base")
pipe("The square root of x is the cube root of y. What is y to the power of 2, if x = 4?")
```

**Access model from an inference API**

In the third instance, models can also be accessed via an inference API. This can be accessed by going to the _Model page_ as shown in the screenshot above, then in the top-right corner, click on `Deploy` > `Inference API`. 

This brings up a pop-up window displaying the following code snippet for using the model via an inference API:

```
import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "The answer to the universe is",
})
```

The generated output, irrespective of which methods were used, would give the following:
```
x = 4 * 2 = 8 x = 16 y = 16 to the power
```

## 4. Summary

