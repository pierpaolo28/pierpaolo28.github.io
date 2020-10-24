---
layout: post
permalink: blog/blog40/
categories: [Machine Learning, Deployment]
---

![Photo by [R Mo](https://unsplash.com/@mooo3721?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10150/0*KhRA4Qyf8mV5QmtR)
Photo by [R Mo](https://unsplash.com/@mooo3721?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

# Deploying Machine Learning projects using Tkinter

## A complete guide towards deploying for free Machine Learning projects as applications in executable file format.

## Introduction

Thanks to a wide variety of open-source libraries, it is relatively easy nowadays to start exploring datasets and making some first predictions using simple Machine Learning (ML) algorithms in Python. Although, to make these trained models useful in the real world, it is necessary to share them and make them easily accessible on other users machines to make predictions. Only in this way Machine Learning can be used to provide benefit to society.

In this article, I will walk you through how to easily create a Graphical User Interface (GUI) for your Machine Learning project and then share your application as an executable file which can be run on other machines (whiteout needing the end-user to have Python or any library installed!). In case you are interested in finding out more, all the code used for this article (and more!) is available on [my GitHub profile](https://github.com/pierpaolo28/Data-Visualization/tree/master/Tkinter%20ML).

## Transfer Learning Image Classification

In order to shift our focus on the Graphical Interface development and deployment, in this article, we are going to use the VGG16 pre-trained model available on Tensorflow to easily build a Portable Image Classifier. In Video 1, is available a quick animation demonstrating the final workflow of our application.

![Video 1: GUI Demonstration](https://cdn-images-1.medium.com/max/2164/1*JjKKJ0PJGyhq5G1_AUVkwg.gif) <br>
Video 1: GUI Demonstration

Transfer Learning, is an area of research focused on transferring useful knowledge acquired by a Machine Learning model to another model which we are planning to use for a different (but still to some extent related) topic. This can be particularly useful when working with a limited amount of data (Figure 1).

![Figure 1: Transfer Learning Workflow ([Source](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a))](https://cdn-images-1.medium.com/max/2000/1*b4GiiiIgxhfd3pUd86ZUuw.png)
<br> Figure 1: Transfer Learning Workflow ([Source](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a))

One of the most common applications of transfer learning is [Computer Vision](https://towardsdatascience.com/roadmap-to-computer-vision-79106beb8be4). For example, in this article, we are going to use the [VGG16 model](https://neurohive.io/en/popular-networks/vgg16/) pre-trained on the [ImageNet dataset](http://www.image-net.org/) in order to quickly build a robust image classifier. In fact, the ImageNet dataset comprised of a huge amount of images (14 million) and about 21 thousand classes, making it therefore quite complete for this type of task.

Researchers are currently working on applying transfer learning techniques also in other fields such as Music [1] and Text classification [2].

## Graphical User Interface (GUI)

First of all, we need to import all our necessaries dependencies.

 <script src="https://gist.github.com/pierpaolo28/ea9bfb9e039c9f3d519668837f5a8374.js"></script>

Now, we can make use of the Tkinter library in order to create our Graphical Interface (as shown in Video 1). We start first by creating the base of our window (***root***) and we then add on top of it different elements such as a program title (***tit***), a frame (***frame***) a button to load an image to display on the frame (***chose_image***) and a button to fire our image classifier (***class_image***). Finally, we instantiate our VGG16 model and launch our GUI (***using root.mainloop()***).

<script src="https://gist.github.com/pierpaolo28/8bdf7a9f412e52dadabb67b1dd535c2d.js"></script>

In order to associate actions to perform when a user press either of the two GUI buttons, we can define two functions which get activated on click (***load_img()*** and ***classify()***).

In the ***load_img()*** function, we first clear the frame in case there is any widget attached, then we let the user upload an image and finally we rescale and display the image and its filename on the window frame.

<script src="https://gist.github.com/pierpaolo28/8c0f4b180e20de2b3e67005e46cedf9f.js"></script>

In the ***classify()*** function, we instead preprocess our image (using the [Keras guidelines](https://keras.io/applications/#vgg16) for this pre-trained model) and finally print on the frame the top 5 predictions of our classifier and it’s percentage confidence.

<script src="https://gist.github.com/pierpaolo28/1a74fa0f3d5e726478fff1b8aadf3991.js"></script>

Once our program is perfectly functioning locally, we can then export it into an executable format.

## Deployment

One of the easiest ways to convert a Python file into an executable (for either Windows or Linux platforms) is to use [Pyinstaller](https://www.pyinstaller.org/) (Figure 2).

![Figure 2: Pyinstaller [3]](https://cdn-images-1.medium.com/max/2000/1*06ypn4XciUhiWApn0wfMPA.jpeg)
<br> Figure 2: Pyinstaller [3]

In the case of a project with a single file and not too many dependencies, this can be done with just one command line statement:

    pyinstaller my_script_name.py

Although, for more complicated projects might be a better idea to create a virtual environment for the project and use a [Spec file](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) in order to give clear indications to Pyinstaller about how to create the executable and what assets to include. An example of Spec file for this project is available at [this link](https://github.com/pierpaolo28/Data-Visualization/blob/master/Tkinter%20ML/main.spec).

Finally, in case our executable might require different assets (eg. images, videos, etc…) then it could be a great idea to include everything in an installation system file using [NSIS](https://nsis.sourceforge.io/Download) (making so easier to install the executable and all the required dependencies on another machine).

In case you can be interested in using this application yourself, a download link is available on [my personal website.](https://pierpaolo28.github.io/Projects/project18.html)

Additionally, some alternative techniques which can be used in order to deploy Machine Learning systems are using:

* [Cloud Services](https://towardsdatascience.com/flask-and-heroku-for-online-machine-learning-deployment-425beb54a274) (eg. Heroku, AWS, Google Cloud)

* [Online Dashboards](https://towardsdatascience.com/interactive-dashboards-for-data-science-51aa038279e5) (eg. Dash, R-Shiny)

* Application Programming Interfaces (A.P.I.)

These techniques are widely used nowadays and they can make Machine Learning models easily available on the Web, although they will most likely incur in hosting charges (which are instead not needed using executables).

*I hope you enjoyed this article, thank you for reading!*

## Bibliography

[1] Transfer learning for music classification and regression tasks, Keunwoo Choi, György Fazekas. Accessed at: [https://arxiv.org/abs/1703.09179](https://arxiv.org/abs/1703.09179)

[2] A Practitioners’ Guide to Transfer Learning for Text Classification using Convolutional Neural Networks, Tushar Semwal, Gaurav Mathur. Accessed at: [https://arxiv.org/abs/1801.06480](https://arxiv.org/abs/1801.06480)

[3] Pyinstaller. Freeze (package) Python programs into stand-alone executables, Github. Accessed at: [https://github.com/pyinstaller/pyinstaller](https://github.com/pyinstaller/pyinstaller)
