---
title: Revolutionizing Claims, from Deepfake Detection to Next-Best-Action
layout: post
permalink: blog/blog97/
categories: [Finance]
---

![Revolutionizing Claims, from Deepfake Detection to Next-Best-Action (Image by Author).](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*4RASX9V2BD-7v4G-feujJQ.png)<br>Revolutionizing Claims, from Deepfake Detection to Next-Best-Action (Image by Author).

<!--end_excerpt-->

## Revolutionizing Claims: From Deepfake Detection to Next-Best-Action

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
            This is a guest post originally published on <a href="https://medium.com/google-cloud/revolutionizing-claims-from-deepfake-detection-to-next-best-action-77f5273a7016" target="_blank">Google Cloud - Community</a>.
        </ul>
        </td>
    </tr>
    </tbody>
</table>

Solving information overload and sophisticated Fraud with Google ADK
--------------------------------------------------------------------

The insurance claims process is a critical juncture for both policyholders and carriers. For policyholders, it’s a moment of need, expecting fair and swift resolution. For carriers, it’s a complex dance between empathy, accuracy, and fraud prevention. However, this vital process is currently facing two formidable challenges: an overwhelming **information overload** from diverse data sources and the insidious rise of **sophisticated fraud**, particularly with AI-generated or tampered evidence.

Manually sifting through mountains of unstructured claim documents, cross-referencing policies, and verifying the authenticity of digital evidence is slow, error-prone, and increasingly insufficient against cunning fraudulent tactics. This bottleneck not only delays legitimate claims but also exposes carriers to significant financial losses from successful fraud attempts. The industry desperately needs a solution that can accelerate legitimate payouts while robustly defending against novel forms of deception.

This article introduces two cutting-edge agent applications, built using the Google Agent Development Kit (ADK) and leveraging advanced GenAI capabilities, designed to revolutionize claims processing:

1.  An “**Investigator Agent**” that acts as a digital forensic expert, capable of detecting tampered or AI-generated evidence, particularly in image formats.
2.  A “**Reasoning Agent**” that intelligently analyzes unstructured claim documents against a vast repository of company policies to recommend the optimal “Next-Best-Action” for each unique claim.

Together, these agents form a powerful, intelligent system that augments human claims adjusters, transforming them from overwhelmed processors into strategic decision-makers.

The Framework: Google Agent Development Kit (ADK)
-------------------------------------------------

To tackle the complexity of claims processing, we need a framework that goes beyond simple LLM API calls. The Google ADK is purpose-built for creating robust, stateful, and auditable agentic workflows. Its key features enable us to construct a sophisticated system:

*   **Agents:** Specialized, intelligent units for distinct tasks. We’ll use LlmAgent for complex reasoning and SequentialAgent to orchestrate our pipeline deterministically.
*   **State Management:** The ADK’s Session object with its shared state dictionary allows agents to communicate and pass crucial claim details — like initial fraud flags or extracted policy clauses — seamlessly through the workflow.
*   **Tools:** Agents are empowered with capabilities beyond text generation. Our agents will use tools to interact with external systems for deepfake detection, vector database lookups, and more.
*   **Structured Output:** ADK’s integration with Pydantic ensures our agents output clean, validated JSON, providing reliable, actionable data for downstream systems or human review.

The Architecture: An Intelligent Claims Processing Pipeline
-----------------------------------------------------------

Our goal is to automate and enhance the critical cognitive steps a human claims adjuster performs. The improved pipeline incorporates the Investigator Agent to preemptively flag fraudulent evidence and the Reasoning Agent to provide intelligent, policy-driven recommendations.

1.  **The Investigator Agent:** Receives initial claim data, including multimedia evidence. It uses specialized tools to analyze digital evidence (e.g., images) for authenticity and flags potential deepfakes or tampering.
2.  **The Reasoning Agent:** Takes the verified claim details (and any fraud flags) and analyzes them against a comprehensive set of company policies and guidelines to recommend the “Next-Best-Action.”
3.  **The Orchestrator:** A root agent (SequentialAgent) manages the flow, ensuring the Investigator Agent runs first, followed by the Reasoning Agent, creating a coherent, end-to-end workflow.

![Figure 1: System Architecture (Image by Author).](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*SAvYqKqMXP0Zckzav1iVBw.png)<br>Figure 1: System Architecture (Image by Author).

Step 1: The Investigator Agent — Detecting Digital Deception
------------------------------------------------------------

The rise of sophisticated AI tools means that digital evidence — especially images — can no longer be trusted at face value. Our Investigator Agent is designed to tackle this challenge head-on. It focuses on verifying the authenticity of submitted images, leveraging advanced techniques to detect tampering or AI generation.

For this tutorial, we’ll simulate a verify_image_authenticity tool. In a real-world scenario, this tool would integrate with services like Google Cloud’s [SynthID](https://deepmind.google/models/synthid/) for detecting AI-generated content or custom Computer Vision models for forensic analysis of image manipulation.

```python
# In agent.py
from typing import Literal, Optional, Any, AsyncGenerator
from pydantic import BaseModel, Field
import asyncio
import os
import json
from google.adk.agents import Agent, SequentialAgent, BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai import types as genai_types
# --- Tools ---
def verify_image_authenticity(image_id: str) -> dict:
    """
    Verifies the authenticity of a given image to detect deepfakes or tampering.
    Args:
        image_id: The unique identifier for the image to be verified.
    Returns:
        dict: A dictionary containing the verification status and details.
              - 'status': "authentic", "tampered", "ai_generated", or "unverifiable".
              - 'confidence': A float representing the confidence score (0.0 to 1.0).
              - 'details': A string with additional findings.
    """
    print(f"--- Tool: verify_image_authenticity called for image_id: {image_id} ---")
    # Simulate API call to an image analysis service (e.g., SynthID, custom CV model)
    if image_id == "claim_123_evidence_fake.jpg":
        return {
            "status": "ai_generated",
            "confidence": 0.95,
            "details": "High confidence that the image contains AI-generated elements consistent with deepfake manipulation."
        }
    elif image_id == "claim_456_evidence_tampered.png":
        return {
            "status": "tampered",
            "confidence": 0.88,
            "details": "Image metadata indicates post-processing and pixel anomalies consistent with tampering."
        }
    else:
        return {
            "status": "authentic",
            "confidence": 0.99,
            "details": "No signs of tampering or AI generation detected."
        }
# --- Agents ---
class InvestigatorAgent(BaseAgent):
    """
    Agent responsible for analyzing digital evidence (e.g., images) for authenticity.
    Uses specialized tools for deepfake detection and tampering analysis.
    """
    image_verification_tool: Any
    def __init__(self, name: str, image_verification_tool: Any):
        super().__init__(name=name)
        self.image_verification_tool = image_verification_tool
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        claim_evidence = ctx.session.state.get("claim_evidence", {})
        image_id = claim_evidence.get("image_id")
        if not image_id:
            ctx.session.state["evidence_status"] = "no_image_submitted"
            ctx.session.state["fraud_flags"] = False
            yield Event(author=self.name, content=genai_types.Content(parts=[genai_types.Part(text="No image evidence submitted.")]))
            return
        verification_result = self.image_verification_tool(image_id=image_id)
        ctx.session.state["evidence_status"] = verification_result["status"]
        ctx.session.state["fraud_flags"] = (verification_result["status"] != "authentic")
        yield Event(author=self.name, content=genai_types.Content(parts=[genai_types.Part(
            text=f"Image verification complete. Status: {verification_result['status'].upper()}, Confidence: {verification_result['confidence']:.2f}. Details: {verification_result['details']}"
        )]))
investigator_agent = InvestigatorAgent(
    name="InvestigatorAgent",
    image_verification_tool=verify_image_authenticity
)
```

Step 2: The Reasoning Agent — Policy-Driven Next-Best-Action
------------------------------------------------------------

Once the authenticity of the evidence is assessed, the core task of claims processing begins: understanding the claim details in light of company policies to determine the appropriate course of action. Our Reasoning Agent excels here, combining document analysis with intelligent policy retrieval.

It uses two main tools/capabilities:

1.  A simulated retrieve_policy_documents tool: In a real implementation, this would connect to a [Vector AI Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) database. This tool dynamically fetches relevant policy clauses or guidelines based on the claim type and details.
2.  An LlmAgent: Leveraging a powerful LLM, it processes the claim narrative, the retrieved policy documents, and any fraud flags from the Investigator Agent to recommend a precise “Next-Best-Action.”

```python
# Continuing in agent.py...
# --- Pydantic Schemas ---
class ClaimDetails(BaseModel):
    claim_id: str = Field(description="The unique identifier for the claim.")
    claim_type: Literal["auto", "home", "medical"] = Field(description="The type of the insurance claim.")
    description: str = Field(description="A brief description of the incident.")
    policy_number: str = Field(description="The policy number associated with the claim.")
    reported_damage: str = Field(description="Details of the reported damage or loss.")
class NextBestAction(BaseModel):
    recommended_action: str = Field(description="The recommended next step for claims processing.")
    reason: str = Field(description="The reasoning behind the recommended action, citing policy context.")
    urgency: Literal["low", "medium", "high"] = Field(description="The urgency level of the recommended action.")
    flag_for_human_review: bool = Field(description="True if human review is strongly recommended, otherwise False.")
# --- Tools ---
def retrieve_policy_documents(claim_type: str, relevant_keywords: list[str]) -> dict:
    """
    Retrieves relevant policy documents or clauses from a Vector AI Search database.
    Args:
        claim_type: The type of claim (e.g., "auto", "home", "medical").
        relevant_keywords: Keywords extracted from the claim description to find matching policies.
    Returns:
        dict: A dictionary containing 'status', 'policies_found' (list of relevant policy texts), and 'details'.
    """
    print(f"--- Tool: retrieve_policy_documents called for claim_type: {claim_type}, keywords: {relevant_keywords} ---")
    # Simulate Vector AI Search lookup
    if "fraud" in [k.lower() for k in relevant_keywords]:
        return {
            "status": "success",
            "policies_found": [                "Policy-FRAUD-001: All claims with a 'fraud_flag' must undergo secondary review by a senior adjuster.",
                "Policy-INVESTIGATION-005: Deepfake or AI-generated evidence requires immediate claim suspension and referral to the special investigations unit."
            ],
            "details": "Anti-fraud policies retrieved based on keywords."
        }
    elif claim_type == "auto" and "accident" in [k.lower() for k in relevant_keywords]:
        return {
            "status": "success",
            "policies_found": [                "Policy-AUTO-010: Auto accident claims require a police report and damage assessment.",
                "Policy-PAYOUT-003: Minor damage claims (< $5000) can be fast-tracked for approval."
            ],
            "details": "Auto accident policies retrieved."
        }
    else:
        return {
            "status": "success",
            "policies_found": ["General Policy-001: Process all claims fairly and promptly."],
            "details": "General policies retrieved."
        }
# --- Agents ---
reasoning_agent = Agent(
    name="ReasoningAgent",
    model="gemini-2.5-flash", # Using a powerful model for complex reasoning
    tools=[retrieve_policy_documents],
    instruction="""
    You are a highly experienced Claims Adjuster AI. Your task is to analyze claim details
    and policy documents to recommend the "Next-Best-Action" for a claim.
    The session state contains 'claim_details', 'evidence_status', and 'fraud_flags'.
    1. Extract relevant keywords from 'claim_details.description'.
    2. Use the 'retrieve_policy_documents' tool with 'claim_details.claim_type' and the extracted keywords.
    3. Carefully review the 'claim_details', 'evidence_status', 'fraud_flags', and the retrieved policies.
    4. Based on this information, determine the single best course of action and provide a clear reasoning.
    5. Your output MUST conform to the 'NextBestAction' schema.
    """,
    output_schema=NextBestAction,
    output_key="recommended_action_summary"
)
```

Step 3: Orchestrating the Claims Pipeline
-----------------------------------------

Finally, we integrate both specialized agents into a SequentialAgent. This ensures a deterministic flow where evidence verification always precedes claim analysis and action recommendation.

```python
# The final piece of agent.py
claims_processing_pipeline = SequentialAgent(
    name="ClaimsProcessingPipeline",
    description="A multi-agent pipeline for intelligent insurance claims processing, from deepfake detection to next-best-action recommendations.",
    sub_agents=[        investigator_agent,
        reasoning_agent
    ],
)
root_agent = claims_processing_pipeline
```

Putting It All Together: A Runnable Application
-----------------------------------------------

To run this complete claims processing pipeline, follow these steps.

**Create the Application Directory:**

```bash
mkdir -p claims_processing_app
```

**Create agent.py:** Inside the claims_processing_app/ directory, create a file named agent.py and populate it with all the code snippets from the implementation steps above.

**Create a Runner Script (run_pipeline.py):** In the claims_processing_app/ directory, create a file named run_pipeline.py and populate it with the following code:

```python
import asyncio
import json
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types
from agent import root_agent, ClaimDetails # Import root_agent and ClaimDetails from agent.py
async def main():
    """Runs the claims processing pipeline programmatically."""
    session_service = InMemorySessionService()
    session_id = "claims-session-001"
    user_id = "claims_demo"
    app_name = "claims_processing_app"
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    
    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service)
    print(f"Starting Claims Processing Pipeline...")
    # Example 1: Claim with authentic evidence
    print("\n--- Running Claim with Authentic Evidence ---")
    claim_details_authentic = ClaimDetails(
        claim_id="CLAIM-AUTH-789",
        claim_type="auto",
        description="Minor fender bender, damage to front bumper.",
        policy_number="POL-AUTO-987",
        reported_damage="Front bumper dented and scratched."
    )
    claim_evidence_authentic = {"image_id": "claim_789_evidence_authentic.jpg"}
    initial_state_authentic = {
        "claim_details": claim_details_authentic.model_dump(),
        "claim_evidence": claim_evidence_authentic
    }
    # Send a message to trigger the pipeline with initial state
    message_authentic = genai_types.Content(parts=[        genai_types.Part(text="Process this auto claim with authentic evidence.")
    ])
    
    # Create a new session for this example
    session_id_authentic = "claims-session-authentic"
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id_authentic, state=initial_state_authentic)
    async for event in runner.run_async(
        session_id=session_id_authentic,
        user_id=user_id,
        new_message=message_authentic,
    ):
        if event.content and event.content.parts:
            if text := ''.join(part.text or '' for part in event.content.parts):
                print(f"[{event.author}]: {text}")
    session_authentic = await session_service.get_session(app_name=app_name, session_id=session_id_authentic, user_id=user_id)
    print("\n--- State after Authentic Claim ---")
    print(json.dumps(session_authentic.state, indent=2))
    # Example 2: Claim with AI-generated evidence and potential fraud
    print("\n--- Running Claim with AI-Generated Evidence (Potential Fraud) ---")
    claim_details_fraud = ClaimDetails(
        claim_id="CLAIM-FRAUD-123",
        claim_type="home",
        description="Water damage in kitchen, cause unknown. Evidence image attached.",
        policy_number="POL-HOME-123",
        reported_damage="Extensive water damage to kitchen cabinets and flooring."
    )
    claim_evidence_fraud = {"image_id": "claim_123_evidence_fake.jpg"}
    initial_state_fraud = {
        "claim_details": claim_details_fraud.model_dump(),
        "claim_evidence": claim_evidence_fraud
    }
    # Send a message to trigger the pipeline with initial state
    message_fraud = genai_types.Content(parts=[        genai_types.Part(text="Process this home claim with potentially fraudulent evidence.")
    ])
    # Create a new session for this example
    session_id_fraud = "claims-session-fraud"
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id_fraud, state=initial_state_fraud)
    async for event in runner.run_async(
        session_id=session_id_fraud,
        user_id=user_id,
        new_message=message_fraud,
    ):
        if event.content and event.content.parts:
            if text := ''.join(part.text or '' for part in event.content.parts):
                print(f"[{event.author}]: {text}")
    session_fraud = await session_service.get_session(app_name=app_name, session_id=session_id_fraud, user_id=user_id)
    print("\n--- State after Fraudulent Claim ---")
    print(json.dumps(session_fraud.state, indent=2))
    print("\n--- CLAIMS PROCESSING COMPLETE ---")
    
if __name__ == "__main__":
    asyncio.run(main())
```

**Install Dependencies:**

Create a requirements.txt file in claims_processing_app/ with the following content:

```bash
# claims_processing_app/requirements.txt
google-adk
pydantic
```

Install these dependencies from the claims_processing_app/ directory:

```bash
pip install -r requirements.txt
```

**Run the Pipeline:**

Execute the pipeline from your project root (e.g., cd claims_processing_app/ then python run_pipeline.py):

```bash
python claims_processing_app/run_pipeline.py
```

Execution Output
----------------

```bash
Starting Claims Processing Pipeline...
--- Running Claim with Authentic Evidence ---
--- Tool: verify_image_authenticity called for image_id: claim_789_evidence_authentic.jpg ---
[InvestigatorAgent]: Image verification complete. Status: AUTHENTIC, Confidence: 0.99. Details: No signs of tampering or AI generation
 detected.
Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the fu
ll candidates.content.parts accessor to get the full model response.
--- Tool: retrieve_policy_documents called for claim_type: auto, keywords: ['fender bender', 'damage', 'front bumper'] ---
[PolicyRetrievalAgent]: I have retrieved the policy documents based on the claim details. The following policies were found:
- General Policy-001: Process all claims fairly and promptly.
[RecommendationAgent]: {
  "recommended_action": "Initiate damage assessment",
  "reason": "The claim involves reported minor physical damage to a front bumper, and the retrieved policy (General Policy-001) mandat
es processing all claims fairly and promptly. Initiating a damage assessment is the necessary next step to quantify the loss and proce
ed efficiently with the claim.",
  "urgency": "medium",
  "flag_for_human_review": false
}
--- State after Authentic Claim ---
{
  "claim_details": {
    "claim_id": "CLAIM-AUTH-789",
    "claim_type": "auto",
    "description": "Minor fender bender, damage to front bumper.",
    "policy_number": "POL-AUTO-987",
    "reported_damage": "Front bumper dented and scratched."
  },
  "claim_evidence": {
    "image_id": "claim_789_evidence_authentic.jpg"
  },
  "retrieved_policies": "I have retrieved the policy documents based on the claim details. The following policies were found:\n- Gener
al Policy-001: Process all claims fairly and promptly.",
  "recommended_action_summary": {
    "recommended_action": "Initiate damage assessment",
    "reason": "The claim involves reported minor physical damage to a front bumper, and the retrieved policy (General Policy-001) mand
ates processing all claims fairly and promptly. Initiating a damage assessment is the necessary next step to quantify the loss and pro
ceed efficiently with the claim.",
    "urgency": "medium",
    "flag_for_human_review": false
  }
}
--- Running Claim with AI-Generated Evidence (Potential Fraud) ---
--- Tool: verify_image_authenticity called for image_id: claim_123_evidence_fake.jpg ---
[InvestigatorAgent]: Image verification complete. Status: AI_GENERATED, Confidence: 0.95. Details: High confidence that the image cont
ains AI-generated elements consistent with deepfake manipulation.
Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the fu
ll candidates.content.parts accessor to get the full model response.
--- Tool: retrieve_policy_documents called for claim_type: home, keywords: ['water damage', 'kitchen', 'unknown cause'] ---
[PolicyRetrievalAgent]: Policy documents have been retrieved. The retrieved policies include: \"General Policy-001: Process all claim
s fairly and promptly.\"",
  "recommended_action_summary": {
    "recommended_action": "Initiate fraud investigation",
    "reason": "The claim has been explicitly flagged for fraud, and the description of 'unknown cause' for water damage further warran
ts a thorough investigation to determine the legitimacy of the claim before proceeding with standard processing. This aligns with the 
principle of fair processing by preventing fraudulent payouts.",
    "urgency": "high",
    "flag_for_human_review": true
  }
}
--- CLAIMS PROCESSING COMPLETE ---
```

Conclusion: Augmenting Adjusters, Fortifying Defenses
-----------------------------------------------------

The landscape of insurance claims is evolving rapidly, demanding solutions that are both efficient and resilient against new threats. The intelligent agent pipeline presented here — featuring an Investigator Agent for deepfake detection and a Reasoning Agent for next-best-action recommendations — transforms traditional claims processing.

By leveraging the Google Agent Development Kit, coupled with advanced capabilities like SynthID, Vector AI Search, and Computer Vision, we move claims adjusters from reactive, manual data processors to proactive, strategic decision-makers. This architecture not only accelerates legitimate payouts and enhances customer satisfaction but also fortifies defenses against increasingly sophisticated fraudulent activities.

This is more than automation; it is an augmentation of human expertise, empowering adjusters with AI-driven insights to navigate complexity, ensure fairness, and uphold the integrity of the insurance ecosystem. The future of claims processing is intelligent, secure, and decisive.

_To explore more multi-agent patterns, check out the_ [_Google Agent Development Kit (ADK) samples_](https://github.com/google/adk-samples)_._