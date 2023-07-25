# 📓 Lesson 3 - Getting up to speed with Hugging Face Hub

In this lesson, we'll be introducing the Hugging Face Hub and focus on the Models feature. Particularly, we'll explore the use of LLM models that are hosted on the Hugging Face Hub platform for building LLM tools.

## Table of Contents
1. [What is Hugging Face Hub?](#1-what-is-hugging-face-hub)
2. [Using Hugging Face Hub](#2-using-hugging-face-hub)
3. [Using a Hugging Face Model](#3-using-a-hugging-face-model)

## 1. What is Hugging Face Hub?

The Hugging Face Hub is an open-source platform that hosts over 120,000 models, 20,000 datasets, and 50,000 demo apps, where all have been designed to facilitate collaboration and innovation in machine learning. Particularly, models can be uploaded to the platform, models can then be fine-tuned and models can be accessed via API inference calls as well as via the `transformers` library in Python.

## 2. Hugging Face Models

Hugging Face Models is available at https://huggingface.co/models and a screenshot is shown below:

<p align="center">
   <img src="../img/lesson-3-hugging-face-hub-models.png" width="65%">
</p>

As we can see in the left side panel, models are conveniently categorized into various Tasks and in this lesson we'll focus on LLMs which can be found in _Text2Text Generation_ under the *Natural Language Processing* sub-heading.

Let's say that we want to use Google's [FLAT-T5 base](https://huggingface.co/google/flan-t5-base) model, we can navigate to its model page whereby further information about the model is provided in its Model card.

<p align="center">
   <img src="../img/lesson-3-huggingface.co_google_flan-t5-base.png" width="65%">
</p>

We can test the model by experimenting with the _Hosted inference API_ found on the right panel. Additionally, we can see example apps using the FLAN-T5 model in _Spaces using google/flan-t5-base_.

[//]: # (Hugging Face Model Page Diagram https://excalidraw.com/#json=Wk098OU44goApcrItbIlT,NZpeTWLp1EbrU96obSt9IQ)

## 3. Using a Hugging Face Model

Let's proceed to using the model. Particularly, instructions for using the model is provided in two places:
1. _</> Use in Transformers_ - A button located in the top-right hand corner, provides information on how to use the model via the `transformers` Python library.
2. _Usage_ section in the _Model card_ - Example scripts on using the model via the `transformers` Python library are also provided here.
