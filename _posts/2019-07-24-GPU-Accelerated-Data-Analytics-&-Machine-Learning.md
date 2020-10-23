---
layout: post
permalink: blog/blog12/
categories: [Data Science, Machine Learning]
---

![](https://cdn-images-1.medium.com/max/2600/1*MvW5Sdj0r95REY0llCd3AQ.jpeg)
<span class="figcaption_hack">(Source:
[https://res.infoq.com/news/2018/10/Nvidia-keynote-gtc/en/resources/1BFA0900F-5083-497B-8275-B80D87C9CFF8-1539179054604.jpeg](https://res.infoq.com/news/2018/10/Nvidia-keynote-gtc/en/resources/1BFA0900F-5083-497B-8275-B80D87C9CFF8-1539179054604.jpeg))</span>

<!--end_excerpt-->

# GPU Accelerated Data Analytics & Machine Learning

## The future is here! Speed up your Machine Learning workflow using Python RAPIDS libraries support.

### Introduction

GPU acceleration is nowadays becoming more and more important. The main two
drivers for this shift are:

1.  The world’s amount of data is doubling every year [1].
1.  [Moore’s law](https://www.youtube.com/watch?v=2ugsWUv-DVs) is now coming to an
end because of limitations imposed by the quantum realm [2].

As a demonstration for this shift, an increasing number of online data science
platforms is now adding GPU enabled solutions. Some examples are: Kaggle, Google
Colaboratory, Microsoft Azure and Amazon Web Services (AWS).

In this article, I will first introduce you to the NVIDIA open-source Python
RAPIDS libraries and I will then offer you a practical demonstration of how
RAPIDS can speed up Data Analysis up to 50 times.

All the code used for this article is available on my
[GitHub](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/NVIDIA-RAPIDS%20AI)
and [Google
Colaboratory](https://colab.research.google.com/drive/1oEoAxBbZONUqm4gt9w2PIzmLTa7IjjV9)
for you to play with.

### RAPIDS

Many solutions have been proposed in the last few years in order to work with
large amounts of data. Some examples are [MapReduce, Hadoop and
Spark](https://towardsdatascience.com/big-data-analysis-spark-and-hadoop-a11ba591c057).

RAPIDS is now designed to be the next evolutionary step in data processing.
Thanks to its Apache Arrow in-memory format, RAPIDS can lead to up to around 50x
speed improvement compared to Spark in-memory processing (Figure 1).
Additionally, it is also able to scale from one to multi-GPUs [3].

All RAPIDS libraries are based on Python and are designed to have Pandas and
Sklearn like interfaces to facilitate adoption.

![](https://cdn-images-1.medium.com/max/2600/1*878gvZ3l8DXP357A1m55jg.png)
<span class="figcaption_hack">Figure 1: Data Processing Evolution [3]</span>

All RAPIDS packages are now free to be used on [Anaconda, Docker and cloud-based
solutions](https://rapids.ai/) such as Google Colaboratory.

RAPIDS structure is based on different libraries in order to accelerate data
science from end to end (Figure 2). Its main components are:

* cuDF = used to perform data processing tasks (Pandas like).
* cuML = used to create Machine Learning models (Sklearn like).
* cuGraph = used to perform graphing tasks ([Graph
Theory](https://www.analyticsvidhya.com/blog/2018/09/introduction-graph-theory-applications-python/)).

RAPIDS has additionally integration with: PyTorch & Chainer for Deep Learning,
Kepler GL for visualization, and Dask for distributed computation [4].

![](https://cdn-images-1.medium.com/max/2600/1*kYer2MYrg3akmZdn2Z8RaQ.png)
<span class="figcaption_hack">Figure 2: RAPIDS architecture [3]</span>

### Demonstration

I will now demonstrate to you how using RAPIDS can lead to a faster Data
Analysis compared to using Pandas and Sklearn. All the code I will be using is
available on [Google
Colaboratory](https://colab.research.google.com/drive/1oEoAxBbZONUqm4gt9w2PIzmLTa7IjjV9),
so feel free to test it out yourself!

In order to use RAPIDS, we need first of all to enable our Google Colaboratory
notebook to be used in GPU mode with a Tesla T4 GPU and then install the
required dependencies (guidance is available on my [Google Colabortory
notebook](https://drive.google.com/open?id=1oEoAxBbZONUqm4gt9w2PIzmLTa7IjjV9)).

#### Preprocessing

Once is everything set up, we can then import all the necessary libraries.

<script src="https://gist.github.com/pierpaolo28/566a64359db2440db7f4a7e50ac1cee2.js"></script>

In this example, I will show you how RAPIDS can speed up your Machine Learning
workflow compared to just using Sklearn. In this case, I decided to use Pandas
for preprocessing both the RAPIDS and Sklearn analysis. On my [Google
Colaboratory](https://drive.google.com/open?id=1oEoAxBbZONUqm4gt9w2PIzmLTa7IjjV9)
notebook is available also another example in which I use instead cuDF for
preprocessing. Using cuDF instead of Pandas, can lead to faster preprocessing
especially if working with a large amount of data.

For this example, I decided to fabricate a simple dataset using Gaussian
Distributions consisting of three features and two labels (0/1).

<script src="https://gist.github.com/pierpaolo28/fbd17893576019f4c29ebe3f01bcb226.js"></script>

The values of the means and standard deviations of the distributions have been
chosen so that to make this classification problem fairly easy (linearly
separable data).

![](https://cdn-images-1.medium.com/max/2000/1*MtzZAGyFwyf0LkeccAH7Ig.png) <br>
<span class="figcaption_hack">Figure 3: Sample Dataset</span>

Once created the dataset, I divided it features and labels and then defined a
function to preprocess it.

<script src="https://gist.github.com/pierpaolo28/5f45676f672689c78ded108862de6205.js"></script>

Now that we got our Training/Test sets we are finally ready to get started with
our Machine Learning. In this example, I will be using XGBoost (Extreme Gradient
Boosting) as classifier.

#### RAPIDS

In order to use XGBoost with RAPIDS we need first to convert our Training/Tests
inputs in matrix form.

<script src="https://gist.github.com/pierpaolo28/1329620ba8a603d8837e575fe7d93c21.js"></script>

Successively, we can start training our model.

<script src="https://gist.github.com/pierpaolo28/7642cc074fd7f0062fc909bb8b98d9b5.js"></script>

The output of the above cell is shown below. Using the XGBoost library provided
by RAPIDS took just under two minutes to train our model.

    CPU times: user 1min 54s, sys: 307 ms, total: 1min 54s
    Wall time: 1min 54s

Additionally RAPIDS XGBoost library provides also a really handy function to
rank and plot the importance of each feature in our dataset (Figure 4).

<script src="https://gist.github.com/pierpaolo28/e68f8bf70586585ff8dcd3372308668e.js"></script>

This can be really useful in order to reduce the dimensionality of our data. By
selecting just the most important features and training our model on it, we
would, in fact, reduce the risk to overfit our data and we would also speed up
training times. If you want to find out more about feature selection you can
read this [my
article](https://towardsdatascience.com/svm-feature-selection-and-kernels-840781cc1a6c)
about it.

![](https://cdn-images-1.medium.com/max/2000/1*Zuf5kYJa3j1fLKwr9OSY9A.png)
<span class="figcaption_hack">Figure 4: XGBoost Feature Importance</span>

Finally, we can now calculate the accuracy of our classifier.

<script src="https://gist.github.com/pierpaolo28/5a8bb1ae7b535d10f67e5357fdf30022.js"></script>

The overall accuracy of our model using RAPIDS was equal to 98%.

    XGB accuracy using RAPIDS: 98.0 %

#### Sklearn

I will now repeat the same analysis using plain Sklearn.

<script src="https://gist.github.com/pierpaolo28/45b1fabde7c642955ef71c3b5889ee82.js"></script>

In this occasion, it took just above 11 minutes to train our model. That means
using Sklearn for this problem size was 5.8 times slower than using RAPIDS
(662s/114s). By using cuDF instead of Pandas in the preprocessing stage we can
reduce the execution time even more for the overall workflow of this example.

    CPU times: user 11min 2s, sys: 594 ms, total: 11min 3s
    Wall time: 11min 2s

Finally, calculated the overall accuracy of the model using Sklearn.

<script src="https://gist.github.com/pierpaolo28/1f3112e5f3e96a919e28beefa8b07330.js"></script>

Also, in this case, the overall accuracy was equal to 98%. That means that using
RAPIDS can lead to faster results without compromising at all our model
accuracy.

    XGB accuracy using Sklearn: 98.0 %

#### Conclusion

As we can see from this example, using RAPIDS lead to a consistent decrease in
execution time.

This can be greatly important when working with large amounts of data since
RAPIDS would be able to reduce execution time from days to hours and from hours
to minutes.

RAPIDS offers valuable documentation and examples to make the most out of its
libraries. If you are interested in finding out more, some examples are
available [here](https://github.com/rapidsai/notebooks) and
[here](https://github.com/rapidsai/notebooks-extended).

I additionally created two other notebooks to explore RAPIDS cuGraph and Dask
libraries. If you are interested in finding out more, these are available
[here](https://drive.google.com/open?id=1cb40U3gdXZ7ASQsWZypzBFrrFOKpvnbB) and
[here](https://drive.google.com/open?id=1jrHoqh_zH7lIsWNsyfRaq0aUARkkW1s2).

### Bibliography

[1] What is Big Data? — A Beginner’s Guide to the World of Big Data. Anushree
Subramaniam, edureka! . Accessed at:
[https://www.edureka.co/blog/what-is-big-data/](https://www.edureka.co/blog/what-is-big-data/?source=post_page---------------------------)

[2] No More Transistors: The End of Moore’s Law. Interesting Engineering, John
Loeffler. Accessed at:
[https://interestingengineering.com/no-more-transistors-the-end-of-moores-law](https://interestingengineering.com/no-more-transistors-the-end-of-moores-law)

[3] RAPIDS: THE PLATFORM INSIDE AND OUT, Josh Patterson 10–23–2018. Accessed at:
[http://on-demand.gputechconf.com/gtcdc/2018/pdf/dc8256-rapids-the-platform-inside-and-out.pdf](http://on-demand.gputechconf.com/gtcdc/2018/pdf/dc8256-rapids-the-platform-inside-and-out.pdf)

[4] GPU-Accelerated Data Science | NVIDIA GTC Keynote Demo. Jensen Huang.
Accessed at:
[https://www.youtube.com/watch?v=LztHuPh3GyU](https://www.youtube.com/watch?v=LztHuPh3GyU)
