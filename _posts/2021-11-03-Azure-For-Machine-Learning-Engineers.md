---
layout: post
permalink: blog/blog66/
categories: [Machine Learning]
---

![](https://miro.medium.com/max/2000/0*ZCTYT_miuLgAEwKa)Photo by [Markus Winkler](https://unsplash.com/@markuswinkler?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

# Azure for Machine Learning Engineers

## Getting an understanding of all the different AI services provided by Azure and when they should be used

# Introduction

As more and more companies decide to move their on-premises datacenters to the cloud, cloud skills are now becoming increasingly important.

In 2020, Microsoft Azure was declared the fastest growing cloud provider [1] and therefore I decided to challenge myself to learn more about their Data Science services and complete their [Azure Data Scientist certification](https://docs.microsoft.com/en-us/learn/certifications/azure-data-scientist/).

<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="bca2f766-dca5-42b1-a6d0-15805e137065" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>

In this article, we are going to cover some of Azure key Machine Learning services and how they compare each other in order to create complete AI solutions. If you are interested in learning more about the foundations of cloud computing and Big Data systems, additional information is available in my previous articles [“Cloud Foundations for Data Scientists”](https://towardsdatascience.com/cloud-foundations-for-data-scientists-e9d0c14fc98a) and [“Big Data Analysis: Spark and Hadoop”](https://towardsdatascience.com/big-data-analysis-spark-and-hadoop-a11ba591c057).

# Azure Services

Azure provides 4 different levels of abstraction, which can be used in order to create end to end Machine Learning solutions:

- Azure Applied AI Services
- Azure Cognitive Services
- Azure Machine Learning
- AI Infrastructure

## Azure Applied AI Services

At this level, Azure provides a set of specialist AI services designed with specific business scenarios in mind. These types of services have been built on top of the Azure Cognitive Services APIs in order to provide the end-user with different types of pre-made models ready to be used in specific business environments without almost any form of setup requirements. Some examples of Applied AI Services are:

- **Azure Form Recognizer:** to automatically extract knowledge from collections of documents and output the results in a structured data format able to provide pieces of information such as: relationships, bounding boxes, etc.
- **Azure Metrics Advisor:** to perform monitoring and anomaly detection of time series data in order to automatically calculate metrics from data and drive decisions.
- **Azure Cognitive Search:** makes it possible to use AI ranking capabilities to quickly find and explore the content available within an organization on a large scale.
- **Azure Bot Service:** makes use of pre-built natural language models in order to quickly build conversational bots. Azure Bot Service Composer additionally provides a visual interface in order to make it as easy as possible to create and test your virtual agent.

## Azure Cognitive Services

Cognitive Services is a collection of customisable APIs for tasks related to vision, speech, decision making and language. Making use of these APIs, you could then be able to integrate AI capabilities in your application without even having any expertise at all about Data Science and Machine Learning. It is possible to make use of Azure Cognitive Services by using many different methods such as: Azure Portal (the main Azure user interface), Azure Command Line Interface, SDK libraries (in languages such as C#, Java, JavaScript and Python) and Azure Resource Manager Templates. Some examples of capabilities available in Cognitive Services are:

- Speech to text conversion
- Speech Translation
- Speaker Recognition
- Anomaly Detection
- Content Moderation
- News Search using Bing
- Object Recognition

A quick example demonstrating how easy it can be to get started using the Cognitive Services API is available below (Figure 1).

![](https://miro.medium.com/max/2624/1*24kMMAM_6KLj8cq_PknG5g.png)
Figure 1: Azure Cognitive Services Computer Vision API in action (Image by Author).

## Azure Machine Learning (ML)

Azure ML is an end to end platform which can be used to prepare, build, train and deploy your own machine learning models and pipelines (instead of using pre-made models created by Microsoft). In order to make this possible, Azure provides both graphical interfaces (such as a drag and drop designer and AutoML capabilities) and coding environments (e.g. Jupyter Lab) to develop your own models using common open-source libraries such as Tensorflow, Keras, PyTorch, ONNX, etc…

Creating end deploying models in the same environment, makes then possible to follow common MLOps (Machine Learning → Operations) practices, keep track of ML experiments and monitor their performance over time in a production environment so that to react as quickly as possible in case of any data drift.

Some of the key capabilities provided by Azure Machine Learning are:

- Data Labelling
- Collaborative notebooks environment
- Automated Machine Learning tools for time series forecasting, classification and regression
- Creating ML pipelines using drag and drop tools
- Built-in MLOps capabilities
- Built-in model interpretability visualizations

A quick example demonstrating some of the different sections of the Azure Machine Learning platform is available below (Figure 2).

![](https://miro.medium.com/max/3840/1*7GwaoCXl9tDbfBciRvI54w.gif)
Figure 2: Azure Machine Learning platform (Image by Author).

## AI Infrastructure

Finally, Azure also provides different scalable Virtual Machines which can be selected by users in order to create and run their Machine Learning and Data Science projects. In this way, users are able to have complete control over their development environment and the different packages they would like to use.

Additionally, Azure also provides Data Science specific Virtual Machines which comes pre-packaged with some of the most common Data Science libraries (e.g. TensorFlow, Keras, MLFlow, etc…).

# Conclusion

Overall, Azure provides a complete suite of services that can be used in order to work with data at any stage of the analytics lifecycle. In addition to Microsoft AI services, Azure also provides a Marketplace on which users can decide to use AI-powered services created by other organizations such as Azure Databricks (for optimized Apache Spark), SAS Viya, DataRobot, Dataiku, H2O.ai, etc…

If you are interested in finding out more about other AI cloud providers services such as AWS, additional information is available in my previous article [“AWS for Machine Learning Engineers”](https://towardsdatascience.com/aws-for-machine-learning-engineers-47e50a3b8015).

# Bibliography

[1] Microsoft Azure is the fastest-growing cloud platform around. And they’ve got key needs you could fill. TheNextWeb. Accessed at: <https://thenextweb.com/news/microsoft-azure-is-the-fastest-growing-cloud-platform-around-and-theyve-got-key-needs-you-could-fill>
