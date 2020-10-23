---
layout: post
permalink: blog/blog1/
categories: [Artificial Intelligence]
---

![](https://cdn-images-1.medium.com/max/2200/1*kvjh_jOKaq5oqlOxjkxC8g.png)
<span class="figcaption_hack">
<br />
(Source =[https://www.datanami.com/2018/05/30/opening-up-black-boxes-with-explainable-ai/](https://www.datanami.com/2018/05/30/opening-up-black-boxes-with-explainable-ai/))</span>

# Need for Explainability in AI and Robotics

## Introduction

Breakthroughs in Artificial Intelligence (AI) taken place during the last few
years enabled possibilities for computers to perform tasks that would have been
impossible to do using traditional software programming. These advancements are
now opening up to us an entirely new world of potential applications for
Artificial Intelligence such as Robotics, Finance and Medicine. Examples of
modern AI applications can be: handwriting recognition, speech recognition, face
recognition, computer vision etc…

Use of AI in decision-making applications (such as employment) has recently
caused some concerns both for individuals and authorities. This is because, when
working with deep neural networks, it is currently not possible (at least to a
full extent) to understand the decision-making process the algorithm performs
when having to carry out a predetermined task. Because of this lack of
transparency in the decision-making process, perplexities can arise from the
public regarding the trustworthiness of the model itself. Therefore, the need
for Explainable AI is now becoming the next prefixed evolutionary step in order
to prevent the presence of any form of bias in AI models.

## Artificial Intelligence & Robotics

One of the main differences between traditional programming and AI is that
non-AI programs are written defying a set of instructions. Instead, AI models
learn without having to be explicitly programmed. This can, therefore, enable us
to perform tasks that seemed impossible using traditional programming. Machine
Learning (ML) is one of the most used AI tools. Some examples of how ML is
currently used can be:

* Predictions while Commuting
* Videos Surveillance
* Email Spam and Malware Filtering
* Search Engine Result Refining
* Product Recommendations
* Online Fraud Detection

Machine Learning can potentially also be used to enhance industrial robotic
systems abilities. As recent developments, particularly in Reinforcement
Learning and Deep Learning, clearly show that there is a huge potential in this
area.

There are two main types of robots. A traditional robot is a machine able to
perform repetitive highly specialised tasks (eg.industrial robots). Instead, an
intelligent robot is able to extract information from the surrounding
environment in order to make meaningful decisions (eg. behaviour based robots).

There are four main areas in which Machine Learning can be applied in robotics
[1]:

* Vision = detection and recognition of objects
* Grasping = determine best orientation and position to grasp objects
* Motion Control = obstacle avoidance and interaction
* Data = find patterns to decide the best action to take

Two examples of how Machine Learning can improve performance of robotics systems
are Multi-Robots Systems and Swarms. This is because both these classes of
robots mainly aim to perform complex tasks through collective behaviours.
Programming collective behaviour using traditional programming can become an
extremely challenging task, using Machine Learning (eg. Reinforcement Learning)
instead can make it easier and possibly lead to more innovative solutions we
couldn’t have thought of. The main differences between Multi-Robots systems and
Swarms are that the former has global knowledge of the environment and can have
a centralised architecture whilst the latter don’t have a global knowledge of
the environment and use a decentralised architecture.

A sub-field of Machine Learning that can have really important applications in
Robotics Systems is Deep Learning (DL). For example, DL algorithms using
Multi-Layer Artificial Networks have managed to perform incredibly well in tasks
such as image recognition which have really important applications in robotic
systems vision. One problematic area though of DL algorithms is that currently,
we are not able to fully track the decision making process the algorithm makes
when having to make a decision (therefore the needs for Explainable AI).

![](https://cdn-images-1.medium.com/max/2200/1*Vg9T26o9T59fAjyVi6BKQQ.jpeg)
<br />
<span class="figcaption_hack">Figure 1 — Relationship between AI-ML-DL (Image Reproduced from [2])</span>

## Ethics

The main aims of Explainable AI (XAI) is to make machines explain themselves and
to reduce the impact of biased algorithms (Figure 2). One example of how ethics
is becoming increasingly important in AI can be witnessed in the publication of
a list of ethical principles Google is promising to follow when implementing AI
algorithms [3]. Google decided to publish these principles to clarify in which
areas the implementation of AI can become dangerous and to confirm its interest
in producing AI self-explainable algorithms.

![](https://cdn-images-1.medium.com/max/2200/1*K2mq3O0Z9LUFZehSAV27ew.png)
<br />
<span class="figcaption_hack">Figure 2 — Explainable AI Revolution (Image Reproduced from [4])</span>

During the last few years, the first few XAI models have started being
developed. Some of the most successful ones are: Reversed Time Attention Model
(RETAIN), Local Interpretable Model-Agnostic Explanations (LIME) and Layer-wise
Relevance Propagation (LRP) [5]. Theses listed methods used for producing
explainable models are still nowadays not able to produce exhaustive results,
therefore research in this area is still in need of further developments.

## Bibliography

[1] Applying Artificial Intelligence and Machine Learning in Robotics, Robotic
Industries Applications. (Accessed:
[https://www.robotics.org/blog-article.cfm/Applying-Artificial-Intelligence-and-Machine-Learning-in-Robotics/103](https://www.robotics.org/blog-article.cfm/Applying-Artificial-Intelligence-and-Machine-Learning-in-Robotics/103))
January 2019

[2] Deep learning series 1: Intro to deep learning — Dhanoop Karunakaran —
Medium. (Accessed:
[https://medium.com/intro-to-artificial-intelligence/deep-learning-series-1-intro-to-deep-learning-abb1780ee20](https://medium.com/intro-to-artificial-intelligence/deep-learning-series-1-intro-to-deep-learning-abb1780ee20))
January 2019

[3] Artificial Intelligence at Google — Our Principles — Google AI. (Accessed:
[https://ai.google/principles/](https://ai.google/principles/)) January 2019

[4] Explainable Artificial Intelligence (XAI) — Mr. David Gunning —
DARPA.(Accessed:
[https://www.darpa.mil/program/explainable-artificial-intelligence](https://www.darpa.mil/program/explainable-artificial-intelligence))
January 2019

[5] An introduction to explainable AI, and why we need it — Patrick Ferris —
Medium. (Accessed:
[https://medium.freecodecamp.org/an-introduction-to-explainable-ai-and-why-we-need-it-a326417dd000](https://medium.freecodecamp.org/an-introduction-to-explainable-ai-and-why-we-need-it-a326417dd000))
January 2019
