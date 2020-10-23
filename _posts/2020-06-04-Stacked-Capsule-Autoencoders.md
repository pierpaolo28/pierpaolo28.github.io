---
layout: post
permalink: blog/blog42/
categories: [Extra, Deep Learning]
---

![Photo by [Will B](https://unsplash.com/@willbro?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/12000/0*XfosbY2xJCLpQlCC) Photo by [Will B](https://unsplash.com/@willbro?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

# Stacked Capsule Autoencoders

## A look into the future of object detection in images and videos using Unsupervised Learning and a limited amount of training data.

## Introduction

During the last few years, [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) and a team of researchers started working on a revolutionary new type of neural network based on Capsules.

Some of the main motivations behind this study are that current neural networks like [Convolutional Neural Networks (CNNs)](https://en.wikipedia.org/wiki/Convolutional_neural_network) are able to achieve the state of the art accuracy in [computer vision](https://towardsdatascience.com/roadmap-to-computer-vision-79106beb8be4) tasks such as object detection only if provided a large amount of data.

One of the main reason why models like CNNs require such a large amount of data is their inability to capture orientational and spatial relationships between the different elements which compose an image. In fact, one of the main techniques used in order to improve CNNs performances is Data Augmentation. When applying Data Augmentation, we help our model learn more in-depth and in a more general way what characterises different objects by creating additional data from the original one by for example rotating, cropping, flipping, etc… the original images. In this way, our model will more likely be able to recognise the same object even if seen from a different perspective (Figure 1).

![Figure 1: Viewing the same object from a different perspective can cause misconception [1].](https://cdn-images-1.medium.com/max/2000/1*raMNsT7H947BObauwCRttQ.png)

Figure 1: Viewing the same object from a different perspective can cause misconception [1].

CNNs are able to detect objects by first identifying edges and shapes in an image and then combining them together. This approach although does not take into account spacial hierarchies which construct the overall image, and therefore leading to the need of creating large datasets in order to perform well (increasing therefore also the computational cost necessary in order to train the model).

## Capsules

Geoffrey Hinton approach of using Capsules closely follow instead the principle of Inverse Graphic. In fact, according to Hinton, every time our brain processes a new object, its representation does not depend on the viewing angle. Therefore, in order to create models able to perform object recognition as good as our brain can do, we need to be able to capture the hierarchical relationship of the different parts which compose an object and relate them with respect to a frame of coordinates.

This can be achieved by basing our network on a structure called Capsule. A capsule is a data structure incorporating in a vector form all the main information of the feature we are detecting. Its main constituents are:

 1. A logistic unit which represents if a shape exists in an image.

 2. A matrix representing the [pose](http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/MARBLE/high/pose/express.htm) of the shape.

 3. A vector embedding other information such as colour, deformations, etc…

Different approaches have been proposed by Hinton research team during the last few years in order to create Capsule Network such as:

* 2017: [Dynamic Routing](https://arxiv.org/abs/1710.09829) (discriminative learning and part-whole relationships).

* 2018: [Expectation–maximization Algorithm](https://www.cs.toronto.edu/~hinton/absps/EMcapsules.pdf) (discriminative learning and part-whole relationships).

* 2019: [Stacked Capsule Networks](https://arxiv.org/abs/1906.06818) (unsupervised Learning, whole parts relationships).

In Capsule Networks, the different neurons compete with each other in order to find agreeing parts which compose objects in images. Three different approaches can be used in order to measure agreements between different capsules:

* Using cosine distance as a measure of agreement.

* Expectation-Maximization.

* Mixture Models.

As shown in Figure 2, basing our system on understanding objects on the grounds of geometric relationships we can then enable our model to be able to reliably detect an object (even if captured from a different point of view or under different light conditions) providing just one instance of it during training (no Data Augmentation needed).

![Figure 2: Object Detection from different points of view [2]](https://cdn-images-1.medium.com/max/2000/1*gHnUO-A3vYj0qtqHXSkGPw.png)

Figure 2: Object Detection from different points of view [2]

## Stacked Capsule Networks

One of the additions to the 2019 approach to create capsule networks, is the ability to perform object detection in an unsupervised way therefore not having the need to label our data.

This model architecture can be divided into 3 main different stages such as:

* Constellation Autoencoder (CCAE): at this stage, an autoencoder model is trained in an unsupervised way to maximise part capsules likelihood.

* Part Capsule Autoencoder (PCAE): our input images are divided into constituent parts in order to infer objects poses.

* Object Capsule Autoencoder (OCAE): the created parts get organised together with their corresponded poses to recreate objects.

Combining these three stages together we can then get our final Stacked Capsule Network. The whole process can be summarised in the workflow in Figure 3.

![Figure 3: Stacked Capsule Networks General Workflow [3]](https://cdn-images-1.medium.com/max/2400/1*W_mGUOZzEYyeZnUchnq0WQ.jpeg)

Figure 3: Stacked Capsule Networks General Workflow [3]

If you are interested in finding out more about Stacked Capsule Networks, additional information about the topic is provided in the following video presentation by Geoff Hinton at the AAAI 2020 Turing Awards from around minute 3 till minute 34.

<div>
<iframe width="560" height="315" src="https://www.youtube.com/embed/UX8OubxsY8w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Video 1: AAAI 2020 Turing Awards

*****
*I hope you enjoyed this article, thank you for reading!*

## Bibliography

[1] 10 Certainties About the Truth, KOET, Lisa Beebe. Accessed at: [https://www.kcet.org/arts-entertainment/10-certainties-about-the-truth](https://www.kcet.org/arts-entertainment/10-certainties-about-the-truth)

[2] Matrix Capsules with EM routing, Geoffrey Hinton, Sara Sabour, Nicholas Frosst — Google Brain. Accessed at: [https://openreview.net/pdf?id=HJWLfGWRb](https://openreview.net/pdf?id=HJWLfGWRb)

[3] Stacked Capsule Autoencoders, Adam Kosiorek. Accessed at: [http://akosiorek.github.io/ml/2019/06/23/stacked_capsule_autoencoders.html](http://akosiorek.github.io/ml/2019/06/23/stacked_capsule_autoencoders.html)
