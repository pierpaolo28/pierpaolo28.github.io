---
layout: post
permalink: blog/blog43/
categories: [Data Science]
---

![Photo by [Kelly Sikkema](https://unsplash.com/@kellysikkema?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/11136/0*x2fhqjKco9CZsfeK)Photo by [Kelly Sikkema](https://unsplash.com/@kellysikkema?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

# Roadmap to Natural Language Processing (NLP)

## An introduction to some of the most common technique and models used in Natural Language Processing (NLP)

## Introduction

Due to the development of [Big Data](https://towardsdatascience.com/big-data-analysis-spark-and-hadoop-a11ba591c057) during the last decade. organizations are now faced with analysing large amounts of data coming from a wide variety of sources on a daily basis.

Natural Language Processing (NLP) is the area of research in Artificial Intelligence focused on processing and using Text and Speech data to create smart machines and create insights.

One of nowadays most interesting NLP application is creating machines able to discuss with humans about complex topics. [IBM Project Debater](https://www.research.ibm.com/artificial-intelligence/project-debater/) represents so far one of the most successful approaches in this area.

 <div>
 <iframe width="560" height="315" src="https://www.youtube.com/embed/naQujxmg9gg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
 </div>
 <span class="figcaption_hack">Video 1: IBM Project Debater</span>
 <br>

## Preprocessing Techniques

Some of the most common techniques which are applied in order to prepare text data for inference are:

* **Tokenization:** is used to segment the input text into its constituents words (tokens). In this way, it becomes easier to then convert our data into a numerical format.

* **Stop Words Removal:** is applied in order to remove from our text all the prepositions (eg. “an”, “the”, etc…) which can just be considered as a source of noise in our data (since they do not carry additional informative information in our data).

* **Stemming:** is finally used in order to get rid of all the affixes in our data (eg. prefixes or suffixes). In this way, it can in fact become much easier for our algorithm to not consider as distinguished words which have actually similar meaning (eg. insight ~ insightful).

All of these preprocessing techniques can be easily applied to different types of texts using standard Python NLP libraries such as [NLTK](https://www.nltk.org/) and [Spacy](https://spacy.io/).

Additionally, in order to extrapolate the language syntax and structure of our text, we can make use of techniques such as Parts of Speech (POS) Tagging and Shallow Parsing (Figure 1). Using these techniques, in fact, we explicitly tag each word with its lexical category (which is based on the phrase syntactic context).

![Figure 1: Parts of Speech Tagging Example [1].](https://cdn-images-1.medium.com/max/2000/1*fRsFnY3Nk7y0hWcBbnzy6A.png)<br> Figure 1: Parts of Speech Tagging Example [1].

## Modelling Techniques

### Bag of Words

Bag of Words is a technique used in Natural Language Processing and [Computer Vision](https://towardsdatascience.com/roadmap-to-computer-vision-79106beb8be4) in order to create new features for training classifiers (Figure 2). This technique is implemented by constructing a histogram counting all the words in our document (not taking into account the word order and syntax rules).

![Figure 2: Bag of Words [2]](https://cdn-images-1.medium.com/max/2000/1*ZBBlFr8_uj5owi4Z_YhzOw.jpeg)<br> Figure 2: Bag of Words [2]

One of the main problems which can limit the efficacy of this technique is the presence of prepositions, pronouns, articles, etc… in our text. In fact, these can all be considered as words which are likely to appear frequently in our text even without necessarily being really informative in finding out what are the main characteristics and topics in our document.

In order to solve this type of problem, a technique called “Term Frequency-Inverse Document Frequency” (TFIDF) is commonly used. TFIDF aims to rescale the words count frequency in our text by considering how frequently each of the words in our text appears overall in a large sample of texts. Using this technique, we will then reward words (scaling up their frequency value) which appear quite commonly in our text but rarely in other texts, while punishing words (scaling down their frequency value) which appear frequently in both our text and other texts (such as prepositions, pronouns, etc…).

### Latent Dirichlet Allocation (LDA)

Latent Dirichlet Allocation (LDA) is a type of Topic Modelling technique. Topic Modelling is a field of research focused on finding out ways to cluster documents in order to discover latent distinguishing markers which can characterize them based on their content (Figure 3). Therefore, Topic Modelling can also be considered in this ambit as a [dimensionality reduction technique](https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be) since it allows us to reduce our initial data to a limited set of clusters.

![Figure 3: Topic Modelling [3]](https://cdn-images-1.medium.com/max/2000/1*Gct6iypi9qL8ZJ-kIWAswA.png)<br> Figure 3: Topic Modelling [3]

Latent Dirichlet Allocation (LDA) is an unsupervised learning technique used to find out latent topics which can characterize different documents and cluster together similar ones. This algorithm takes as input the number ***N*** of topics which are believed exists and then groups the different documents into ***N*** clusters of documents which are closely related to each other.

What characterises LDA from other clustering techniques such as K-Means Clustering is that LDA is a soft-clustering technique (each document is assigned to a cluster based on a probability distribution). For example, a document can be assigned to a Cluster A because the algorithm determines that it is 80% likely that this document belongs to this class, while still taking into account that some characteristics embedded into this document (the remaining 20%) are more likely to belong instead to a second Cluster B.

### Word Embeddings

Word Embeddings are one of the most common ways to encode words as vectors of numbers which can then fed in into our Machine Learning models for inference. Word Embeddings aim to reliably transform our words into a vector space so that similar words are represented by similar vectors.

![Figure 4: Word Embedding [4]](https://cdn-images-1.medium.com/max/2000/1*gTia0WpgIGM8nAfJQndMhw.png)<br> Figure 4: Word Embedding [4]

Nowadays, there are three main techniques used in order to create Word Embeddings: [Word2Vec](https://en.wikipedia.org/wiki/Word2vec), [GloVe](https://en.wikipedia.org/wiki/GloVe_(machine_learning)) and [fastText](https://en.wikipedia.org/wiki/FastText). All these three techniques, use a shallow neural network in order to create the desired word embedding.

In case you can be interested in finding out more about how Word Embeddings works, [this article is a great place where to start.](https://machinelearningmastery.com/what-are-word-embeddings/)

### Sentiment Analysis

Sentiment Analysis is an NLP technique commonly used in order to understand if some form of text expresses positive, negative or neutral sentiment about a topic. This can be particularly useful to do when for example trying to find out what is the general public opinion (through online reviews, tweets, etc…) about a topic, product or a company.

In sentiment analysis, sentiments in texts are usually represented as a value between -1 (negative sentiment) and 1 (positive sentiment) referred to as polarity.

Sentiment Analysis can be considered as an Unsupervised Learning technique since we are not usually provided with handcrafted labels for our data. In order to overcome this obstacle, we make use of prelabeled lexicons (a book of words) which had been created to quantify the sentiment of a large number of words in different contexts. Some examples of widely used lexicons in sentiment analysis are [TextBlob](https://github.com/sloria/TextBlob/tree/eb08c120d364e908646731d60b4e4c6c1712ff63) and [VADER](https://github.com/cjhutto/vaderSentiment).

## Transformers

[Transformers](http://jalammar.github.io/illustrated-transformer/) represent the current state of the art NPL models in order to analyse text data. Some examples of widely known Transformers models are [BERT](https://arxiv.org/abs/1810.04805) and [GTP2](https://openai.com/blog/better-language-models/).

Before the creation of Transformers, Recurrent Neural Networks (RNNs) represented the most efficient way to analyse sequentially text data for prediction but this approach found quite difficult to reliably make use of long term dependencies (eg. our network might find difficult to understand if a word fed in several iterations ago might result to be useful for the current iteration).

Transformers successfully managed to overcome this limitation thanks to a mechanism called [Attention](https://arxiv.org/pdf/1706.03762.pdf) (which is used in order to determine which parts of the text to focus on and give more weight). Additionally, Transformers made easier to process text data in parallel rather than sequentially (therefore improving execution speed).

Transformers can nowadays be easily implemented in Python thanks to [Hugging Face library](https://huggingface.co/).

### Text Prediction Demonstration

Text prediction is one of the tasks which can be easily implemented using Transformers such as GPT2. In this example, we will give as input a quote from “[The Shadow of the Wind](https://en.wikipedia.org/wiki/The_Shadow_of_the_Wind)” by Carlos Ruiz Zafón and our transformer will then generate other 50 characters which should logically follow our input data.

<script src="https://gist.github.com/pierpaolo28/cb0242a1e48688ef199c3f7a0e2ebfb7.js"></script>

    A book is a mirror that offers us only what we already carry inside us.
    It is a way of knowing ourselves, and it takes a whole life of self
    awareness as we become aware of ourselves. This is a real lesson
    from the book My Life.

As can be seen from our example output shown above, our GPT2 model performed quite well in creating a resealable continuation for our input string.

An example notebook which you can run in order to generate your own text is available at [this link.](https://drive.google.com/open?id=1UVfieBsf4gb6J_s_FaRA93D0ueO4-7JE)

*I hope you enjoyed this article, thank you for reading!*

## Bibliography

[1] Extract Custom Keywords using NLTK POS tagger in python, Thinkinfi, Anindya Naskar. Accessed at: [https://www.thinkinfi.com/2018/10/extract-custom-entity-using-nltk-pos.html](https://www.thinkinfi.com/2018/10/extract-custom-entity-using-nltk-pos.html)

[2] Comparison of word bag model BoW and word set model SoW, ProgrammerSought. Accessed at: [http://www.programmersought.com/article/4304366575/;jsessionid=0187F8E68A22612555B437068028C012](http://www.programmersought.com/article/4304366575/;jsessionid=0187F8E68A22612555B437068028C012)

[3] Topic Modeling: Art of Storytelling in NLP,
TechnovativeThinker. Accessed at: [https://medium.com/@MageshDominator/topic-modeling-art-of-storytelling-in-nlp-4dc83e96a987](https://medium.com/@MageshDominator/topic-modeling-art-of-storytelling-in-nlp-4dc83e96a987)

[4] Word Mover’s Embedding: Universal Text Embedding from Word2Vec, IBM Research Blog. Accessed at: [https://www.ibm.com/blogs/research/2018/11/word-movers-embedding/](https://www.ibm.com/blogs/research/2018/11/word-movers-embedding/)
