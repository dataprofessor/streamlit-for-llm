# 📖 Lesson 0 <br> Getting up to speed with Streamlit

In this lesson, we'll get you started with Streamlit from going over the overarching concept of this low-code web framework, setting up a coding environment and to writing your first Streamlit app.

## Table of Contents
1. [What is Streamlit?](#1-what-is-streamlit)
2. [Prerequisites](#2-prerequisites)
3. [Installing Streamlit](#3-installing-streamlit)
4. [Setting up your Streamlit workspace](#4-setting-up-your-streamlit-workspace)
5. [Creating your first Streamlit app](#5-creating-your-first-streamlit-app)
6. [Running the Streamlit app](#6-running-the-streamlit-app)
7. [Methods for displaying information in the app](#7-methods-for-displaying-information-in-the-app)
8. [Input widgets for accepting user information in the app](#8-input-widgets-for-accepting-user-information-in-the-app)
9. [Chat elements for building a chatbot](#9-chat-elements-for-building-a-chatbot)
10. [Summary](#summary)
11. [Examples](#examples)

## 1. What is Streamlit?

Streamlit is a Python library that you can use to build interactive data-driven web apps.

A typical workflow for the creation and deployment of Streamlit app is summarized below:

<p align="center">
   <img src="../img/lesson-0-streamlit-workflow.png" width="90%">
</p>

1. **Collect requirements** - In this phase, we want to make a list of the desirable features and capabilities that we want our web app to do.
2. **Code** - Next, we'll do the actual coding of the web app with the Streamlit library.
3. **Repo** - Once the code is complete, we can Git push (*i.e.* upload) it to a GitHub repo where app files are stored and used in a subsequent deployment phase. 
4. **Cloud** - To share our Streamlit apps publicly, we're going to deploy the app on the cloud using a platform such as [Streamlit Community Cloud](https://streamlit.io/cloud). In a few clicks of the mouse, one can go from app files stored on the GitHub repo to a deployed app.
5. **App** - Streamlit app can be easily shared via the deployed URL in the format of https://<subdomain>.streamlit.app/ where `subdomain` refers to the unique identifier that can either be automatically generated by the server as a long form URL (*e.g.* https://dataprofessor-st-matplotlib-line-plot-streamlit-app-2a0abu.streamlit.app/) or explicitly renamed to a shorter and easy to remember one (*e.g.* https://chanin.streamlit.app/).

## 2. Prerequisites

Here's what you need to use Streamlit:
- Have basic Python knowledge.
- Write scripts to perform specific tasks (like taking several Excel files as input and combining them into one).
- Build and grow the Streamlit app line by line instead of starting with a predefined layout (it takes only a few lines of code).
If you can do all this, congratulations! You're ready to plunge into the world of Streamlit.

## 3. Installing Streamlit

If you already have an existing Python coding environment, Streamlit can be installed using `pip` as shown below:

```
pip install streamlit
```

## 4. Setting up your Streamlit workspace

It is typically good practice to house the Streamlit app in their own dedicated conda environment. This way the library dependencies don’t get entangled with other Python libraries used by other apps.

Here, we're going to replicate a Streamlit app from an existing GitHub repo available at https://github.com/dataprofessor/eda-app/.

Particularly, we're going to clone the EDA app from a YouTube tutorial video on [*How to Build an EDA app using Pandas Profiling*](https://youtu.be/p4uohebPuCg).

**Step 1.** Create a conda environment

Create a conda environment called eda:

```
conda create -n eda python=3.8
```

**Step 2.** Activate the eda environment:

```
conda activate eda
```

**Step 3.** To install prerequisite libraries we must first download the requirements.txt file (it contains the library version numbers):

```
wget https://raw.githubusercontent.com/dataprofessor/ydata_profiling/main/requirements.txt
```

**Step 4.** To actually install prerequisite libraries using the requirements.txt file

```
pip install -r requirements.txt
```

Inside the `requirements.txt` file you'll see the following contents:

```
streamlit
pandas
ydata_profiling
streamlit_pandas_profiling
```

**Step 5.** Download and unzip contents from the GitHub repo: https://github.com/dataprofessor/ydata_profiling/archive/main.zip

**Step 6.** Launch the app:

```
streamlit run app.py
```

You’ll see the web app browser pop up:

<p align="center">
  <img src="../img/lesson-0-EDA-app.png" width="90%">
</p>

The functionality of this EDA app leverages the capabilities of pandas-profiling. Let's take a look at the app in action:

<p align="center">
   <img src="../img/lesson-0-EDA-app-screencast.gif" width="90%">
</p>

Congratulations! You now know how to clone a Streamlit app from a GitHub repo, setup a dedicated conda environment, and successfully launch the app!

## 5. Creating your first Streamlit app

Before we get into the nuts and bolts of the Streamlit library, let's take a hands-on approach for learning how to use Streamlit. Particularly, creating a simple **Hello world app** would probably be an expected rite of passage to learning Streamlit!

It's not as difficult as you may think. In fact, it takes only 2 lines of code to do just that!

```Python
import streamlit as st
st.write('Hello world!')
```

Click on the **See code explanation** toggle button to reveal the explanatory text:

<details>
<summary><i>See code explanation</i></summary>

Here's a line-by-line breakdown of the code:
  1. Import the `streamlit` library as `st` (so that we can later refer to `streamlit` literally as `st` instead of having to type the full word `streamlit`.
  2. Use `st.write` to write a text output and inside the `st.write` command we use the `'Hello world!'` string as the input argument.
</details>

## 6. Running the Streamlit app

Locally, you can run the newly created Streamlit app by launching a command-line terminal and enter the following:

```
streamlit run streamlit_app.py
```

where `streamlit_app.py` is the Streamlit app that you've just created.



## 7. Output widgets for displaying information in the app

Now that we know how to create your first Streamlit app and get it up and running, it's now time to explore how we can display information in the app.

In the Streamlit Documentation page, the [Text elements](https://docs.streamlit.io/library/api-reference/text) and [Write and magic](https://docs.streamlit.io/library/api-reference/write-magic) pages provide several ways in which information can be displayed. 

Here's a list of methods for displaying information in app:
- [`st.title()`](https://docs.streamlit.io/library/api-reference/text/st.title) - Display the app's title.
- [`st.header()`](https://docs.streamlit.io/library/api-reference/text/st.header) - Display text as a section header
- [`st.subheader()`](https://docs.streamlit.io/library/api-reference/text/st.subheader) - Display text as a sub-section header
- [`st.write()`](https://docs.streamlit.io/library/api-reference/text/st.write) - Can both display text and write arguments to the app.
- [`st.markdown()`](https://docs.streamlit.io/library/api-reference/text/st.markdown) - Display text in Markdown format
- [`st.text()`](https://docs.streamlit.io/library/api-reference/text/st.text) - Display fixed width and pre-formatted text
- [`st.code()`](https://docs.streamlit.io/library/api-reference/text/st.code) - Display code that can be copied
- [`st.caption()`](https://docs.streamlit.io/library/api-reference/text/st.caption) - Display small caption text
- [`st.latex()`](https://docs.streamlit.io/library/api-reference/text/st.latex) - Display LaTeX expressions

Proceed to **Project 0** to see how to use these widgets in a Streamlit app.

## 8. Input widgets for accepting user information in the app

A great part about building data-driven apps is the ability to take in user input via various widgets, for example, sliders, text input, number input, color selector, etc. Such widget input can then be used to set model parameters, assign values to function parameters, and so much more.

Here's a list of common input widgets that I typically use:
- [`st.text_input()`](https://docs.streamlit.io/library/api-reference/text/st.text_input) - Displays a single-line text input widget
- [`st.number_input()`](https://docs.streamlit.io/library/api-reference/text/st.number_input) - Displays a number input widget
- [`st.selectbox()`](https://docs.streamlit.io/library/api-reference/text/st.selectbox) - Displays a drop-down selection widget
- [`st.multiselect()`](https://docs.streamlit.io/library/api-reference/text/st.multiselect) - Displays a multi-selection widget
- [`st.slider()`](https://docs.streamlit.io/library/api-reference/text/st.slider) - Displays either a single-value slider or a range slider
- [`st.file_uploader()`](https://docs.streamlit.io/library/api-reference/text/st.file_uploader) - Displays a file upload widget
- [`st.button()`](https://docs.streamlit.io/library/api-reference/text/st.button) - Displays a button widget
- [`st.download_button()`](https://docs.streamlit.io/library/api-reference/text/st.download_button) - Displays a download button widget

Note: It should be mentioned that aside from those listed above, there are several more input widgets from which you can use. More information on the [Input widgets](https://docs.streamlit.io/library/api-reference/widgets) Docs page.

Proceed to **Project 0** to see how to use these widgets in a Streamlit app.

## 9. Chat elements for building a chatbot

Streamlit currently provides 3 chat elements widgets (more info in the [Chat elements](https://docs.streamlit.io/library/api-reference/chat) Docs page) that is designed for you to use in conjunction with one another, for example, in building a chatbot (or you can also use them separately).

Here's a list of the chat elements:
- [`st.chat_input()`](https://docs.streamlit.io/library/api-reference/chat/st.chat_input) - Displays a chat input widget
- [`st.chat_message()`](https://docs.streamlit.io/library/api-reference/chat/st.chat_message) - Inserts a chat message container for displaying LLM generated responses
- [`st.status()`](https://docs.streamlit.io/library/api-reference/status/st.status) - Inserts a status container for display output from long-running tasks

Proceed to **Project 0** to see how to use these widgets in a Streamlit app.

## Summary

In this lesson, we're introduced to Streamlit along with how to setup a computing environment as well as creating our first Streamlit app.

[//]: # 
