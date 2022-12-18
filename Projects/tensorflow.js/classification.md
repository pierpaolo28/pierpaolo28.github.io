---
layout: post_body
date: 2019-08-29
title: TensorFlow.js Classification
tags: [Artificial Intelligence, Machine Learning]
featured-img: tfjs
img-type: jpg
permalink: Projects/tensorflow.js/classification.html
github: https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Google%20AI%20tools/tensorflow.js
---

<script src="script2.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"> </script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-vis"></script>

The dataset used is for this example is the "Wine Data Set".

The features contained in this dataset are:
1. Fixed acidity
2. Volatile acidity
3. Citric acid
4. Residual sugar
5. Chlorides
6. Free sulphur dioxide
7. Total sulphur dioxide
8. Density
9. PH
10. Sulphates
11. Alcohol
12. Quality

And the label column (called style) identifies if a certain wine is
white (1) or red (0). This dataset is available to download [here.](https://www.kaggle.com/sgus1318/winedata)

If you are interested in a dataset analysis using Python instead of
TensorFlow.js, this is available [here.](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/blob/master/Google%20AI%20tools/tensorflow.js/Classfication.ipynb)

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
