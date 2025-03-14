---
title: Unlocking Customer Insights with AI Market Research Digital Twins
layout: post
permalink: blog/blog90/
categories: [Generative AI]
---

![Market Research Digital Twin (Image by Author).](https://cdn-images-1.medium.com/max/3342/1*tzLOTQ9i-80u5bkhlKDmpA.gif)<br>Market Research Digital Twin (Image by Author).

<!--end_excerpt-->

## Unlocking Customer Insights with AI Market Research Digital Twins

<table>
    <thead>
    <tr>
        <td align="left">
        :memo:   Please Note
        </td>
    </tr>
    </thead>

    <tbody>
    <tr>
        <td>
        <ul>
            This is a guest post originally published on <a href="https://medium.com/p/5c576ab3f184" target="_blank">Google Cloud - Community</a>.
        </ul>
        </td>
    </tr>
    </tbody>
</table>

### An end to end guide on how to generate synthetic survey results data and create digital twins of survey respondents

## Introduction

In today’s fast-paced market, understanding your customer is paramount. Traditional market research methods, while valuable, can be time-consuming and expensive. What if you could create a “digital twin” of your target customer, an AI-powered persona that could answer your questions, provide feedback, and offer insights on demand?

This blog post will guide you through building your own Market Research Digital Twin using Streamlit, a user-friendly Python framework for creating web applications, and Google’s Gemini Pro. This dynamic duo will enable us to quickly prototype and deploy an interactive tool to gather customer insights.

The application will consist of first asking the user to provide a description of an example potential customer persona and a series of survey questions the potential customer should answer to create a target profile. Once the survey is responded using Gemini, a chat session with the created digital twin is created for the user to interact with and gain new customer behaviour insights.

## Digital Twins

A digital twin in this context is an AI representation of an ideal customer, built on data and designed to simulate their responses and behaviors. Here’s why this approach is gaining traction:

* **Speed and Efficiency:** Get answers to your market research questions instantly, without the lead times associated with traditional surveys or focus groups.

* **Cost-Effectiveness:** Reduce the expenses of recruiting, incentivizing, and analyzing data from real participants.

* **Scalability:** Create multiple digital twins representing different customer segments, allowing for targeted research and analysis.

* **24/7 Availability:** Your digital twin is always ready to provide insights, whenever you need them.

* **Iterative Exploration:** Experiment with different questions and scenarios to explore customer perspectives in depth.

## Demonstration

Let’s dive into the practical steps of creating the application. In this example we will be assuming to be working in a [Cloud Workstations](https://cloud.google.com/workstations/docs) environment.

### **Step 1: Setting up the Environment**

 1. **Google Cloud Project:** You’ll need a Google Cloud Project with the Vertex AI API enabled.
 2. **Installing Dependencies:** Install the necessary Python libraries:

````
pip install streamlit google-cloud-aiplatform
````

**3. Authentication:** Set up your Google Cloud authentication so your application can access the Vertex AI API. You can use Application Default Credentials (ADC) for this. For example, by using the Google Cloud SDK:

    gcloud auth application-default login

### Step 2: Importing Libraries and Initializing the Model

First we import all the necessary libraries, retrieve the current Project ID and instantiate our Gemini model.

````python
import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, Content
import sys

# Get project ID from command line argument if available
project_id = "your-project-here" if not sys.argv else sys.argv[1]

# Initialize Vertex AI
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel("gemini-pro")
````

### **Step 3: **Defining Helper Functions **Streamlit App Structure**

Setting up:

* Helper function to get Gemini responses.

* Session state variables for storing chat history and initial survey responses.

* Creating input fields for the user to define the persona description and the initial survey questions.

````python
def get_gemini_response(model, prompt):
    """Gets a response from the Gemini model."""
    response = model.generate_content(prompt)
    return response.text

st.title("Market Research Digital Twin")

# Initialize chat history and initial response in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "initial_response" not in st.session_state:
    st.session_state.initial_response = None

# User input
persona_desc = st.text_input("Enter your persona description:")
user_prompt = st.text_input("Enter your survey questions:")
````

### **Step 4: Defining Prompts and Instructions**

At this point we are ready to define the two main prompts to first answer survey questions based on the provided profile and then specify the system prompt to follow in order to impersonate the Digital Twin during the chat interaction.

````python
INITIAL_PROMPT = f"""
You are working for a market research company interested in asking a series of questions to potential users. 
Make sure to reply to all the questions as an average {persona_desc}:

Here is the list of questions:
"""

BOILERPLATE_INSTRUCTIONS = f"""
You are working for a market research company interested in asking a series of questions to potential users. 
Make sure to reply to all the questions as an average {persona_desc}. 
Here are some information about the persona you are trying to impersonate:
"""
````

### **Step 5: Main App Loop**

Once the user has provided the survey questions and persona description, the main Streamlit loop can be initiated. After the survey questions have been answered by Gemini, the results are then displayed on screen and the main chat session with the newly generated digital twin is created.

````python
if persona_desc and user_prompt:
    # Calculate initial_response only if it's not already calculated
    if st.session_state.initial_response is None:
        st.session_state.initial_response = get_gemini_response(
            model, INITIAL_PROMPT + "\n\n" + user_prompt
        )

    # Display initial_response in Markdown (only if it's available)
    if st.session_state.initial_response:
        st.markdown("**Initial Survey Response:**")
        st.markdown(st.session_state.initial_response)

        # Construct the system instructions using the stored initial_response
        system_instructions = (
            BOILERPLATE_INSTRUCTIONS
            + "\n\n"
            + st.session_state.initial_response
            + "\n\n"
            + "Use the answers to these questions to then reply to any 
                follow up question in the chat. You need to pretend to be 
                the virtual version of the person that responded to this 
                survey."
        )

        # Create Content objects for system instructions
        initial_messages = [
            Content(
                role="user",
                parts=[Part.from_text(system_instructions)],
            )
        ]
        
        # Start the chat session
        chat = model.start_chat(history=initial_messages)

        # Accept user input in the chat
        if prompt := st.chat_input("What is up?"):
            # Add user message to chat history (session_state)
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Send user prompt to the chat and get the response
            chat_response = chat.send_message(prompt)

            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": chat_response.text}
            )

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
````

### **Step 6: Running the Application**

At this point we just need to save the code as a Python file (e.g., app.py) and run it from the terminal:

    streamlit run app.py   --browser.serverAddress=localhost   --server.enableCORS=false   --server.enableXsrfProtection=false   --server.port 8080 your-project-name

In case you don’t have any example survey to use on the spot, this could be easily generated providing Gemini with a prompt like this:

    I work for a Market research company, and want to do some research 
    about customer behaviour in the music sector, can you create an 
    extensive questionnaire to get all the necessary info to create an 
    accurate profile about a potential target customer?

An example demonstration of the whole workflow is provided below (Figure 1):

![Figure 1: End result application (Image by Author).](https://cdn-images-1.medium.com/max/3342/1*tzLOTQ9i-80u5bkhlKDmpA.gif)<br>Figure 1: End result application (Image by Author).

## Conclusion

This application is just a starting point of how GenAI could be used for Market Research. This process could be further enhanced for example by:

* **Adding more sophisticated persona creation:** Use data from various sources to build richer and more nuanced digital twins.

* **Implementing advanced prompting techniques:** Fine-tuning the model’s responses and explore different interaction styles.

* **Integrating with other data sources and analytics tools:** Connect your digital twin to real-time data and gain deeper insights.

* **Building a more polished UI:** Adding features like user profiles, data visualization, and reporting.
