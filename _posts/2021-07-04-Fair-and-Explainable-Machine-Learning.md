---
layout: post
permalink: blog/blog59/
categories: [Artificial Intelligence]
---

![](https://miro.medium.com/max/12000/0*Pka37tvq8-RcQGMb)
Photo by [Nicolas Jossi](https://unsplash.com/@nicopic?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

# Fair and Explainable Machine Learning

## A guide on how to prevent bias in Machine Learning models and understand their decisions.

> “Although neural networks might be said to write their own programs, they do so towards goals set by humans, using data collected for human purposes. If the data is skewed, even by accident, the computers will amplify injustice.”
>
> — The Guardian \[1\]

### Introduction

Application of Machine Learning in ambits such as medicine, finance and education is still nowadays quite complicated due to the ethical concerns surrounding the use of algorithms as automatic decision-making tools.

Two of the main causes at the root of this mistrust are: bias and low explainability. In this article, we are going to explore both of these concepts and introduce different techniques which can be applied in order to make our models more fair and explainable.

### Bias

In Machine Learning the term bias is commonly associated as the difference between the correct values we are trying to predict and the predictions made by our model. However, in cognitive science, the term bias can have many other connotations. Some examples of cognitive biases are \[2\]:

-   **Reporting bias:** how frequently an outcome/property is recorded in our data is not truly representative of how frequently it appears in the real world compared to the other outcomes/properties considered in our data.
-   **Selection bias:** selecting a sample from a population which is not truly representative of the key population characteristics (not a random sample).
-   **Overgeneralization:** oversimplifying a process can potentially lead to wrong conclusions.
-   **Correlation fallacy:** misinterpreting a spurious correlation as a cause-effect driven process.
-   **Confirmation bias:** focusing just on finding sources which confirm an our prior belief rather than fairly assessing different views/options about a topic.

If bias is embedded in our data and/or Machine Learning model, this could then give rise to **algorithmic bias** (biased automatic decision-making tools). One of the most intuitive approaches, in order to try to understand if a Machine Learning model is biased or not, is to disaggregate the evaluation for our model.

For example, let us imagine we trained a model in order to classify if someone is affected or not by disease and we achieved about 80% classification accuracy. At this point, in order to make sure our model is truly fair we give a closer look at how the accuracy would change if we consider first just woman and then just men. Considering just woman we get about 95% accuracy, while considering just men we get about 55% accuracy! In order to try to understand why there is such a big difference in performance, we could then try to examine our training data. After a careful analysis, we then notice that about 75% of our training data contained samples just about female patients, and therefore our model gave overall more weight to these samples in order to ultimately reduce as much as possible our misclassification score. Performing this type of analysis helped us, therefore, to understand that although our model was able to perform overall well, it shouldn’t potentially be used in a medical setting in order to perform diagnosis for male patients. It would have been in fact “unfair” to use this model for both male and female diagnosis considering the disparity in the accuracy for each sub-group. In order to take this analysis even further, the resulting confusion matrices and precision/recall metrics should be considered to assess false positive/negative rates influences.

Another factor which should be taken into account when trying to understand if a data-driven system might be biased or not is to make some background researches about how the training data was generated in the first place (e.g. were the participant voluntarily involved, were they from different countries, had they varied backgrounds, was the research study sponsored by any organization, etc…).

Bias mitigation algorithms can therefore be applied at three possible stages during a Data Science workflow: **pre-processing** (on the training data), **in-processing** (while training a model), **post-processing** (on the predicted labels). Some of the most common bias mitigation algorithms for each of these stages are \[3\]:

-   **Pre-Processing:** Reweighting, Disparate Impact Remover, Learning Fair Representations.
-   **In-Processing:** Adversarial Debiasing, Prejudice Remover, Meta Fair Classifier.
-   **Post-Processing:** Reject Option Classification and Calibrated Equalized Odds.

All these different approaches can then be implemented in Python making use of the [AI Fairness 360 library](https://github.com/Trusted-AI/AIF360).

### Explainable AI

One of the key trade-offs in modern Machine Learning models is performance against complexity. More complex models, such as Deep Learning based architecture, tend in fact to usually outperform more traditional models such as regression techniques and linear classifiers.

Complex models are commonly referred to as **Black Boxes** (e.g. ensemble models, neural networks) and they are traditionally difficult to interpret when trying to understand why they would make a choice over another. In contrast, models such as Decision Trees and Linear Regression are instead considered as **White-Boxes** (they make much easier to understand how a prediction was created).

Explainable AI is a new branch in Artificial Intelligence which aims to try to “demystify” Machine Learning models predictions by providing to the end-user, not just predictions but also supporting evidence.

Creating explainable models could then benefit:

-   **Users/Clients:** Why was my loan denied? Why I got suggested this medical treatment?
-   **Regulators/Governments:** provide evidence that a model is fair.
-   **Data Scientists/Developers:** how well is our model truly performing? how could it be improved?

Different approaches towards Explainable AI are currently used nowadays, some of the main examples are:

-   **SHAP (Shapley additive explanations):** aims to explain a model prediction by measuring how much each feature contributed to making the prediction (the larger the absolute value of the Shapley Value and the more important a feature is considered to be).
-   **LIME (Local Interpretable Model-Agnostic Explanations):** is mainly used when working with highly non-linear models. LIME aims to linearize non-linear spaces by dividing the original feature space into different linear subsections so that to make the model explainable by a linear model on a local basis.
-   **Tree-based Feature Importance:** calculate the average reduction in impurity for a tree (or a forest of trees) caused by each input feature. According to this principle, features which split nodes closer to the top of the three would then have more weight when creating a model prediction.
-   **Partial Dependence Plots (PDP):** summarise the relationship between a set of input variables and our model predictions. In this way, it can be possible to visually understand how a model prediction depends on the different input variables.
-   **Individual conditional expectation (ICE) plots:** helps us in trying to understand individual observations predictions by simulating what would happen if the input data would have been slightly modified.

Some of the most commonly used Python libraries in order to perform Explainable AI tasks are: [AI Explainability 360 (AIX360)](https://github.com/Trusted-AI/AIX360) and [Captum](https://captum.ai/).

### Bibliography

\[1\] The Guardian view on machine learning: people must decide. Editorial. Accessed at: [https://www.theguardian.com/commentisfree/2016/oct/23/the-guardian-view-on-machine-learning-people-must-decide](https://www.theguardian.com/commentisfree/2016/oct/23/the-guardian-view-on-machine-learning-people-must-decide)

\[2\] Stanford CS224N: NLP with Deep Learning, Winter 2019, Lecture 19 — Bias in AI. [stanfordonline](https://www.youtube.com/channel/UCBa5G_ESCn8Yd4vw5U-gIcg). Accessed at: [https://www.youtube.com/watch?v=XR8YSRcuVLE&ab\_channel=stanfordonline](https://www.youtube.com/watch?v=XR8YSRcuVLE&ab_channel=stanfordonline)

\[3\] Fair and Explainable AI. Margriet Groenendijk. Accessed at: [https://margriet-groenendijk.gitbook.io/trusted-ai-workshop/](https://margriet-groenendijk.gitbook.io/trusted-ai-workshop/)
