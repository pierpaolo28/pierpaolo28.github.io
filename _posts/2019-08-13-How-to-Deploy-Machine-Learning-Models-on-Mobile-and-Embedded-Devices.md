---
layout: post
permalink: blog/blog16/
categories: [Deployment]
---

![How to Deploy Machine Learning Models on Mobile and Embedded Devices](https://www.freecodecamp.org/news/content/images/size/w2000/2019/08/1_D3HyTjQ_zA2uKTwTZgd0Pg.png)(Source: https://tipsmake.com/google-launched-tensorflow-lite-10-for-mobile-devices-and-embedded-devices)

# How to Deploy Machine Learning Models on Mobile and Embedded Devices

## Introduction

Thanks to libraries such as Pandas, scikit-learn, and Matplotlib, it is relatively easy to start exploring datasets and make some first predictions using simple Machine Learning (ML) algorithms in Python. Although, to make these trained models useful in the real world, it is necessary to make them available to make predictions on either the Web or Portable devices.

In two of my previous articles, I explained how to create and deploy a simple Machine Learning model using [Heroku/Flask](https://towardsdatascience.com/flask-and-heroku-for-online-machine-learning-deployment-425beb54a274) and [Tensorflow.js](https://towardsdatascience.com/online-machine-learning-with-tensorflow-js-2ae232352901). Today, I will instead explain to you how to deploy Machine Learning models on Smartphones and Embedded Devices using TensorFlow Lite.

## TensorFlow Lite

TensorFlow Lite is a platform developed by Google to train Machine Learning models on mobile, IoT (Interned of Things) and embedded devices.

Using TensorFlow Lite, all the workflow is executed within the device, which avoids having to send data back and forth from a server. Some of the main advantages of doing this are:

-   Increased privacy since the data doesn't have to leave the device (this can allow you to apply techniques such as [Differential Privacy and Federated Learning](https://towardsdatascience.com/ai-differential-privacy-and-federated-learning-523146d46b85)).
-   Reduced power consumption, because no internet connection is required.
-   Decreased latency, since there is no communication with the server.

TensorFlow Lite offers API support for different languages such as Python, Java, Swift and C++.

A typical workflow using TensorFlow Lite would consist of:

1.  Creating and training a Machine Learning model in Python using TensorFlow.
2.  Converting our model in a suitable format for TensorFlow Lite using [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert/index).
3.  Deploying our Machine Learning model on our mobile device using [TensorFlow Lite interpreter](https://www.tensorflow.org/lite/guide/inference).
4.  Optimising the model memory consumption and accuracy.

There are several techniques which have been developed during the last few years in order to reduce the memory consumption of Machine Learning models [1]. One example is Model Quantization.

Model Quantization aims to reduce:

1.  The precision representations of Artificial Neural Networks weights (eg. converting 34.3456657 to 34.3).
2.  The memory access costs for reading and storing intermediate activation functions.

Using Model Quantization can therefore lead to a reduction in the model latency and size. One of the main drawbacks of this technique is a slight decrease in accuracy (which can be more or less important depending on the applications).

According to the TensorFlow Lite documentation, taking the Inception_v3 Image Classifier as example, using Model Quantization can lead to up to 0.8% decrease in accuracy. On the other hand, using Model Quantization made it possible to reduce the model size by 4 times (95.7MB vs 23.9MB) and the latency by 285ms (1130ms vs 845ms) [2].

In the following example, I will  demonstrate how to use a pre-trained model in an Android Application.

## Demonstration

As a practical example, I recently created an Android Studio App using the pre-trained Inception v3 Image Classifier thanks to TensorFlow Lite.

### Inception v3

The Inception Classifier was created in order to solve some limitations brought from creating very large and deep neural networks for image classification tasks.

A few years ago, in order to solve image classification tasks, were created deep learning models composed by an always increasing number of layers and neurons in each layer. Taking this approach, it was possible to score better results, but it also also led to two main problems:

1.  Increasing amount of computational power required to train our model.
2.  Increasing probability of overfitting (making our model perform really well during training stage but not so much when working with brand new data).

The creation of the Inception Classifier aimed instead to solve these problems by heavily engineering the characteristics of the model, increasing the training speed. During the last few years, different versions of the Inception classifier have been created. In the following example I decided to use the v3 version.

### Android Image Classifier

In order to create this App, I decided to use Android Studio as the IDE. In this way, it was relatively easy to integrate all the required TensorFlow Lite dependencies to load the Inception v3 model.

I successively decided to divide this App in two main windows:

-   In the first one, the user is welcomed and is asked to select the image classifier to use (in this case the "Inception Quantized Classifier"). Then, the user is asked to take a picture of the object they want to classify and finally the picture is cropped. In this case, it was necessary to crop the image since the Inception Classifier takes just squared images as inputs.
-   In the second window, the user is finally ask to click on the "Classify Image" button in order to get in return the 3 most likely predictions made by the classifier.

![](https://www.freecodecamp.org/news/content/images/2019/08/ezgif.com-optimize.gif) <br>
<span class="figcaption_hack">Simple Android Image Classifier</span>

In order to realise this project, I referenced Michael Shea and the TensorFlow Lite documentation implementations [3, 4].

If you are interested in testing out yourself this App, all the code and an Apk of the App is available in [my Github repository](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Google%20AI%20tools/TensorFlow-Lite-Image-Classifier).

In case you are planning to start your own project using TensorFlow Lite, their [documentation](https://www.tensorflow.org/lite/guide/get_started) is probably to best place where to start.

### Bibliography

[1] Nimit S. Sohoni, Christopher R. Aberger et al, Low-Memory Neural Network Training: A Technical Report. Accessed at: <https://arxiv.org/pdf/1904.10631.pdf>

[2] Model optimization, TensorFlow. Accessed at: <https://www.tensorflow.org/lite/performance/model_optimization>

[3] Michael Shea, TensorFlow Lite Inception Model Android Tutorial. Accessed at: <https://www.youtube.com/watch?v=8zQsAl2z4iU>

[4] TensorFlow Lite Documentation, TensorFlow Lite image classification Android example application. Accessed at: <https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android>
