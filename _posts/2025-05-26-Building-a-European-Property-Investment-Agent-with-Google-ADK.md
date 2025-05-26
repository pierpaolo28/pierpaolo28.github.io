---
title: Building a European Property Investment Agent with Google ADK
layout: post
permalink: blog/blog91/
categories: [Generative AI]
---

![Agent Development Kit Frontend (Image by Author).](https://cdn-images-1.medium.com/max/4436/1*3dS_wVpwQBM5HTs3lJaMfQ.png)<br>Agent Development Kit Frontend (Image by Author).

<!--end_excerpt-->

## Building a European Property Investment Agent with Google ADK

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
            This is a guest post originally published on <a href="https://medium.com/p/ac2e27a6098b" target="_blank">Google Cloud - Community</a>.
        </ul>
        </td>
    </tr>
    </tbody>
</table>

### End to end demonstration on how to build AI Agents using Google Agent Development Kit

The world of AI agents is rapidly evolving, offering exciting possibilities for automating tasks and providing specialized assistance. In fields like finance and investment, where analyzing vast amounts of dynamic data is crucial, AI agents can act as powerful assistants, sifting through information, identifying trends, and providing tailored insights. [Google’s Agent Development Kit (ADK)](https://google.github.io/adk-docs/) is a powerful framework designed to help developers build, test, and deploy these sophisticated agents with relative ease. In this post, we’ll walk through a practical example: creating a simple, yet illustrative, agent capable of providing insights into European property investment hotspots and economic outlooks. This project demonstrates how to structure an agent using the ADK’s core concepts to handle specific domain-related queries.

## What is Google ADK?

The Google Agent Development Kit (ADK) is a robust framework that simplifies the process of building AI agents powered by large language models (LLMs). At its heart, the ADK provides a structured way to define an agent’s capabilities. It allows developers to specify the LLM model the agent will use, provide clear instructions on how the agent should behave, and equip it with “tools” — essentially, functions or APIs the agent can call to perform specific actions or retrieve external information.

One of the key strengths of the ADK is its support for creating hierarchies of agents. This pattern, often referred to as a “coordinator-worker” or “orchestrator” pattern, allows you to build complex agents by breaking down capabilities into smaller, more manageable specialized agents. A high-level “coordinator” agent receives the initial user query, understands the user’s intent, and then delegates the task to the most appropriate “worker” agent. This modular approach makes agents easier to develop, debug, and scale, as each worker agent can be focused on a specific domain or task, equipped with only the tools it needs. This contrasts with building a single, monolithic agent that tries to handle everything, which can quickly become unwieldy.

## Setting Up Your Environment

Before we dive into the code that defines our European property investment agent, you need to set up your development environment. For this demonstration, I utilized a [Google Cloud Workstation](https://cloud.google.com/workstations/docs), which offers a convenient, pre-configured cloud-based environment, saving the hassle of local setup complexities. However, you can also set this up on a local machine with Python installed.

### Install the Google ADK

Open your terminal or Cloud Workstation command line and run the following command to install the necessary Python library from PyPI:

    pip install google-adk

This command fetches and installs the core ADK library and its dependencies, giving you access to the classes and functions needed to define your agents and tools.

### Authenticate with Google Cloud

If you plan to use Google Cloud services, such as Vertex AI for accessing powerful LLMs like Gemini, you’ll need to authenticate your development environment. This command sets up your application default credentials, allowing your code running in the environment to access Google Cloud resources securely:

    gcloud auth application-default login

Follow the prompts to log in with your Google account. This step is crucial if GOOGLE_GENAI_USE_VERTEXAI is set to "TRUE" in your environment configuration.

## Project Structure

Our project is organized within a standard Python package structure. The main code resides in a folder named europe_property_investor. Inside this folder, we have a few key files that define our agent and its configuration:

    europe_property_investor/
    ├── .env
    ├── __init__.py
    └── agent.py

This structure is clean and follows Python best practices for creating reusable modules.

Let’s look at the purpose of each file:

### .env

This file is used to store environment variables that configure our agent’s runtime behavior, particularly its connection to Google Cloud services. Using a .env file is a common practice for managing configuration settings separately from your code, making it easy to change settings without modifying the core logic.

    GOOGLE_CLOUD_PROJECT="TODO" # Replace TODO with your Google Cloud Project ID
    GOOGLE_CLOUD_LOCATION="us-central1" # e.g., us-central1 or europe-west1
    GOOGLE_GENAI_USE_VERTEXAI="TRUE"

You **must** replace "TODO" with your actual Google Cloud Project ID. The GOOGLE_CLOUD_LOCATION specifies the region for Vertex AI, and GOOGLE_GENAI_USE_VERTEXAI="TRUE" tells the ADK to use Vertex AI for accessing the Gemini model, rather than the public GenAI API.

### __init__.py

This file is essential for Python to recognize the europe_property_investor directory as a package. It can also be used to control which objects are exposed when the package is imported. In our simple case, it primarily serves to make the main root_agent directly accessible from the package level.

````python
from . import agent
from .agent import root_agent
````

By importing root_agent here, we can easily refer to our main agent when running the ADK web interface command later.

### agent.py

This is the core of our agent application. It contains all the definitions for the tools our agent can use, the specialized “worker” agents that handle specific tasks, and the main “coordinator” agent that acts as the entry point for user interactions and orchestrates the flow by delegating tasks to the appropriate workers.

Let’s break down the key components within agent.py:

### Imports and Configuration

We begin by importing the necessary classes from the google.adk library, as well as standard Python typing utilities. We also define the specific LLM model we intend to use.

````python
import os
from google.adk.agents import Agent 
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search
from typing import TypedDict, List, Optional, Dict, Any

MODEL_NAME = "gemini-2.0-flash" 
````

Using gemini-2.0-flash provides a good balance of performance and cost-effectiveness for many agent tasks. You could experiment with other models depending on your specific needs and budget.

### TypedDict Definitions

TypedDict from the typing module is a powerful feature that allows us to define dictionaries with specific keys and value types. While not strictly required by the ADK, using TypedDict for the output of our tools is highly recommended. It serves as clear documentation for the structure of the data the tool returns, which is invaluable for maintainability. Crucially, this type information is also provided to the LLM, helping it better understand the data it receives from tool calls and improving its ability to process and respond based on that data.

````python
# --- TypedDict Definitions (Shared by relevant agents/tools) ---
class PropertyHotspot(TypedDict):
    location: str
    country: str
    property_types_favored: List[str]
    reasoning: str
    potential_appreciation_outlook: str
    average_rental_yield_pa: Optional[str]
    market_sentiment: str
    risk_level: str
    key_drivers: List[str]
    potential_headwinds: List[str]
    investment_horizon_suitability_years: str
    data_source_year: str

class EconomicOutlook(TypedDict):
    country: str
    gdp_growth_forecast_pa: str
    inflation_rate_pa: str
    stability_assessment: str
    key_economic_notes: List[str]
    data_source_year: str
````

These definitions clearly outline the expected data fields for property hotspots and economic outlooks, making the code more readable and helping the LLM interpret the tool results accurately.

### Tool Function Definitions

These are standard Python functions that encapsulate specific capabilities our agent needs. The ADK allows the LLM to call these functions dynamically based on the user’s request and the agent’s instructions. In a real-world application, these functions would typically interact with external services, databases, or APIs to fetch real-time data or perform actions. For this demonstration, we use simple mock data stored directly within the functions to simulate the tool’s behavior.

* get_european_property_hotspots: This function simulates fetching information about promising European real estate investment locations. It accepts parameters that allow filtering by countries, investment horizon, risk appetite, and property type focus, demonstrating how the LLM can pass arguments to tools.

````python
def get_european_property_hotspots(
    countries_of_interest: Optional[List[str]] = None,
    investment_horizon_years: Optional[int] = None,
    risk_appetite: Optional[str] = None,
    property_type_focus: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Fetches detailed information on promising European real estate investment locations.
    This tool can be filtered by countries, investment horizon, risk appetite, and property type focus.
    Returns a list of dictionaries, each representing a property hotspot with detailed attributes.
    """
    print(
        f"Tool (get_european_property_hotspots) called with countries: {countries_of_interest}, "
        f"horizon: {investment_horizon_years} years, risk: {risk_appetite}, types: {property_type_focus}"
    )
    all_hotspots_data: List[PropertyHotspot] = [
        {
            "location": "Lisbon (Principe Real, Alfama)", "country": "Portugal",
            "property_types_favored": ["Renovated Apartments", "Luxury Residences", "Residential"],
            "reasoning": "Sustained international demand, strong tourism, tech hub growth. Prime areas continue to appreciate.",
            "potential_appreciation_outlook": "High (6-9% annually in prime zones)", "average_rental_yield_pa": "3-4.5%",
            "market_sentiment": "Positive", "risk_level": "Medium",
            "key_drivers": ["Golden Visa (historic impact)", "Tech sector", "Tourism", "Lifestyle appeal"],
            "potential_headwinds": ["Rising prices affecting affordability", "Regulatory changes for short-term rentals"],
            "investment_horizon_suitability_years": "5-10", "data_source_year": "2025 Q1"
        },
        {
            "location": "Porto (Cedofeita, Bonfim)", "country": "Portugal",
            "property_types_favored": ["Residential Apartments", "Guesthouses", "Residential"],
            "reasoning": "More affordable than Lisbon with significant growth, vibrant culture, and increasing tourism.",
            "potential_appreciation_outlook": "High (7-10% annually)", "average_rental_yield_pa": "4-6%",
            "market_sentiment": "Very Positive", "risk_level": "Medium",
            "key_drivers": ["Tourism growth", "Urban regeneration", "Lower entry point than Lisbon"],
            "potential_headwinds": ["Infrastructure strain with growth", "Increased competition"],
            "investment_horizon_suitability_years": "5-7", "data_source_year": "2025 Q1"
        },
        {
            "location": "Valencia (Ruzafa, El Cabanyal)", "country": "Spain",
            "property_types_favored": ["Beachfront properties (El Cabanyal)", "Modern Apartments (Ruzafa)", "Residential", "Vacation"],
            "reasoning": "Excellent quality of life, growing tech scene, more affordable than Barcelona/Madrid. Coastal regeneration.",
            "potential_appreciation_outlook": "Medium-High (5-8% annually)", "average_rental_yield_pa": "4-5.5%",
            "market_sentiment": "Positive", "risk_level": "Medium",
            "key_drivers": ["Lifestyle", "Tech investment", "Tourism", "University city"],
            "potential_headwinds": ["Some areas saturated", "Local rental regulations"],
            "investment_horizon_suitability_years": "3-7", "data_source_year": "2025 Q1"
        },
        {
            "location": "Malaga City", "country": "Spain",
            "property_types_favored": ["City center apartments", "Properties near tech park", "Residential", "Vacation"],
            "reasoning": "Significant urban renewal, cultural hub, growing tech presence beyond just Costa del Sol tourism.",
            "potential_appreciation_outlook": "Medium-High (5-7% annually)", "average_rental_yield_pa": "4-5%",
            "market_sentiment": "Positive", "risk_level": "Medium-Low",
            "key_drivers": ["Tech hub development", "Cultural tourism", "Infrastructure investment"],
            "potential_headwinds": ["Seasonal tourism dependency in wider region", "Price increases in prime spots"],
            "investment_horizon_suitability_years": "5-10", "data_source_year": "2025 Q1"
        },
        {
            "location": "Athens (Koukaki, Pangrati)", "country": "Greece",
            "property_types_favored": ["Renovated apartments for short/long term let", "Golden Visa eligible properties", "Residential"],
            "reasoning": "Economic recovery, tourism boom, and government incentives. Focus on central, well-connected areas.",
            "potential_appreciation_outlook": "Medium (4-7% annually)", "average_rental_yield_pa": "4-6%",
            "market_sentiment": "Cautiously Optimistic", "risk_level": "Medium-High",
            "key_drivers": ["Tourism", "Golden Visa", "Infrastructure upgrades", "Low starting base"],
            "potential_headwinds": ["Bureaucracy", "Geopolitical factors in region", "Taxation uncertainties"],
            "investment_horizon_suitability_years": "5-7", "data_source_year": "2025 Q1"
        },
        {
            "location": "Warsaw (Mokotów, Srodmiescie)", "country": "Poland",
            "property_types_favored": ["New build apartments", "Buy-to-let residential", "Residential"],
            "reasoning": "Strong domestic economy, increasing foreign investment, major business services hub. Relatively stable.",
            "potential_appreciation_outlook": "Medium (4-6% annually)", "average_rental_yield_pa": "5-6.5%",
            "market_sentiment": "Positive", "risk_level": "Medium-Low",
            "key_drivers": ["Economic growth (pre-war regional stability)", "Business outsourcing", "Young population"],
            "potential_headwinds": ["Regional geopolitical tensions (Ukraine impact)", "Inflationary pressures"],
            "investment_horizon_suitability_years": "5-10", "data_source_year": "2025 Q1"
        },
        {
            "location": "Budapest (District VII, IX)", "country": "Hungary",
            "property_types_favored": ["Renovation projects", "Short-term rental units", "Residential", "Vacation"],
            "reasoning": "Major tourist destination, relatively low prices for a European capital, vibrant culture.",
            "potential_appreciation_outlook": "Medium (3-6% annually)", "average_rental_yield_pa": "4.5-6%",
            "market_sentiment": "Neutral to Cautiously Optimistic", "risk_level": "Medium-High",
            "key_drivers": ["Tourism", "University city", "Foreign investment in specific sectors"],
            "potential_headwinds": ["Government policies", "Currency fluctuations (HUF)", "Oversupply in certain rental segments"],
            "investment_horizon_suitability_years": "3-7", "data_source_year": "2025 Q1"
        }
    ]
    filtered_hotspots_data = all_hotspots_data
    if countries_of_interest:
        filtered_hotspots_data = [
            spot for spot in filtered_hotspots_data
            if spot["country"].lower() in [country.lower() for country in countries_of_interest]
        ]
    if risk_appetite:
        normalized_risk_appetite = risk_appetite.lower()
        if "low" in normalized_risk_appetite: risk_levels_to_match = ["low", "medium-low"]
        elif "high" in normalized_risk_appetite: risk_levels_to_match = ["high", "medium-high"]
        elif "medium" in normalized_risk_appetite: risk_levels_to_match = ["medium", "medium-low", "medium-high"]
        else: risk_levels_to_match = [normalized_risk_appetite]
        filtered_hotspots_data = [spot for spot in filtered_hotspots_data if spot["risk_level"].lower() in risk_levels_to_match]
    if property_type_focus:
        temp_filtered = []
        normalized_property_type_focus = [ptf.lower() for ptf in property_type_focus]
        for spot in filtered_hotspots_data:
            spot_favored_types_lower = [fav_type.lower() for fav_type in spot["property_types_favored"]]
            if any(focused_type in spot_favored_types_lower for focused_type in normalized_property_type_focus):
                temp_filtered.append(spot)
        filtered_hotspots_data = temp_filtered

    if not filtered_hotspots_data:
        criteria_summary = []
        if countries_of_interest: criteria_summary.append(f"countries: {', '.join(countries_of_interest)}")
        if investment_horizon_years is not None: criteria_summary.append(f"horizon: {investment_horizon_years} years")
        if risk_appetite: criteria_summary.append(f"risk: {risk_appetite}")
        if property_type_focus: criteria_summary.append(f"types: {', '.join(property_type_focus)}")
        reasoning_message = "No specific hotspots found matching all criteria: " + "; ".join(criteria_summary) + f". Current data from {all_hotspots_data[0]['data_source_year'] if all_hotspots_data else 'N/A'}."
        return [{"location": "N/A", "country": "N/A", "property_types_favored": [], "reasoning": reasoning_message, "potential_appreciation_outlook": "N/A", "average_rental_yield_pa": "N/A", "market_sentiment": "N/A", "risk_level": "N/A", "key_drivers": [], "potential_headwinds": [], "investment_horizon_suitability_years": "N/A", "data_source_year": "N/A"}]
    
    return filtered_hotspots_data
````

The print statement inside the function is a simple way to see when the tool is called and what arguments the LLM provides, which is helpful for debugging. The filtering logic demonstrates how a real tool might process parameters to refine its results.

* get_country_economic_outlook: This function simulates retrieving economic data for a given European country.

````python
def get_country_economic_outlook(country: str) -> Dict[str, Any]:
    """
    Provides a brief economic outlook (GDP growth, inflation, stability)
    for a specified European country. Returns a dictionary containing economic details.
    """
    print(f"Tool (get_country_economic_outlook) called for {country}")
    outlooks_data: Dict[str, EconomicOutlook] = {
        "portugal": {"country": "Portugal", "gdp_growth_forecast_pa": "1.8%", "inflation_rate_pa": "2.5%", "stability_assessment": "Moderately Stable", "key_economic_notes": ["Tourism dependent", "EU recovery funds boosting investment", "Focus on tech growth"], "data_source_year": "2025 H1"},
        "spain": {"country": "Spain", "gdp_growth_forecast_pa": "2.1%", "inflation_rate_pa": "2.8%", "stability_assessment": "Moderately Stable", "key_economic_notes": ["Strong tourism rebound", "Renewable energy investment", "Regional disparities"], "data_source_year": "2025 H1"},
        "greece": {"country": "Greece", "gdp_growth_forecast_pa": "2.5%", "inflation_rate_pa": "3.2%", "stability_assessment": "Improving", "key_economic_notes": ["Post-bailout recovery", "Investment in infrastructure", "High national debt remains a concern"], "data_source_year": "2025 H1"},
        "poland": {"country": "Poland", "gdp_growth_forecast_pa": "3.0%", "inflation_rate_pa": "4.5%", "stability_assessment": "Stable but watchful (geopolitics)", "key_economic_notes": ["Strong manufacturing base", "Proximity to Ukraine war poses some risk/impact", "EU funding utilization key"], "data_source_year": "2025 H1"},
        "hungary": {"country": "Hungary", "gdp_growth_forecast_pa": "2.2%", "inflation_rate_pa": "5.0%", "stability_assessment": "Moderately Stable with political variables", "key_economic_notes": ["Dependent on foreign manufacturing (automotive)", "EU funds disputes", "Forint volatility"], "data_source_year": "2025 H1"}
    }
    result_data = outlooks_data.get(country.lower())
    
    if result_data:
        return result_data 
    else:
        return {
            "country": country, "gdp_growth_forecast_pa": "N/A", "inflation_rate_pa": "N/A", 
            "stability_assessment": "Data not available in mock set", 
            "key_economic_notes": ["No specific data for this country in the current simulated dataset."], 
            "data_source_year": "N/A"
        }
````

Again, this uses mock data but illustrates how a tool would take a specific input (a country name) and return structured information.

### Worker Agent Definitions

Worker agents are specialized agents designed to handle specific types of queries by utilizing a limited set of relevant tools. This specialization makes their instructions simpler and their behavior more predictable for their specific domain.

* property_hotspots_agent: This agent is solely focused on providing information about property investment locations. It is equipped with only the get_european_property_hotspots tool. Its instruction guides it to use this tool based on the criteria provided by the user.

````python
property_hotspots_agent = Agent(
    name="PropertyHotspotsAgent",
    model=MODEL_NAME,
    instruction="You are a specialist in European property hotspots. You have one tool to find detailed property investment locations. Use it based on the user's criteria (countries, investment horizon, risk appetite, property type focus).",
    description="Provides detailed information on promising European real estate investment locations.",
    tools=[get_european_property_hotspots] 
)
````

Its instruction is concise and directly relates to the capability of its single tool.

* economic_outlook_agent: This agent specializes in providing economic summaries for countries. It is equipped with only the get_country_economic_outlook tool.

````python
economic_outlook_agent = Agent(
    name="EconomicOutlookAgent",
    model=MODEL_NAME,
    instruction="You are a specialist in European country economic outlooks. You have one tool to fetch economic data (GDP, inflation, stability) for a given country.",
    description="Provides a brief economic outlook for a specified European country.",
    tools=[get_country_economic_outlook] 
)
````

Similarly, its instruction is tailored to the economic outlook domain.

* google_search_agent: This agent serves as a general-purpose fallback for queries that cannot be handled by the more specialized agents. It wraps the standard google_search tool provided by the ADK.

````python
google_search = Agent(
    name="GoogleSearch",
    model=MODEL_NAME,
    instruction="You are a web search assistant. You have one tool for performing Google searches. Use it to find specific, recent information or anything not covered by other specialized agents.",
    description="Performs Google searches for general information or recent news.",
    tools=[google_search], 
)

google_search_grounding = AgentTool(agent=google_search)

google_search_agent = Agent(
    name="GoogleSearchAgent",
    model=MODEL_NAME,
    instruction="Given a query that its not possible to ask using PropertyHotspotsAgent and EconomicOutlookAgent use Google Search to find an answer. If no answer is found, inform the user you don't know the answer. Inform the user, you are using Google Search to reply. If the user asks anything not related to European Property Investment, decline to answer.",
    description="Uses Google search to attempt to answer questions that are not possible to answer using PropertyHotspotsAgent and EconomicOutlookAgent",
    tools=[google_search_grounding]
)
````

This agent’s instruction is crucial — it tells it to *only* use search if the other agents can’t answer and to stay within the domain of European Property Investment.

### Coordinator Agent Definition

The root_agent is the top-level agent and the one directly invoked by the ADK web interface. Its primary role is not to answer queries itself, but to understand the user's intent and delegate the task to the most appropriate specialized worker agent. This is where the orchestration happens.

````python
# --- Coordinator Agent Definition ---
# This is the agent that will be invoked by 'adk web'
root_agent = Agent(
    name="EuropePropertyInvestmentCoordinator",
    model=MODEL_NAME,
    instruction=(
        "You are a coordinator agent for European property investment analysis. "
        "Your role is to understand the user's query and delegate the task to the most appropriate specialized agent. "
        "You have access to the following specialized agents:\n"
        "- **PropertyHotspotsAgent**: Use this agent to find detailed information about specific property investment locations, including filtering by criteria like country, risk, and property type.\n"
        "- **EconomicOutlookAgent**: Use this agent to get the general economic outlook for a specific country (e.g., GDP growth, inflation).\n"
        "- **GoogleSearchAgent**: Use this agent for very recent news, highly specific details not covered by other agents, or broader web searches.\n\n"
        "Follow these steps:\n"
        "1. Analyze the user's query to determine the type of information needed.\n"
        "2. If the query is broad or unclear for a specific task (e.g., 'best investments' without criteria for PropertyHotspotsAgent), ask clarifying questions to get necessary details (like preferred countries, risk appetite, investment horizon, property types).\n"
        "3. Choose the single best specialized agent for the core task. For example, if the user asks for 'property hotspots in Spain with medium risk', delegate to PropertyHotspotsAgent. If they ask 'economic outlook for Portugal', delegate to EconomicOutlookAgent. If they ask 'recent property news in Berlin', delegate to GoogleSearchAgent.\n"
        "4. Clearly state which agent you are delegating to and what you are asking it to do.\n"
        "5. Relay the information from the specialized agent back to the user in a clear and helpful manner.\n"
        "6. If a query requires information from multiple domains (e.g., property hotspots AND economic outlook for those countries), you might need to break it down and call relevant agents sequentially, presenting a synthesized answer. However, for a single user turn, focus on the primary intent and choose one agent if possible, or explain the need for multiple steps."
        "Do not try to use tools directly yourself; your function is to coordinate your sub-agents."
    ),
    description="Coordinates property investment queries by delegating to specialized agents for property hotspots, economic outlooks, and web searches.",
    sub_agents=[
        property_hotspots_agent,
        economic_outlook_agent,
        google_search_agent,
    ]
)
````

The instruction for the root_agent is the most detailed, as it defines the agent's overall strategy for handling user requests. It explicitly lists the available sub-agents and provides a step-by-step process for analyzing the query, asking clarifying questions when needed, selecting the appropriate sub-agent, and relaying the final response. This clear instruction is critical for guiding the LLM's reasoning and delegation process.

## Running the Agent

With the .env, __init__.py, and agent.py files correctly set up in your europe_property_investor directory, you can now run your agent using the ADK command-line interface. Navigate in your terminal to the directory *containing* your europe_property_investor folder and execute the following command:

    adk web

This command does several things: it finds the root_agent defined in your package (thanks to the __init__.py file), initializes it, and starts a local web server. This server provides a simple chat interface in your web browser, allowing you to interact directly with your root_agent.

Once the server is running (usually accessible at [http://localhost:8000](http://localhost:8000)), open your web browser and navigate to the provided address. You'll see a chat window where you can type your queries related to European property investment (Figure 1).

![Figure 1: Live Demonstration of Agent Frontend (Video by Author).](https://cdn-images-1.medium.com/max/3840/1*3hqyXS7WD__KoVla-OkpFA.gif)<br>Figure 1: Live Demonstration of Agent Frontend (Video by Author).

Try typing queries such as:

* “Tell me about property hotspots in Portugal.” (This should trigger the PropertyHotspotsAgent)

* “What is the economic outlook for Spain?” (This should trigger the EconomicOutlookAgent)

* “Find recent news about property market changes in Berlin.” (This should trigger the GoogleSearchAgent)

* “What are the best investment opportunities?” (This should likely prompt the root_agent to ask for clarification, as per its instruction).

Observe how the root_agent processes your request, identifies the relevant information needed, and then delegates the task to the appropriate specialized worker agent. The worker agent will then use its assigned tool (either fetching mock data or performing a simulated search), and the root_agent will present the result back to you in a conversational manner. This interaction loop demonstrates the power of the coordinator-worker pattern in action.

## Conclusion

This practical demonstration using the Google Agent Development Kit illustrates how you can build intelligent agents with structured behavior. By defining specialized tools and organizing agents in a hierarchical coordinator-worker pattern, you can create applications that are modular, maintainable, and capable of handling complex, domain-specific queries.

While this “Europe Property Investor” agent currently uses mock data, it provides a solid foundation. The next steps could involve integrating real-time data sources — such as financial market APIs, real estate listing services, or economic data providers — into the tool functions. You could also expand the capabilities by adding more specialized worker agents and tools, perhaps for analyzing specific property types (commercial, industrial), assessing legal or tax implications, or even performing rudimentary financial modeling. The modularity offered by the ADK makes such expansions significantly more manageable. Experiment with different queries and observe how the root_agent delegates to the worker agents; understanding this flow is key to building more sophisticated agents with the Google ADK!
