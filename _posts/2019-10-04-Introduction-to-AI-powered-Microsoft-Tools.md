---
layout: post
permalink: blog/blog28/
categories: [Artificial Intelligence]
---

![](https://www.freecodecamp.org/news/content/images/size/w2000/2019/10/Microsoft-Ai-1.jpeg)
<span class="figcaption_hack">[(Source: https://2s7gjr373w3x22jf92z99mgm5w-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/MS-Research-AI.png)](https://2s7gjr373w3x22jf92z99mgm5w-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/MS-Research-AI.png)</span>

# Introduction to AI-powered Microsoft Tools
## A summary of some of the best AI tools provided by Microsoft and their future reseach advancements

### Introduction

Microsoft is nowadays one of the major providers for AI powered cloud services.
In fact, according to a RightScale's survey carried out in 2018, Microsoft Azure
Cloud services are currently second just to Amazon AWS (Figure 1).

In this article, I will be considering Microsoft as case study as Microsoft CEO
Satya Nadella recently shared Microsoft interest to make AI a vital part of
their business [1].

> “To be the leader in it, it's not enough just to sort of have AI capability
> that we can exercise—you also need the ability to democratise it so that every
business can truly benefit from it.”                                - Satya Nadella

![](https://www.freecodecamp.org/news/content/images/2019/10/stacking-up-cloud-vendors-2018-right-scale-1.png) <br>
<span class="figcaption_hack">Figure 1: 2018 Top Cloud Providers [2]</span>

I will now introduce you to some of the different Microsoft tools which are
currently available and some alternatives provided by the completion. Finally,
we will focus on what are going to be next steps in research.

### Microsoft AI Tools

Microsoft Azure currently provides a wide range of services which can be used to
create any sort of AI powered solutions. Some of the most important ones are:

* Azure Machine Learning Service
* Azure Machine Learning Studio
* Auto Machine Learning (ML)
* Azure Internet of Things (IoT)

#### Azure Machine Learning Service

Azure Machine Learning enables you to create, train and test Machine Learning
and Deep Learning models using Microsoft Cloud Services.

In this way, you don't have to worry anymore about memory and computational
power constraint of your local machine because all the work is executed on
Microsoft Servers.

When using Azure Machine Learning, all the main Python libraries comes
preinstalled (eg. Tensorflow, PyTorch, scikit-learn),  therefore reducing at
minimum set-up time. This enables developers to quickly create new models
without any type of constraint or environmental set up.

#### Azure Machine Learning Studio

Azure Machine Learning Studio enables users to perform Machine Learning tasks without
needing any programming experience.

ML models are created and tested just using a visual interface by dragging and
dropping all the model components (Figure 2). Once a model is ready to be
deployed in the real world, it can then be easily exported out of the Azure ML
Studio platform.

Right now, Azure Machine Learning Studio is mainly suitable for Clustering,
Classification and Regression tasks. Additionally, if desired,  it is possible
to add code in Python or R in Azure Machine Learning Studio to add more workflow
functionalities.

![](https://www.freecodecamp.org/news/content/images/2019/10/b391e301d2372a1c42bed40506a6ab5e7c072bb3_azure-ml-studio-1.jpg) <br>
<span class="figcaption_hack">Figure 2: Binary Classification in Azure Machine Learning Studio [3]</span>

#### Auto Machine Learning (ML)

Automated Machine Learning is currently one of the hottest topics in AI.

Nowadays Data Scientists and Machine Learning Engineers spends lots of their
time trying to identify the best Machine Learning model and Hyper-parameters to
use for each different prediction task. AutoML aims instead to automate this
process by creating software able to correctly identify and test Machine
Learning models (Figure 3).  

![](https://www.freecodecamp.org/news/content/images/2019/10/flow2.png) <br>
<span class="figcaption_hack">Figure 3: Azure AutoML [4]</span>

Automated Machine Learning is still an area in large development and it can be
used right now (with satisfactory results) just for a limited number of tasks.

AutoMl can be currently implemented using Microsoft Tools using either Azure
Machine Learning or
[ML.NET](https://dotnet.microsoft.com/apps/machinelearning-ai/ml-dotnet). Right
now, just classification and forecasting/regression problems can solved using
Microsoft services.

AutoML, can instead be implemented in Python using libraries such as
[Auto-sklearn](https://github.com/automl/auto-sklearn),
[TPOT](https://github.com/EpistasisLab/tpot) and
[H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html). Application of
AutoML in fields like Unsupervised Learning are currently still under
development.

#### Azure Internet of Things (IoT)

Azure is able to deliver both pre-customized and fully customizable solutions
for IoT services (Figure 4). In this way, Azure is able to provide solutions for
both beginners and experts in IoT. Microsoft Azure enables to easily scale IoT
systems to include devices from different manufacturers and also provides
analytics and Machine Learning services support.

If you are looking for a more detailed explanation on how the Internet of Things
is going to change our life and how it can be implemented using cloud services,
take a look at [my previous blog
post](https://www.freecodecamp.org/news/introduction-to-iot-internet-of-things/).

![](https://www.freecodecamp.org/news/content/images/2019/10/1519855877803.jpg) <br>
<span class="figcaption_hack">Figure 4: IoT Devices Workflow [5]</span>

### Research in Artificial Intelligence

Microsoft is now demonstrating a huge interest in AI. Right now, some of its
services such as Cortana, Skype or Office 365 are already starting making an
extensive use of AI. Additionally, just in 2018, Microsoft acquired 5 AI
companies.

Microsoft, also decided to create an organisation called Microsoft Research AI
to work on future developments of AI products. Some of the main topics currently
under research are: Bias in AI, Ethics and Interpretability.

#### Bias in AI

According to [Rich
Caruana](https://www.microsoft.com/en-us/research/people/rcaruana/), a senior
researcher at Microsoft, Microsoft is currently working on creating a
bias-detection tool [6].

Every Machine Learning model is trained using some input data. Although, at
times, the input data might contain some form of bias which might compromise the
model ability to correctly make predictions (eg. favourite a class compared to
another). Testing a trained model using a Bias-detection tool, could therefore
be of great help to minimise this risk.

In the meantime, also other companies such as Facebook and IBM are currently
working on implementing a similar tools for their corresponding businesses [6,
7].

#### Ethics

In April 2019, the European Commission published a list of [Ethics Guidelines
for Trustworthy
AI](https://ec.europa.eu/digital-single-market/en/news/ethics-guidelines-trustworthy-ai).
These principles, in addition to the previous application of [GDPR (General Data
Protection
Regulation)](https://digitalguardian.com/blog/what-gdpr-general-data-protection-regulation-understanding-and-complying-gdpr-data-protection),
defined quite a clear path of how end users should be given access to
fair/unbiased products and how their personal data should be protected.

Big companies such as Google, Facebook and Microsoft already started working
towards this direction and techniques such [Differential Privacy and Federated
Learning](https://towardsdatascience.com/ai-differential-privacy-and-federated-learning-523146d46b85)
have been created in order to protect users privacy in AI applications.

> “Artificial Intelligence brings great opportunity, but also great
> responsibility. We’re at that stage with AI where the choices we make need to be
grounded in principles and ethics – that’s the best way to ensure a future we
all want.”                                                         - Satya Nadella [8]

#### Interpretability

Use of AI in decision-making applications (such as medicine or law) has recently
caused some concerns both for individuals and authorities. This is because, when
working with complex Machine Learning models or deep neural networks, it is
currently not possible (at least to a full extent) to understand the
decision-making process the algorithm performs when having to carry out a
predetermined task.

One possible solution to this problem is Explainable AI (XAI). The main aims of
XAI are to make machines explain themselves and to reduce the impact of biased
algorithms.

Different algorithms have been implemented in last few years in order to make
models more explainable, some examples are: Reversed Time Attention Model
(RETAIN), Local Interpretable Model-Agnostic Explanations (LIME) and Layer-wise
Relevance Propagation (LRP). These can be implemented using Python libraries
such as: ELI5, Skater, SHAP and Microsoft InterpretML.

If you are interested in finding out more about Explainable AI, you can find
more information
[here](https://towardsdatascience.com/need-for-explainability-in-ai-and-robotics-75dc6077c9fa).

### Bibliography

[1] Microsoft CEO Satya Nadella On The Extraordinary Potential Of AI. Forbes,
[Bob Evans](https://www.forbes.com/sites/bobevans1/). Accessed at:
[https://www.forbes.com/sites/bobevans1/2018/06/04/microsoft-ceo-satya-nadella-on-the-extraordinary-potential-of-ai/#3c3c6383162f](https://www.forbes.com/sites/bobevans1/2018/06/04/microsoft-ceo-satya-nadella-on-the-extraordinary-potential-of-ai/#3c3c6383162f)

[2] Top cloud providers 2018: How AWS, Microsoft, Google, IBM, Oracle, Alibaba
stack up. ZDNet, [Larry
Dignan](https://www.zdnet.com/meet-the-team/us/larry-dignan/). Accessed at:
[https://www.zdnet.com/article/top-cloud-providers-2018-how-aws-microsoft-google-ibm-oracle-alibaba-stack-up/](https://www.zdnet.com/article/top-cloud-providers-2018-how-aws-microsoft-google-ibm-oracle-alibaba-stack-up/)

[3] Code free Data Science Microsoft Azure Machine Learning. Accessed at:
[https://gilberttanner-homepage.cdn.prismic.io/gilberttanner-homepage/b391e301d2372a1c42bed40506a6ab5e7c072bb3_azure-ml-studio-1.jpg](https://gilberttanner-homepage.cdn.prismic.io/gilberttanner-homepage/b391e301d2372a1c42bed40506a6ab5e7c072bb3_azure-ml-studio-1.jpg)

[4] Tutorial: Use automated machine learning to predict taxi fares. Microsoft
Azure Documentation. Accessed at:
[https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-auto-train-models](https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-auto-train-models)

[5] Smart Devices and Analytics Spur Innovation in the Internet of Things. Eric
Wetjen, MathWorks. Accessed at:
[https://www.mathworks.com/company/newsletters/articles/smart-devices-and-analytics-spur-innovation-in-the-internet-of-things.html](https://www.mathworks.com/company/newsletters/articles/smart-devices-and-analytics-spur-innovation-in-the-internet-of-things.html)

[6] Microsoft Creating Tool to Weed Out AI Bias. Dominique Adams, DIGIT.
Accessed at:
[https://digit.fyi/microsoft-ai-bias-detection/](https://digit.fyi/microsoft-ai-bias-detection/)

[7] IBM launches tool aimed at detecting AI bias. Zoe Kleinman, BBC. Accessed
at:
[https://www.bbc.co.uk/news/technology-45561955](https://www.bbc.co.uk/news/technology-45561955)

[8] Guidelines released for ethical and trustworthy AI. [Cornelia Kutterer -
Senior Director EU Government Affairs, AI, Privacy & Digital Policies,
Microsoft](https://blogs.microsoft.com/eupolicy/author/corneliakutterer/).
Accessed at:
[https://blogs.microsoft.com/eupolicy/2019/04/09/ethical-guidelines-trustworthy-ai/](https://blogs.microsoft.com/eupolicy/2019/04/09/ethical-guidelines-trustworthy-ai/)
