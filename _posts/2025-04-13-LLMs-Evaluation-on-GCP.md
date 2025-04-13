---
title: LLMs Evaluation on GCP
layout: post
permalink: blog/blog90/
categories: [Generative AI]
---

![AI Generated (Image by Author).](https://cdn-images-1.medium.com/max/2048/1*Y4lleX5fvkEjk0eVzqXTIw.jpeg)<br>AI Generated (Image by Author).

<!--end_excerpt-->

## LLMs Evaluation on GCP

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
            This is a guest post originally published on <a href="https://medium.com/p/9186fad73f22" target="_blank">Google Cloud - Community</a>.
        </ul>
        </td>
    </tr>
    </tbody>
</table>

### An introduction to some of the most common evaluation approaches for LLM applications and how GCP can support you across the journey.

## Introduction

Widespread availability and fast-tracked progresses in LLM performance have made it really easy for practitioners to develop fully fledged AI backed applications in a matter of days. Regardless, even if the road to production may be paved with good intentions, it’s too often littered with the wrecks of projects that skipped rigorous pre-production evaluation. Thorough testing and validation are the essential guardrails that keep a system on track and prevent costly, late-stage failures.

The foundational model of choice is merely the source of an LLM’s backed application potential (Figure 1). True evaluation is charting the full course of the river: the data that forms its currents, the infrastructure that shapes its banks, and the applications that are its ultimate destination. Only by understanding this entire flow can we predict whether the LLM will reach its potential or run dry before it meets the sea.

![Figure 1: LLM Evaluation Overview (Image by Author).](https://cdn-images-1.medium.com/max/2000/0*OD5fGaXoj76cC_XY)<br>Figure 1: LLM Evaluation Overview (Image by Author).

Defining a standardized way to evaluate an LLM can not only make it possible to quantify the model accuracy but also:

* Tracking progress over different development iterations.

* Streamline comparison between different models.

* Optimizing for fair use (e.g. creating transparent and reproducible processes for bias mitigation).

* Meeting regulatory and Service Level Agreements (SLAs) requirements.

## Metrics

Metrics to evaluate LLMs can be further divided into 2 categories: quantitative and qualitative.

Quantitative metrics can be easily calculated using numeric formulas, some examples include (Figure 2):

* [**Perplexity**](https://en.wikipedia.org/wiki/Perplexity): how well the model can predict the next word in a sentence (the lower, the better).

* [**ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**](https://en.wikipedia.org/wiki/ROUGE_(metric)): is used for text summarization tasks and checks the overlap between human summaries and LLM generated summaries. ROUGE focuses mainly on recall.

* [**BLEU (Bilingual Evaluation Understudy)**](https://en.wikipedia.org/wiki/BLEU): is used for translation tasks and assesses the LLM output against a reference translation. BLEU focuses instead primarily on precision.

* [**Accuracy**](https://en.wikipedia.org/wiki/Accuracy_and_precision): for traditional classification tasks (e.g. spam/not spam).

![Figure 2: LLMs Tasks vs Metrics (Image by Author).](https://cdn-images-1.medium.com/max/2000/0*3y6aBH3Pcn-5E-iF)<br>Figure 2: LLMs Tasks vs Metrics (Image by Author).

Qualitative metrics focus more on capturing overall language/content quality and usually involve humans or [LLMs as a Judge](https://hamel.dev/blog/posts/llm-judge/) in order to be estimated, some examples include:

* **Factuality**: does the LLM hallucinate? (provides false/misleading information) Is the information provided grounded?

* **Relevance**: how relevant is the LLM response compared to the prompt request?

* **Fluency**: does the response flow sound natural and realistic?

* **Coherence**: are the different phrases/sentences logically consistent?

![Figure 3: Metrics Choice Decision Tree (Image by Author).](https://cdn-images-1.medium.com/max/3200/0*Bp03SN3CxtUsyzkf)<br>Figure 3: Metrics Choice Decision Tree (Image by Author).

Similar approaches can then be applied when evaluating not only LLM text outputs but also other forms of content such as images. Particularly, for Image synthesis metrics such as [**Inception score**](https://en.wikipedia.org/wiki/Inception_score) and [**Frechet inception distance**](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inception_distance) can be used, and to assess image quality **Structural similarity index** and **peak signal-to-noise ratio**.

Finally, another aspect to keep track of is mitigation of any form of [bias](https://en.wikipedia.org/wiki/List_of_cognitive_biases) and ensuring [fairness](https://cloud.google.com/vertex-ai/docs/evaluation/intro-evaluation-fairness). Some key metrics can help us ensuring this include:

* **Demographic parity**: Are loan approvals granted at similar rates for all races? (the model predictions should not be skewed towards any particular group).

* **Equal opportunity**: Are equally qualified candidates from all demographics being wrongly rejected at the same rate? (the model should not disproportionately disadvantage certain groups by making more mistakes for them).

* **Counterfactual Fairness**: Would a person’s job application be evaluated differently if their gender was changed in the application? (to idea is to identify and eliminate biases directly linked to sensitive attributes).

When evaluating a model it can also be helpful to look for possible intrinsic training biases. For example, usually models tend to prefer verbose answers over short ones or prefer one option over another based on its positional order.

## LLM Evaluation Approaches/Steps

There are currently 4 key LLM Evaluation Approaches/Steps:

* **Benchmark/Golden Dataset**: collecting/creating samples of examples reference answers we can evaluate an LLM against. In this case, it is vital to tailor the golden dataset to match future users expectations and needs. Depending on size and structure, these could then be stored in GCP services such as Cloud Storage, BigQuery, Spanner, etc.

* **Business Metrics**: estimating the overall impact of our LLM system on business performance, return on investment, revenue, etc.

* **LLM as a Judge**: using another LLM to evaluate our LLM system for a set of tasks against some predetermined criterias. Some frequent issues with the “LLM as a Judge” approach are: self-bias, inconsistent scoring, and poor correlation with human evaluations.

* **User Provided Feedback**: using human feedback to direct the model towards more useful responses.

These evaluation approaches can then come to action at different stages in the pre/post deployment process (Figure 4).

![Figure 4: LLM Evaluation Stages (Image by Author).](https://cdn-images-1.medium.com/max/4076/1*AfwxY9arDr5Hzdf4yzu2iQ.png)<br>Figure 4: LLM Evaluation Stages (Image by Author).

## Benchmark/Golden Dataset

### Getting Benchmark Datasets

When working with company specific use cases it would then be advisable to create your own internal golden/benchmark dataset to evaluate your model based on company specific internal jargon (e.g. financial, medical terms), etc. This approach can in fact provide much more relevant evaluations tailored to your use case compared to using out of the box industry benchmarks. In case no data is available, generating synthetic data could be used as a last resort.

Additionally, there are a large number of existing Evaluation Benchmark datasets commonly used in the industry in order to evaluate LLMs, some include:

* **GLUE (General Language Understanding Evaluation):** Assesses overall language understanding through nine diverse tasks, including sentiment analysis, question answering, and textual entailment. Provides a single aggregate score for simplified model comparison.

* **SuperGLUE:** A more challenging successor to GLUE, designed after models surpassed human performance on the original benchmark. Features complex tasks requiring advanced language understanding and reasoning.

* **HellaSwag:** Evaluates commonsense reasoning by requiring models to predict the most logical continuation of a given scenario from multiple choices.

* **TruthfulQA:** Focuses on the model’s ability to provide truthful and non-misleading answers, crucial for building reliable AI systems.

* **MMLU (Massive Multitask Language Understanding):** A comprehensive benchmark with over 15,000 questions across 57 subjects, spanning STEM, humanities, and more. Measures a model’s breadth of knowledge and its ability to perform complex reasoning across diverse domains.

* **ARC (AI2 Reasoning Challenge):** Concentrates on scientific reasoning abilities.

* **LAMBADA:** Tests a model’s proficiency in predicting the final word of a text passage, assessing long-range dependencies.

* **SQuAD (Stanford Question Answering Dataset):** Evaluates reading comprehension and the ability to extract answers from a given text.

### Labeled vs Unlabeled Datasets

To aid with the labeling process, different enterprise solutions have been created such as [Labelbox](https://console.cloud.google.com/marketplace/product/labelbox-tackle-public/labelbox-product-gcp), to provide an easy to use interface where to label data and outsource human evaluators (if internal workforce is not possible and data not too sensitive).

Evaluation can also be possible without labeled data (using for example NannyML open source approach with the [Confidence-Based Performance Estimation algorithm](https://ppiconsulting.dev/blog/blog71/) or LLM Autoraters) but often less precise and error prone.

## User Provided Feedback

Human evaluators, front-facing users and LLM Judges can support the evaluation process in 2 main possible ways: direct or comparative assessment.

With direct assessment, a user might be asked to rate an answer or complete some sort of survey following a conversation with an LLM (using pointwise metrics). In comparative assessments, users can instead be provided with different variations of the same answer and asked to pick which one they prefer (through pairwise comparison). This approach can be particularly useful when trying to fine tune a model or perform some form of A/B testing to decide which model is best to use.

## Task specific approaches

So far, we have considered how to evaluate general LLM predictions, although LLMs are usually part of wider systems to solve actual applications. Some common examples include, AI Powered Search, RAG (​​Retrieval Augmented Generation) and Agents. In these cases, additional applications related metrics are needed.

 1. **AI Search:** Evaluation of search quality using Vertex AI Search can be performed by providing examples of typical user queries paired with best matching results, more information about the process can be found [here](https://cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality#unstructured-data). To further improve performance, Vertex AI Agent Builder Search is also able to provide an out of the box solution for [fine-tuning your search model](https://cloud.google.com/generative-ai-app-builder/docs/tune-search).

 2. **RAG:** Design of a RAG system needs to usually go through [multiple optimization iterations](https://cloud.google.com/blog/products/ai-machine-learning/optimizing-rag-retrieval?e=48754805) and open source libraries such as [Ragas](https://github.com/explodinggradients/ragas) can be of great help to streamline the process. With the latest launch of [Vertex AI RAG Engine](https://cloud.google.com/blog/products/ai-machine-learning/introducing-vertex-ai-rag-engine) on GCP, it can then be easier than ever to [optimize RAG hyperparameters](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/rag-engine/rag_engine_evaluation.ipynb) such as Chunk Size/Overlap, Vector Distance threshold, etc.. to improve search quality. Some examples of metrics used to measure RAG contextual relevance include: NDCG (Normalized Discounted Cumulative Gain), MRR (Mean Reciprocal Rank), MAP (Mean Average Precision), Precision@K. Once optimized the retrieval metrics, it can then be possible to understand its impact on response quality using the [Evaluation Service API](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/evaluate_rag_gen_ai_evaluation_service_sdk.ipynb).

 3. **Agents:** As agentic solutions are becoming more and more common in the industry, more complex forms of agent evaluations have been emerging. Overall, the success of an agentic workflow can be measured by its final response (if the agent achieved or not its objectives) or trajectory (sequence of tools the agent invoked to achieve its goals). When evaluating trajectory, metrics such as: exact match, in order match, any-order match, precision, recall, etc. are typically used. Additional information about these types of metrics and data setup for evaluation is available in the [Vertex AI Gen AI evaluation service documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-agents).

Finally, when metrics optimization might not be enough, LLM fine-tuning might be the best approach to take in order to tailor off the shelf LLMs for your use case specifics (either through Full fine-tuning or Parameter efficient tuning). Vertex AI provides [Supervised fine-tuning](https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models) support out of the box for different data types such as text, image, audio, and document. Moreover, LLM fine-tuning and evaluation can also be performed directly in [BigQuery](https://cloud.google.com/blog/products/data-analytics/bigquery-can-now-fine-tune-models-hosted-in-vertex-ai/?e=48754805) depending on use case needs.

## Evaluation Frameworks

Here at Google Cloud, we developed the [Gen AI evaluation service](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview). This library is designed to work seamlessly with Vertex AI and support not only the Gemini family but also open 3rd party models. Using the GenAI evaluation service you are able to get out of the box support for a whole collection of metrics maintained by the Google ecosystem while still having the flexibility to bring and define your own custom metrics. This service is additionally designed to help perform specialized tasks such as prompt engineering, RAG and AI Agents optimization.

On top of this, Vertex AI also supports pairwise model-based evaluation through [AutoSxS](https://cloud.google.com/vertex-ai/generative-ai/docs/models/side-by-side-eval) (with an LLM autorater).

Finally, if you looking to kickstart your GenAI project on GCP, another great resource to look into is the “[Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)”, an open source repository providing templates for common GenAI tasks on GCP, including how to evaluate Generative AI applications using tools like [Gen AI evaluation service](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview) and [Vertex AI Experiments](https://cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments).

### Open Source Alternatives

With the widespread adoption of LLMs, a wealth of libraries have been developed over the last few years in order to bridge the evaluation gap. Some notable examples include:

* [DeepEval](https://github.com/confident-ai/deepeval)

* [TruLens](https://github.com/truera/trulens)

* [Opik](https://github.com/comet-ml/opik)

* [Guardrails AI](https://github.com/guardrails-ai/guardrails) (additional information about guardrails for LLMs and other caveats can be found [here](https://towardsdatascience.com/llms-pitfalls-7a33de009638))

Additionally, other libraries focused also on traditional Machine Learning evaluation tasks have been expanded to include also LLM capabilities:

* [MLFlow](https://mlflow.org/)

* [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/en/index)

* [Deepchecks](https://github.com/deepchecks/deepchecks)

Given the open source nature of these frameworks, they can all be used as part of your development process on GCP with any of the models available on Model Garden.

## Best Practices

To summarize, some common best practices to follow in an evaluation system include (Figure 5):

* Match metrics to real world needs and make them as straightforward and consistent as possible.

* Routinely monitor and create alert systems on key metrics to prevent model performance to degrade for too long unnoticed.

* Regularly benchmark performance against other models and perform unit testing on outputs.

* Whenever using humans in evaluation, make sure to only work with domain experts that can help steer the model in the right direction.

* Perform adversarial attack tests to try to break your own model and discover edge case failures (e.g. Perturbation Testing).

* Ensure LLMs predictions are as repeatable as possible (e.g. use low temperature and fixed seeds).

![Figure 5: Evaluation Pipeline Example (Image by Author).](https://cdn-images-1.medium.com/max/3200/0*Y0thojPSAvJf8HK7)<br>Figure 5: Evaluation Pipeline Example (Image by Author).

For an in-depth guide on evaluation, feel free to refer to the [Hugging Face Evaluation Handbook](https://github.com/huggingface/evaluation-guidebook/tree/main).