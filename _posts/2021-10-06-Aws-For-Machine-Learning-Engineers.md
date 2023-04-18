---
layout: post
permalink: blog/blog64/
categories: [Machine Learning]
---

![](https://miro.medium.com/max/2000/0*Qo_I7nT3b-NsSLVl)Photo by [Alex Kulikov](https://unsplash.com/@burntime?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

# AWS for Machine Learning Engineers

## Exploring some of the key services provided by AWS in order to solve data-driven challenges.

# Introduction

One of the key trends in tech over the last few years has been the constant increase in demand for cloud computing as more and more companies decide to move on-premises datacenters to cloud providers.

In 2020, the cloud computing market size was equal to USD 371.4 billion and by 2025 is projected to reach about USD 832.1 billion [1]. As of 2021, AWS is currently the leading cloud provider in the world by market share [2].

I recently completed the [AWS Machine Learning Speciality exam](https://aws.amazon.com/certification/certified-machine-learning-specialty/) (Figure 1), and I, therefore, decided to make a summary of the key services a Data Scientist might use when working on a project on AWS.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Delighted to have successfully completed the <a href="https://twitter.com/awscloud?ref_src=twsrc%5Etfw">@awscloud</a> Machine Learning Specialty Certification with a score of 970/1000. <br><br>If you are interested in learning more about <a href="https://twitter.com/hashtag/CloudComputing?src=hash&amp;ref_src=twsrc%5Etfw">#CloudComputing</a> and <a href="https://twitter.com/hashtag/DataScience?src=hash&amp;ref_src=twsrc%5Etfw">#DataScience</a>, then feel free to start following me✅<a href="https://t.co/Xm8omw3ndp">https://t.co/Xm8omw3ndp</a></p>&mdash; Pier Paolo Ippolito (@Pier_Paolo_28) <a href="https://twitter.com/Pier_Paolo_28/status/1429443322272260107?ref_src=twsrc%5Etfw">August 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
Figure 1: [AWS ML Exam Completion Tweet](https://twitter.com/Pier_Paolo_28) (Image by Author).

If you are interested in learning more about the foundations of cloud computing, additional information is available in my previous article [“Cloud Foundations for Data Scientists”](https://towardsdatascience.com/cloud-foundations-for-data-scientists-e9d0c14fc98a).

# AWS Services

AWS provides 3 different levels of abstraction, which you can use in order to create Machine Learning solutions: Artificial Intelligence (AI) Services, ML Services, ML Frameworks and Infrastructure.

## Artificial Intelligence Services

At this level, we can find all AWS AI services focused on ease of use and high speed to market. These services are fully managed by AWS and make it possible to add Machine Learning capabilities to your product by just making API calls to highly performing models already pre-trained by AWS. In this way, anyone can be able to make use of AI services even without having any prior experience in ML. Some examples of Artificial Intelligence Services are:

- **Amazon Comprehend:** is a Natural Language Processing (NLP) service designed in order to analyse large amounts of unstructured text data (e.g. identify the language, key facts from the text, the overall sentiment, etc.)
- **Amazon Polly:** is a Deep Learning enabled text to speech service which can be used in order to create talk based applications.
- **Amazon Transcribe:** is speech to text service used in order to convert audio files into text files. This kind of service is able to provide reliable performances with both batch and live streaming data.
- **Amazon Translate:** is a Deep Learning based language translation service.
- **Amazon Rekognition:** is a service designed in order to get insights from images and videos (e.g. object/people detection, content moderation, etc.).
- **Amazon Personalize:** is a recommendations system designed in order to make it easy to provide real-time products ranking, customised marketing and recommendations based on user interactions.

A quick example demonstrating how easy it can be to get started using Amazon Rekognition is available below (Figure 2).

![](https://miro.medium.com/max/3840/1*l5k62_P8Ys3eHCj4D7Y3ng.gif)<br>
Figure 2: Amazon Rekognition Demo (Image by Author).

## ML Services

ML Services focuses on providing managed resources and services to Data Scientists and Researchers in order to enable them to create and deploy Machine Learning models without having to spend too much time setting up the architecture supporting their models. Some examples of ML Services are:

- **Amazon SageMaker:** is a fully managed service designed to cover the entire Machine Learning workflow, from data preparation to deployment and monitoring (Figure 3). Some of the most interesting options available in Amazon Sagemaker are: **Data Wrangler** (a GUI based data preparation tool), a built-in **Feature Store**, **Autopilot** (AWS Automatic ML service), **Pipelines** (for orchestrating automation workflows), etc. If you are interested in learning more about Sagemaker and its capabilities, additional information is available at [this link.](https://www.youtube.com/watch?v=CK_xC4T1blk)
- **Amazon SageMaker Ground Truth:** is a service designed in order to create datasets labels for Machine Learning tasks. Using this service it can be possible to choose either AI-powered automatic labelling tools or to send your data to a human workforce for manual labelling. Additionally, it can also be possible to let the service automatically label instances for which it has high confidence and send the remaining ones to the human workforce (saving therefore time and costs). Currently, Ground Truth is able to support different types of data such as text, images and videos.
- **Amazon SageMaker Neo:** makes it possible to deploy a Machine Learning model anywhere (on the Cloud or IoT Edge Devices) once trained. SageMaker Neo, makes this possible by taking a model trained in any of the major ML frameworks (e.g. Keras, PyTorch, [ONNX](https://towardsdatascience.com/onnx-easily-exchange-deep-learning-models-f3c42100fd77)) and then converts it into an optimised binary representation so that to reduce the amount of memory used to make inference with the model.
- **Amazon Augmented AI:** is a service designed in order to create production ML models which keeps humans in the loop. For some applications such as Finance or Medicine, predictions made by ML models could be really important and have longstanding impacts. Using Augmented AI, we can be able to create workflows to make it possible for humans to check over model predictions and change them when necessary in order to provide feedback to the model (for potential re-training) and improve performances at the same time.

![](https://miro.medium.com/max/3840/1*RuL35SfGmrH4qPHo1QxYtg.png)<br>
Figure 3: Amazon Sagemaker Dashboard (Image by Author).

## ML Frameworks and Infrastructure

This level is designed to enable Machine Learning experts to create their models using traditional open-source frameworks such as PyTorch, TensorFlow, and Apache MXNet on AWS. AWS provides different machine images designed to run high-performance Machine Learning workflows such as Deep Learning AMI and Deep Learning Containers (which all comes with the different ML frameworks already installed). In this way, ML practitioners don’t have to worry anymore about conflicts with libraries dependencies and limited computing capabilities.

# Conclusion

Overall, AWS provides an impressive suite of services that can be used in order to use data at any stage of the analytics lifecycle (e.g. Data Ingestion, Data Storage, Data Processing, Data Analytics, etc…). If you are interested in finding out more about other AI cloud providers services such as Microsoft Azure, additional information is available in my previous article [“Introduction To Ai Powered Microsoft Tools”](https://ppiconsulting.dev/blog/blog28/).

# Bibliography

[1] Globenewswire, Research and Markets. Accessed at: <https://www.globenewswire.com/news-release/2020/08/21/2081841/0/en/Cloud-Computing-Industry-to-Grow-from-371-4-Billion-in-2020-to-832-1-Billion-by-2025-at-a-CAGR-of-17-5.html>

[2] Statista, Amazon Leads \$150-Billion Cloud Market. Accessed at: <https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/>
