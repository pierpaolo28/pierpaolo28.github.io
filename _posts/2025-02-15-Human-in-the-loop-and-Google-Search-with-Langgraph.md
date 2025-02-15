---
title: Human in the loop and Google Search with Langgraph
layout: post
permalink: blog/blog89/
categories: [Generative AI]
---

![Langgraph chatbot with Human in the Loop capability (Image by Author).](https://cdn-images-1.medium.com/max/2972/1*96jC_l5j4N0zhlY0sAyPcQ.png)<br>Langgraph chatbot with Human in the Loop capability (Image by Author).

<!--end_excerpt-->

## Human in the loop and Google Search with Langgraph

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
            This is a guest post originally published on <a href="https://medium.com/google-cloud/human-in-the-loop-and-google-search-with-langgraph-1af5ff2d4e89" target="_blank">Google Cloud - Community</a>.
        </ul>
        </td>
    </tr>
    </tbody>
</table>

### End to end demonstration of how to use Langgraph to create a chatbot able to handover concerning questions to human experts.

## Introduction

In the rapidly evolving world of AI, chatbots are becoming increasingly sophisticated. However, they often hit a wall when faced with complex or novel queries, leading to uncertain or inaccurate responses. This is where LangChain’s new offering, **LangGraph**, comes into play. It allows us to build cyclical graphs that power agent runtimes, creating more dynamic and adaptable conversational AI.

This tutorial focuses on a specific LangGraph implementation that demonstrates a powerful solution: a chatbot that can identify its own limitations, request human intervention to improve its responses, and seamlessly integrate that expert knowledge back into the conversation. Additionally, use of other tools such as Google Search, will be demonstrated.

### LangGraph

LangGraph extends the capabilities of LangChain’s Expression Language (LCEL) by introducing the ability to coordinate multiple chains (or actors) across multiple steps of computation in a cyclic manner. Think of it like a state machine where:

* **Nodes:** represent functions, tools, or even other chains that perform specific actions (e.g., generating text, searching the web, replacing a SIM card).

* **Edges:** define the flow of execution between nodes. They can be conditional, allowing the chatbot to make decisions based on the current state.

* **State:** is a shared data structure that is passed between nodes and updated throughout the conversation. It holds information like the chat history, intermediate results, and flags.

Unlike linear chains, LangGraph’s cyclical nature allows for loops and iterative processes. This is crucial for:

 1. **Reasoning:** The chatbot can revisit previous steps, refine its understanding, and generate more accurate responses.

 2. **Error Handling:** When the chatbot is uncertain, it can loop back to a specific state and request human help.

 3. **Tool Use:** The chatbot can strategically decide which tools to use and when, leading to more effective problem-solving.

## Setup

First of all, we need to make sure to include all the necessary dependencies:

    pip install streamlit
    pip install streamlit_chat
    pip install langchain_google_vertexai
    pip install langchain_google_community
    pip install langgraph

Since we are going to use Google Search as one of the tools, we are now going to perform some setup steps for Google Cloud. For fast development, you could for example run this demo application from the GCP Console or from a [Google Cloud Workstation](https://cloud.google.com/workstations/docs).

In the following steps we make sure to authenticate and then set the GCP project we are going to work with:

    gcloud auth application-default login
    gcloud config set project you-project-name
    gcloud auth application-default set-quota-project you-project-name

Next, we need to make sure to have an *.env* file with the following variables setup:

    GOOGLE_CSE_ID=your_actual_cse_id
    GOOGLE_API_KEY=your_actual_api_key

To get the variables values, make sure to activate ***“Custom Search API”*** in your GCP project. In the Cloud Console, go to ***“APIs & Services” -> “Credentials.”*** Click ***“Create Credentials” -> “API key.”*** This will generate your ***GOOGLE_API_KEY***.

To get ***GOOGLE_CSE_ID***, go to the [Custom Search Engine control panel](https://programmablesearchengine.google.com/controlpanel/create). Create a Search Engine, then click customize and the Search engine ID will be your GOOGLE_CSE_ID (Figure 1).

![Figure 1: Search Engine Creation (Image by Author).](https://cdn-images-1.medium.com/max/4360/1*8HZfYSWIIIzrwCmo7OhHvQ.png)<br>Figure 1: Search Engine Creation (Image by Author).

## Demonstration

### Setup and Initialization

First, we need to set up our environment and initialize the necessary components:

````python
import streamlit as st
from streamlit_chat import message
import os
import re
import uuid
import queue
from typing import Annotated
from langchain_google_vertexai import ChatVertexAI
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.messages import HumanMessage, AIMessage
from typing_extensions import TypedDict
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import Tool
from langchain_core.tools import tool
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.environ.get("GOOGLE_CSE_ID") 
os.environ["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "graph" not in st.session_state:
    st.session_state.graph = None
if "waiting_for_human" not in st.session_state:
    st.session_state.waiting_for_human = False
if "human_response" not in st.session_state:
    st.session_state.human_response = None
if "form_id" not in st.session_state:
    st.session_state.form_id = str(uuid.uuid4())

# Initialize memory for LangGraph
memory = MemorySaver()
````

Particularly we use Streamlit session state to store:

* ***messages***: A list to keep track of the conversation history.

* ***graph***: The compiled LangGraph instance.

* ***waiting_for_human***: A boolean flag indicating whether the chatbot is waiting for human input.

* ***human_response***: Stores the human expert’s input.

* ***form_id***: A unique ID for the human intervention form.

And initialize MemorySaver, which will be used as a checkpointer for our LangGraph to store and retrieve the conversation state.

### Defining Tools and the Uncertainty Detection Function

Next, we define the tools our chatbot can use and the crucial function for detecting uncertainty in the LLM’s responses:

````python
class State(TypedDict):
    messages: Annotated[list, add_messages]

@tool
def replace_sim(phone_model: str):
    """Provides instructions for replacing a SIM card in a specific phone model."""
    instructions = {
        "iPhone 13": "1. Power off your iPhone 13. \n2. Locate the SIM tray on the right side of the phone. \n 3. Use a SIM ejector tool (or a small paperclip) to insert into the small hole on the SIM tray. \n4. Gently push until the tray pops out. \n 5. Remove the old SIM card from the tray and place the new SIM card in the tray. \n6. Insert the SIM tray back into the phone. \n7. Power on your iPhone 13.",
        "Samsung Galaxy S21": "1. Power off your Samsung Galaxy S21. \n2. Locate the SIM tray on the top of the phone. \n 3. Use a SIM ejector tool (or a small paperclip) to insert into the small hole on the SIM tray. \n 4. Gently push until the tray pops out. \n 5. Remove the old SIM card from the tray and place the new SIM card in the tray. \n 6. Insert the SIM tray back into the phone. \n7. Power on your Samsung Galaxy S21.",
        "Google Pixel 7": "1. Power off your Google Pixel 7. \n2. Locate the SIM tray on the left side of the phone. \n 3. Use a SIM ejector tool (or a small paperclip) to insert into the small hole on the SIM tray. \n 4. Gently push until the tray pops out. \n5. Remove the old SIM card from the tray and place the new SIM card in the tray, making sure it's aligned correctly. \n 6. Insert the SIM tray back into the phone. \n7. Power on your Google Pixel 7.",
        "OnePlus 10 Pro": "1. Power off your OnePlus 10 Pro. \n2. Locate the SIM tray on the left side of the phone. \n3. Use a SIM ejector tool (or a small paperclip) to insert into the small hole on the SIM tray. \n 4. Gently push until the tray pops out. \n5. Remove the old SIM card from the tray and place the new SIM card in the tray. \n6. Insert the SIM tray back into the phone. \n7. Power on your OnePlus 10 Pro.",
        "Xiaomi 12": "1. Power off your Xiaomi 12. \n2. Locate the SIM tray on the left side of the phone. \n3. Use a SIM ejector tool (or a small paperclip) to insert into the small hole on the SIM tray. \n 4. Gently push until the tray pops out. \n5. Remove the old SIM card from the tray and place the new SIM card in the tray. \n6. Insert the SIM tray back into the phone. \n7. Power on your Xiaomi 12."
    }
    return instructions.get(phone_model, "Sorry, I don't have instructions for that phone model yet.")

# Initialize Google Search tool
search = GoogleSearchAPIWrapper()
search_tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

def is_uncertain(llm_response: str) -> bool:
    """
    Determines if an LLM response indicates uncertainty or inability to provide accurate information.
    
    Args:
        llm_response (str): The response text from the LLM to analyze
        
    Returns:
        bool: True if uncertainty is detected, False otherwise
    """
    # Normalize input text
    normalized_text = llm_response.lower().strip()
    
    # Direct uncertainty indicators
    basic_uncertainty_terms = {
        "epistemic": [
            "not sure",
            "don't know",
            "do not know",
            "doubt",
            "unable to confirm",
            "unable to determine"
        ],
        
        "hedging": [
            "might",
            "may",
            "could",
            "possibly",
            "somewhat"
        ],
        
        "limitation": [
            "limited access",
            "limited information",
            "outside my knowledge"
        ]
    }
    
    # Complex regex patterns for more nuanced uncertainty expressions
    uncertainty_patterns = [
        # Hedging patterns
        r"I (?:think|believe|suppose|assume|guess|imagine|suspect) (?:that )?(?:it )?might be",
        
        # Explicit uncertainty
        r"I['']m not (?:entirely|completely|totally|fully|absolutely|quite|really) (?:sure|certain|confident)",
        
        # Model self-reference
        r"(?:As|Being) (?:an?|the) (?:AI|language model|LLM|assistant)",
        
        # Knowledge limitations
        r"(?:This|That) (?:is|seems to be) (?:beyond|outside) (?:my|the) (?:scope|capability|knowledge|understanding)",
        
        # Complexity acknowledgment
        r"(?:This|That|The question|The matter|The issue|The topic) (?:is|seems) (?:too |quite |very |extremely )?complex",
        
        # Request for clarification
        r"Can you (?:please |kindly )?(?:be more specific|provide more context)"
    ]
    
    # Disclaimer statements
    disclaimer_patterns = [
        r"I am (?:a large )?(?:language model|AI|artificial intelligence)",
        r"For (?:safety|ethical|security) reasons"
    ]
    
    # Check basic uncertainty terms
    for category, terms in basic_uncertainty_terms.items():
        if any(term in normalized_text for term in terms):
            return True
    
    # Check complex uncertainty patterns
    if any(re.search(pattern, llm_response, re.IGNORECASE) for pattern in uncertainty_patterns):
        return True
        
    # Check disclaimer patterns
    if any(re.search(pattern, llm_response, re.IGNORECASE) for pattern in disclaimer_patterns):
        return True
        
    # Check for multiple hedging terms in close proximity
    hedging_terms = basic_uncertainty_terms["hedging"]
    hedging_count = sum(1 for term in hedging_terms if term in normalized_text)
    if hedging_count >= 2:  # Multiple hedging terms indicate higher uncertainty
        return True
    
    return False
````

To summarize, the key 3 tools the AI chatbot will be provided with are:

* ***replace_sim***: This custom tool, decorated with ***@tool***, provides instructions for SIM card replacement. It uses a dictionary to store instructions for various phone models. This is a simple example of how an agent could interact with a company knowledge base.

* ***search_tool***: This tool utilizes the *GoogleSearchAPIWrapper* to perform Google searches.

* ***is_uncertain***: This function is the core of our self-improvement mechanism. It analyzes the LLM’s response (***llm_response***) and returns True if it detects uncertainty, False otherwise.

### Implementing the Human-in-the-Loop Mechanism

This section defines the components that handle human intervention:

````python
class HumanInterventionHandler(BaseCallbackHandler):
    def on_llm_end(self, response, **kwargs):
        if is_uncertain(response.generations[0][0].text):
            st.session_state.human_input_requested = True
            st.session_state.pending_human_input = True
            st.session_state.uncertain_response = response.generations[0][0].text

human_intervention_handler = HumanInterventionHandler()

# Initialize LLM with the handler
llm = ChatVertexAI(
    model_name="gemini-pro",
    callbacks=[human_intervention_handler]
)
llm_with_tools = llm.bind_tools([search_tool, replace_sim])

def process_human_intervention():
    """
    Handle human intervention input and update chat history.
    Pre-populates the form with the LLM's uncertain response.
    """
    if st.session_state.waiting_for_human:
        # Get the stored uncertain response
        initial_response = st.session_state.get("uncertain_response", "")
        
        with st.form(key=f"human_intervention_form_{st.session_state.form_id}"):
            st.markdown("The AI provided this response but wasn't confident. 
                            Please review and modify as needed:")
            human_input = st.text_area(
                "Expert Review:",
                value=initial_response,
                height=200
            )
            
            # Add guidance for the expert
            st.markdown("""
            Please:
            1. Review the AI's response above
            2. Correct any inaccuracies
            3. Add any missing information
            4. Remove any uncertain language
            """)
            
            submitted = st.form_submit_button("Submit Expert Review")
            
            if submitted and human_input:
                # Add human response to chat history
                st.session_state.messages.append({
                    "role": "human-expert",
                    "content": human_input
                })
                st.session_state.human_response = human_input
                st.session_state.waiting_for_human = False
                # Clear the stored uncertain response
                st.session_state.uncertain_response = None
                st.session_state.form_id = str(uuid.uuid4())
                st.rerun()
                return True
    return False

def human_intervention(state: State):
    """
    Handle human intervention in the conversation flow.
    Manages the transition between AI uncertainty and human expert input.
    """
    if not st.session_state.waiting_for_human:
        st.session_state.waiting_for_human = True
        return {"messages": [AIMessage(content="Requesting expert review...")]}
    
    if st.session_state.human_response:
        response = st.session_state.human_response
        st.session_state.human_response = None
        return {"messages": [HumanMessage(content=response)]}
    
    return {"messages": []}
````

### Chatbot Logic and Graph Construction

At this point, we are ready to define the main chatbot flow:

````python
def chatbot(state: State):
    """
    Main chatbot logic with enhanced uncertainty handling.
    """
    if st.session_state.waiting_for_human:
        return {"messages": []}
        
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    
    if is_uncertain(response.content):
        st.session_state.waiting_for_human = True
        # Store the uncertain response for the intervention form
        st.session_state.uncertain_response = response.content
        st.session_state.messages.append({
            "role": "assistant",
            "content": "I'm not completely confident about this response. 
                        Requesting expert review..."
        })
        return {"messages": [AIMessage(content="Requesting expert review...")]}
    
    return {"messages": [response]}
````

And Langgraph graph:

````python
def route_tools(state: State):
    """Modified routing to handle waiting states"""
    if st.session_state.waiting_for_human:
        return "human_intervention"
        
    if not state["messages"]:
        return END
        
    last_message = state["messages"][-1]
    
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        tool_name = last_message.tool_calls[0]["name"]
        return tool_name
        
    return END

# Create graph builder
if st.session_state.graph is None:
    graph_builder = StateGraph(State)
    
    # Add nodes
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("google_search", ToolNode([search_tool]))
    graph_builder.add_node("replace_sim", ToolNode([replace_sim]))
    graph_builder.add_node("human_intervention", human_intervention)
    
    # Add edges
    graph_builder.add_conditional_edges(
        "chatbot",
        route_tools,
        {
            "google_search": "google_search",
            "replace_sim": "replace_sim",
            "human_intervention": "human_intervention",
            END: END
        }
    )
    
    graph_builder.add_edge("google_search", "chatbot")
    graph_builder.add_edge("replace_sim", "chatbot")
    graph_builder.add_edge("human_intervention", "chatbot")
    
    graph_builder.set_entry_point("chatbot")
    graph = graph_builder.compile(checkpointer=memory)
    # Store the graph in session state
    st.session_state.graph = graph
else:
    graph = st.session_state.graph
````

### Streamlit UI

The last step left is then to build the Streamlit user interface:

````python
# Streamlit UI
st.title("LangGraph Chatbot")
st.image(graph.get_graph().draw_mermaid_png(), caption="LangGraph Visualization", use_container_width=True) 

# Custom CSS to style different message types
st.markdown("""
    <style>
    .human-expert {
        background-color: #e6f3ff;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Process any pending human intervention first
process_human_intervention()

# Chat interface with improved message display
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    
    # Handle different message types
    if role == "human-expert":
        with st.chat_message("assistant", avatar="👨‍💼"):
            st.markdown(content)
    elif role == "user":
        with st.chat_message("user"):
            st.markdown(content)
    else:  # assistant
        with st.chat_message("assistant"):
            st.markdown(content)

# Only show chat input if not waiting for human intervention
if not st.session_state.waiting_for_human:
    if prompt := st.chat_input("What's up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Process through graph
        try:
            for event in st.session_state.graph.stream(
                {"messages": [HumanMessage(content=prompt)]},
                config={"configurable": {"thread_id": "1"}}
            ):
                for value in event.values():
                    if value.get("messages"):
                        response = value["messages"][-1].content
                        if not st.session_state.waiting_for_human:
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": response
                            })
                            with st.chat_message("assistant"):
                                st.markdown(response)
                        
                        # Check if we need to stop for human intervention
                        if st.session_state.waiting_for_human:
                            st.rerun()  # Trigger a rerun to show the intervention form
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.session_state.waiting_for_human = False  # Reset state in case of error
else:
    st.warning("Please provide expert input above to continue the conversation.")
````

### Putting everything together

Finally, we are now ready to lunch the application!

    streamlit run app.py
    # or the following command if using Cloud Workstations:
    streamlit run app.py   --browser.serverAddress=localhost   --server.enableCORS=false   --server.enableXsrfProtection=false   --server.port 8080

Asking questions on how to replace SIMs for specific models, should successfully trigger our knowledge base, using queries asking to *search for informations* or *get latest news* about something will trigger instead the Google Search capabilities and whenever the LLM is unsure, the drafted response will appear on screen and an human expert will be able to edit it before sending it to the end user (Figure 2). Whenever the SIM and Google Search tools are used, the different thinking steps of the Chatbot will be displayed on screen to show the end to end thinking process:

 1. First an empty message appears since the chatbot understood it needs to use a tool and not reply.

 2. Then the raw response from the SIM tool or Google Search is displayed.

 3. Finally, the polished response of the Chatbot using the tool context is shown as a final response to the end user.

![Figure 2: Chatbot in action! (Image by Author).](https://cdn-images-1.medium.com/max/3228/1*T_w3AVYx9V2w6s8F4BSWnQ.gif)<br>Figure 2: Chatbot in action! (Image by Author).

## Conclusion

This short tutorial demonstrated how Langgchain can be used to create a simple workflow with human in the loop and different tool capabilities. Although, this is just the beginning! Using this base, feel free to develop more sophisticated logic to handle the human intervention or add other GCP services (e.g. an actual knowledge base powered by Vertex AI search).
