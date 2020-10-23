---
layout: post
permalink: blog/blog41/
categories: [Machine Learning]
---

![Weka Tutorial -- GUI-based Machine Learning with Java](https://www.freecodecamp.org/news/content/images/size/w2000/2020/05/weka-1.png)
(Source: https://www.techiexpert.com/list-of-data-mining-tools/)

# Weka Tutorial – GUI-based Machine Learning with Java

## Introduction

Nowadays, programming languages such as Python and R are undoubtedly some of the most high in demand languages in Data Science and Machine Learning. Could it although be possible to perform common Machine Learning and Data Science tasks without necessarily be proficient in coding?

Of course we can! Weka is an Graphical User Interface based open-source package which can be used in order to perform common Data Science tasks just making use of the graphical interface.

## Basics

Weka can be easily installed on any type of platform by following the instructions at the following [link](https://waikato.github.io/weka-wiki/downloading_weka/), the only pre-requisite needed is having Java 8.0 installed on your local machine.

Once installed Weka, you will have a set of standard data processing and inference techniques such as:

-   ***Data Pre-processing:*** once loaded a dataset, Weka enables us to quickly explore it's attributes and instances. Additionally, different filtering techniques are available in order to for example convert categorical data into numerical or perform [feature selection](https://towardsdatascience.com/feature-selection-techniques-1bfab5fe0784) in order to reduce the dimensionality of our dataset (eg. to speed up training times and performance).
-   ***Classification and Regression Algorithms:*** a collection of different algorithms such as Gaussian Naive Bayes, Decision Trees, K-Nearest Neighbour, Ensembles techniques and various linear regression variants.
-   ***Clustering:*** this technique can be used in order to identify main categories in our data in an unsupervised way. Some examples algorithms available in the Weka collection are K-Means Clustering and Expectation Maximisation.
-   ***Discovering Associations:*** discovering rules in our dataset in order to more easily identify patterns and connections between the different features.
-   ***Data Visualisation:*** a suite of integrated data visualisation techniques to quickly visualise correlations between features and represent learned machine learning patterns such as Decision Trees and K-Means Clustering.

Another interesting feature of Weka, is the possibility to install new packages as they are created. One example of additional installation package is AutoML. AutoML can in fact be particularly useful for beginners which might find difficult to identify what Machine Learning model might be best to use for a specific task. Using Weka AutoML package, different Machine Learning models can be easily tested on the fly and it's [hyper-parameters](https://towardsdatascience.com/hyperparameters-optimization-526348bb8e2d) automatically tuned in order to increase performances.

Finally, for more expert users, Weka also offer a command line interface to use Java code. This can result particularly useful especially if working with large amount of data.

## Example

We are now going to walk through a simple example in order to demonstrate how to get started with Weka. First of all, we can start our analysis by opening Weka Explorer and opening our dataset (in this example the Iris Dataset).

![](https://www.freecodecamp.org/news/content/images/2020/05/image-153.png)

Figure 1: Importing and Visualising the data

Selecting the Classify tab, choosing as our classifier Naive Bayes and clicking start we can then quickly be able to achieve 96% classification accuracy without having to write any line of code!

![](https://www.freecodecamp.org/news/content/images/2020/05/image-154.png)

Figure 2: Naive Bayes Classification Results

## Conclusion

In case you are looking for more information about how to get started with Weka, [this YouTube series](https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal) by Google Developers is a great place where to start.
