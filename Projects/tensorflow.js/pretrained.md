---
layout: post_body
date: 2019-08-29
title: TensorFlow.js Pretrained model
tags: [Artificial Intelligence, Machine Learning]
featured-img: tfjs
img-type: jpg
permalink: Projects/tensorflow.js/pretrained.html
github: https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Google%20AI%20tools/tensorflow.js
---

<script src="script3.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"> </script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-vis"></script>

The dataset used for this example is the "Pima Indians Diabetes Database" dataset.

The features contained in this dataset are:
1. Pregnancies: Number of times pregnant
2. GlucosePlasma: glucose concentration a 2 hours in an oral glucose
tolerance test
3. BloodPressure: blood pressure (mm Hg)
4. SkinThickness: skin fold thickness (mm)
5. Insulin2-Hour: serum insulin (mu U/ml)
6. BMIBody: mass index (weight in kg/(height in m)^2)
7. DiabetesPedigreeFunction: pedigree function
8. Age: Age in years

And the label column (called Outcome) identifies if someone suffers or
not of Diabetes (268 of 768 cases are 1, the others are 0). This dataset
is available to download [here.](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

For this example, I first trained a model using Tensorflow Eager
Execution (executes operations immediately, without building graphs:
operations return concrete values instead of constructing a
computational graph to run later) to create a Multi Layer Perceptron in
Python. Finally, I saved this trained model and deploy it online at this
page ready to make predictions. The Python script I used to create this
model is available [here.](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/blob/master/Google%20AI%20tools/tensorflow.js/PreTrainedModel.ipynb)

You can use the buttons below to open or close the online Machine
Learning model window as you wish.

<button class="btn" id="show-visor">
  Display Visor
</button>

<button class="btn" id="hide-visor">
  Hide Visor
</button>

<button
  onclick="location.href='/Projects/tensorflow.js/tensorjs.html'"
  class="btn">
Previous Page
</button>
