---
layout: post
permalink: blog/blog61/
categories: [Machine Learning]
---

![](https://miro.medium.com/max/12000/0*h35-TIdajmujrlsY)
Photo by [Dan Meyers](https://unsplash.com/@dmey503?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

# Causal Reasoning in Machine Learning

## An investigation through some of the main limitations Artificial Intelligence-powered systems are facing

### Introduction

Thanks to recent advancements in Artificial Intelligence (AI), we are now able to leverage Machine Learning and Deep Learning technologies in both academic and commercial applications. Although, relying just on correlations between the different features, can possibly lead to wrong conclusions since correlation does not necessarily imply causation. Two of the main limitations of nowadays Machine Learning and Deep Learning models are:

-   **Robustness:** trained models might not be able to generalise to new data and therefore would not be able to provide robust and reliable performances in the real world.
-   **Explainability:** complex Deep Learning models can be difficult to analyse in order to clearly demonstrate their decision-making process.

Developing models able to identify cause-effect relationships between different variables might ultimately offer a solution to solve both of these problems. This idea has also been supported by researchers such as Judea Pearl, which advocated how having models able to reason in uncertainties could not be enough to enable researchers to create machines able to truly express intelligent behaviour \[1\].

### Causality

#### Concepts of Causality

Nowadays Machine Learning models, are able to learn from data by identifying patterns in large datasets. Although, humans might be able to perform a same task after just examining a few examples. This is possible thanks to the inherit human ability to understand causal relationships and use inductive inference \[2\] in order to assimilate new information about the world \[3\]. Creating models able to demonstrate causal reasoning would, therefore, open to us a whole new world of opportunities in AI research.

Causality arises naturally in our daily life every-time we ask ourselves any type of interventional or retrospective question (eg. What if I take this action? What if I would have acted differently?).

As shown in Figure 1, Causal Reasoning can be divided into three different hierarchical levels (Association, Intervention, Counterfactuals). At each level, different types of questions can be answered and in order to answer questions at the top levels (eg. Counterfactuals) are necessary as basic knowledge from the lower levels \[4\]. In fact, in order to be able to able to answer retrospective questions, we would expect to first be able to respond to intervention and association type of questions.

![](https://miro.medium.com/max/1400/1*BTBExrtaTvtDJXZPEkTS4A.png)
<br>
Figure 1: Causality Hierarchy (Image by Author)

Currently, Machine Learning models are only able to answer the probabilistic type of questions related to the Association level.

Thanks to the rising interest in this topic, a mathematical framework able to represent causal relationships has been constructed (Structural Causal Models (SCM) \[4\]). Using this type of framework, causal expressions can then be formulated and used in conjunction with data in order to make predictions.

#### Linear and Non-Linear Causality

Causality can be divided into two main types: linear and non-linear (Figure 2) \[5\]:

-   In linear causality, connections between the variables can be in a single direction and every effect can be originated by a limited number of causes. Causes always linearly precede effects (time precedence).
-   In non-linear causality, connections between variables can be bi-directional and effects can possibly be originated by an unlimited number of causes.

Linear causation systems are characterised by proportional relationships between cause and effects variables (eg. Deterministic Systems). Instead, in non-linear causation systems, disproportionate effects can take place (eg. Non-deterministic Systems). For example, small changes in input conditions would then result in different consequences (eg. “Butterfly Effect”).

![](https://miro.medium.com/max/1400/1*ZpWzEmyFANNuzVp3y8QzFg.png)
<br>
Figure 2: Linear vs Non-Linear Causality (Image by Author)

#### Case Study: Recommendation Systems

One of the main weakness of most Machine Learning models is the assumption that the data fed in is independent and identically distributed (IID). When this assumption holds, convergence to the lowest possible loss is achievable but when this constrain is violated the model might perform poorly even when attempting simple tasks (eg. poisoning attacks) \[6\].

As an example, let us consider an e-commerce recommendation system. Nowadays systems, are able to offer recommendations mainly based on products correlated to the ones we are planning to buy, although this cannot always lead to accurate estimates. For instance, we might have recently bought a new phone and we are now looking for a phone case. While browsing for phone cases, although our recommendation system might try to suggest us other items such as phones (just because they are correlated) instead of more cause-effect related items like screen protectors.

### Techniques

One of the main technique used in order to try to discover causal relationships are Graphical Methods such as Knowledge Graphs and Bayesian Belief Networks. These two methods form in fact the basis of the Association level in the Causality Hierarchy, enabling us to answer questions such as: What different properties compose an entity and how are the different components related each other?

Graphical Methods have been of great importance in the last few years in order to start applying causality to Machine Learning. Although, in order for us to move from the Association to the Intervention level in the Causality Hierarchy, alternative approaches might be necessary. Some additional techniques which are commonly used in Explainable AI and Causality in order to answer Intervention types of questions (eg. What if?) are:

-   [Feature Selection techniques](https://towardsdatascience.com/feature-selection-techniques-1bfab5fe0784) (eg. Recursive Feature Elimination, Shapley Values).
-   Global and Local Model Surrogate (eg. Local Interpretable Model-Agnostic Explanations).
-   [Bias in AI](https://towardsdatascience.com/fair-and-explainable-machine-learning-25b802b00bec) (eg. Pre-processing, In-processing, Postprocessing algorithms).
-   [Modelling Hidden Variables](https://towardsdatascience.com/stochastic-processes-analysis-f0a116999e4) (eg. Hidden Markov Models, Boltzmann Restricted Machine).

Finally, apart from Machine Learning, Causal Inference can also be applied to other fields of Artificial Intelligence such as Reinforcement Learning. In fact, in order for agents to achieve good performances in an environment, they need to be able to think about what consequences would their action lead to \[7\], therefore requiring causal abilities belonging to the Counterfactual hierarchical level. Additionally, causality can be used in this ambit also to create causal partial models to predict high dimensional future observations in lower-dimensional spaces \[8\].

#### Comparison

From a statistical and a research point of view, Graphical Methods and modelling techniques to identify hidden variables and biases are now representing an area of growing interest since they are related to areas which have not been explored yet as much as Machine Learning in the past decade (although being still possibly able to be integrated with these techniques).

On the other hand, Feature Selection and Global/Local Model Surrogate techniques are methods commonly used nowadays in Deep Learning problems in order to make complex models easier to analyse to understand their decision-making process (eg. finding out which features had greater weight when making a prediction and using surrogate models to create linear models at a local scale for non-linear problems).

### Bibliography

\[1\] To Build Truly Intelligent Machines, Teach Them Cause and Effect Quanta Magazine. Accessed at: [https://www.quantamagazine.org/to-buildtruly-intelligent-machines-teach-them-cause-and-effect-20180515](https://www.quantamagazine.org/to-buildtruly-intelligent-machines-teach-them-cause-and-effect-20180515), March 2020.

\[2\] Inductive Inference Jan-Willem Romeijn, in Philosophy of Statistics, 2011. ScienceDirect. Accessed at: [https://www.sciencedirect.com/topics/mathematics/inductive-inference](https://www.sciencedirect.com/topics/mathematics/inductive-inference), March 2020.

\[3\] Human-level concept learning through probabilistic program induction Brenden M. Lake, Ruslan Salakhutdinov, Joshua B. Tenenbaum. Accessed at: [https://web.mit.edu/cocosci/Papers/Science-2015-Lake-13328.pdf](https://web.mit.edu/cocosci/Papers/Science-2015-Lake-13328.pdf), March 2020.

\[4\] The Seven Tools of Causal Inference with Reflections on Machine Learning JUDEA PEARL, UCLA Computer Science Department, USA. Accessed at: [https://ftp.cs.ucla.edu/pub/statser/r481.pdf](https://ftp.cs.ucla.edu/pub/statser/r481.pdf), March 2020.

\[5\] Systems Thinking Systems Modelling A Course for Understanding Systems and Creating Systems Models. The Sustainability Laboratory. Accessed at: [https://systemsinnovation.io/system-dynamics-book/](https://systemsinnovation.io/system-dynamics-book/), March 2020.

\[6\] CAUSALITY FOR MACHINE LEARNING Bernhard Schölkopf, Max Planck Institute for Intelligent Systems. Accessed at: [https://arxiv.org/pdf/1911.10500.pdf](https://arxiv.org/pdf/1911.10500.pdf), March 2020.

\[7\] Causal Reasoning from Meta-reinforcement Learning Ishita Dasgupta et. al. Deep Mind. Accessed at: [https://arxiv.org/pdf/1901.08162v1.pdf](https://arxiv.org/pdf/1901.08162v1.pdf), March 2020.

\[8\] Causally Correct Partial Models for Reinforcement Learning Danilo J. Rezende, Ivo Danihelka et. al. Accessed at: [https://arxiv.org/pdf/2002.02836.pdf](https://arxiv.org/pdf/2002.02836.pdf), March 2020.
