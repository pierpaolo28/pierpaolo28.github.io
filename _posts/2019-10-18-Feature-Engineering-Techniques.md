---
layout: post
permalink: blog/blog30/
categories: [Data Science]
---

![](https://cdn-images-1.medium.com/max/2600/0*qppSymXYGZ7PxA24)
<span class="figcaption_hack">Photo by ["My Life Through A
Lens"](https://unsplash.com/@bamagal?utm_source=medium&utm_medium=referral) on
[Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)</span>

<!--end_excerpt-->

# Feature Engineering Techniques

## An introduction to some of the main techniques which can be used in order to prepare raw features for Machine Learning analysis.

### Introduction

Feature Engineering is one of the most important steps to complete before
starting a Machine Learning analysis. Creating the best possible Machine
Learning/Deep Learning model can certainly help to achieve good results, but
choosing the right features in the right format to fed in a model can by far
boost performances leading to the following benefits:

* Enable us to achieve good model performances using simpler Machine Learning
models.
* Using simpler Machine Learning models, increases the transparency of our model,
therefore making easier for us to understand how is making its predictions.
* Reduced need to use Ensemble Learning techniques.
* Reduced need to perform [Hyperparameters Optimization](https://towardsdatascience.com/hyperparameters-optimization-526348bb8e2d).

Other common techniques which can be used in order to make the best use out of
the given data are [Features
Selection](https://towardsdatascience.com/feature-selection-techniques-1bfab5fe0784)
and
[Extraction](https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be),
of which I talked about in my previous posts.

We will now walk through some of the most common Feature Engineering techniques.
Most of the basic Feature Engineering techniques consist of **finding
inconstancies** in the data and of **creating new features** by combining/diving
existing ones.

All the code used for this article is available on my GitHub account at [this
link](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/blob/master/Features%20Analysis/FeatureEngineering.ipynb).

For this example, I decided to create a simple dataset which is affected by some
of the most common problems which are faced during a Data Analysis (eg. Missing
numbers, outlier values, scaling issues, …).

<script src="https://gist.github.com/pierpaolo28/78ed98e2c01e20a1b6f23dc3d6716bce.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*MUn1-8Jg8AWF4ounzdPVfw.png) <br>
<span class="figcaption_hack">Figure 1: Dataset Head</span>

#### Log Transform

When using Log Transform, the distributions of the original features get
transformed to resemble more closely Gaussians Distributions. This can
particularly useful, especially when using Machine Learning models such as
Linear Discriminant Analysis (LDA) and Naive Bayes Classifiers which assume
their input data follows a Gaussian Distribution.

In this example, I am going to apply Log Transform to all the Numeric Features
available in the dataset. I additionally decided to subtract the original
features with their respective minimum values and then add them to one, in order
to make sure each element in these columns is positive (Logarithms just support
positive values).

<script src="https://gist.github.com/pierpaolo28/d8c75ed75bd31f74025090c9bcda3687.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*j8LVuDLzk70Ss003dwIuRg.png) <br>
<span class="figcaption_hack">Figure 2: Logarithmically Transformed Dataset</span>

#### Imputation

Imputation is the art of identifying and replacing missing values from a dataset
using appropriate values. Presence of missing values in a dataset can be caused
by many possible factors such as: privacy concerns, technical faults when
recording data using sensors, humans errors, etc…

There are two main types of Imputation:

* **Numerical Imputation**: missing numbers in numerical features can be imputed
using many different techniques. Some of the main methods used, are to replace
missing values with the overall mean or mode of the affected column. If you are
interested in learning more about advanced techniques, you can find more
information
[here](https://towardsdatascience.com/why-using-a-mean-for-missing-data-is-a-bad-idea-alternative-imputation-algorithms-837c731c1008).
* **Categorical Imputation**: for categorical features, missing values are
commonly replaced using the overall column mode. In some particular case, if the
categorical column structure is not well defined, it might be better instead to
replace the missing values creating a new category and naming it “Unknown” or
“Other”.

We can now, first of all, examine which features are affected by NaNs (Not a
Number) by running the following few lines.

<script src="https://gist.github.com/pierpaolo28/f6d83bb7c092a6b55bbc19592122fc1c.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*qDUYyoU3JgYg6_bJuPCSlQ.png) <br>
<span class="figcaption_hack">Figure 3: Percentage of NaNs in each Feature</span>

One of the easiest methods to deal with Missing Numbers could be to remove all
the rows affected by them. Although, it would better to set up a threshold (eg.
20%), and delete just the rows which have more missing numbers than the
threshold.

<script src="https://gist.github.com/pierpaolo28/079a79a3172ccb377fc76dd8016f4160.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*hFpdFcdFux5v8vk3SJzzHQ.png) <br>
<span class="figcaption_hack">Figure 4: Imputation by deleting features with excessive NaNs</span>

Another possible solution could be to replace all the NaNs with the column mode
for both our numerical and categorical data.

<script src="https://gist.github.com/pierpaolo28/6854d70281adf1f03a8b8c8bdee411bc.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*gxze2yfVe6n_vWEHZ-yh9g.png) <br>
<span class="figcaption_hack">Figure 5: Imputation using column mode</span>

#### Dealing With Dates

[Date Objects](https://www.w3schools.com/python/python_datetime.asp) can be
quite difficult to deal with for Machine Learning models because of their
format. It can, therefore, be necessary at times to divide a date into multiple
columns. This same consideration can be applied to many other common cases in
Data Analysis (eg. Natural Language Processing).

In our example, we are now going to divide our Date column into three different
columns: Year, Month and Day.

<script src="https://gist.github.com/pierpaolo28/43fdb1217b494d9f6cf0c81657ccf1d3.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*xng97NxC5Hx5C7BliwDbqQ.png) <br>
<span class="figcaption_hack">Figure 6: Dealing with Dates</span>

#### Outliers

Outliers are a small fraction of data points which are quite distant from the
rest of the observations in a feature. Outliers can be introduced in a dataset
mainly because of errors when collecting the data or because of special
anomalies which are characteristic of our specific feature.

Four main techniques are used in order to identify outliers:

* **Data Visualization**: determining outlier values by visually inspecting the
data distribution.
* **Z-Score**: is used if we know that the distribution of our features is
Gaussian. In fact, when working with Gaussian distributions, we know that about
2 standard deviations from the distribution mean about 95% of the data will be
covered and 3 standard distributions away from the mean will cover instead about
99.7% of the data. Therefore, using a factor value between 2 and 3 we can be
able to quite accurately delete all the outlier values. If you are interested in
finding out more about Gaussian Distributions, you can find more information
[here](https://towardsdatascience.com/probability-distributions-in-data-science-cce6e64873a7).
* **Percentiles**: is another statistical method for identifying outliers. When
using percentiles, we assume that a certain top and bottom percent of our data
are outliers. The key point when using this method is to find the best
percentage values. One useful approach could be to visualize the data before and
after applying the percentile method to examine the overall results.
* **Capping**: instead of deleting the outlier values, we replace them with the
highest normal value in our column.

Other more advanced techniques commonly used to detect outliers are
[DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) and [Isolation
Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html).

Going on with our example, we can start by looking at our two left numerical
features (X2, X3). By creating a simple BoxPlot using Seaborn, we can clearly
see that X2 has some outlier values.

![](https://cdn-images-1.medium.com/max/2000/1*Fv6VXKdn9O_sxtWujVBNGA.png) <br>
<span class="figcaption_hack">Figure 7: Examining Outliers using Data Visualization</span>

Using both the Z-score (with a factor of 2) and the Percentiles methods, we can
now test how many outliers will be identified in X2. As shown from the output
box below, 234 values were identified using the Z Score, while using the
Percentiles method 800 values were deleted.

<script src="https://gist.github.com/pierpaolo28/bfd164bbc86cf23c0b459a18241f42e5.js"></script>

    8000
    7766
    7200

It could have additionally been possible to deal with our Outliers by capping
them instead of dropping them.

#### Binning

Binning is a common technique used to smooth noisy data, by diving a numerical
or categorical feature in different bins. This can, therefore, help us to
decrease the risk of overfitting (although possibly reducing our model
accuracy).

<script src="https://gist.github.com/pierpaolo28/1115040e473c3c71362659860568a1fe.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*NSkqxTCr7EHFO4PnLyImDw.png) <br>
<span class="figcaption_hack">Figure 8: Binning Numeric and Categoric Data</span>

#### Categorical Data Encoding

Most of Machine Learning models are currently not able to deal with Categorical
Data, therefore it is usually necessary to convert all categorical features to
numeric before feeding them into Machine Learning models.

Different techniques can be implemented in Python such as: One Hot Encoding (to
convert features) and Label Encoder (to convert labels).

One Hot Encoding takes a feature and split it in as many columns as the number
of the different categories present in the original column. It then assigns a
zero to all the rows which didn’t have that particular category and one for all
the ones which instead had it. One Hot Encoding can be implemented in Python
using Pandas **get_dummies()** function.

Label Encoder replaces instead all the categorical cases by assigning them a
different number and storing them in a single column.

It is highly preferable not to use Label Encoder with normal features because
some Machine Learning models might get confused and think that the encoded cases
which have higher values than the other ones might be more important of them
(thinking about them as in hierarchical order). This doesn’t instead happen when
using One Hot Encoding.

![](https://cdn-images-1.medium.com/max/2600/1*ezGOW_jDDvZ9jCjHTj7hLg.jpeg) <br>
<span class="figcaption_hack">Figure 9: Difference between One Hot Encoding and Label Encoding [1]</span>

We can now go on dividing our dataset into features (**X**) and labels (**Y**)
and then applying respectively One Hot Encoding and Label Encoder.

<script src="https://gist.github.com/pierpaolo28/b79dabbc0587aea7fef433189ce4ecf3.js"></script>

#### Scaling

In most of the datasets, numerical features have all different ranges (eg.
Height vs Weight). Although, it can be important for Machine Learning algorithms
to limit within a defined range our input features. In fact, for some
distance-based models such as Naive Bayes, [Support Vector
Machines](https://towardsdatascience.com/svm-feature-selection-and-kernels-840781cc1a6c)
and Clustering Algorithms, it would then be almost impossible to compare
different features if they all have different ranges.

Two common ways of scaling features are:

* **Standardization:** scales the input features while taking into account their
standard deviation (using Standardization our transformed features will look
similar to a Normal Distribution). This method can reduce outliers importance
but can lead to different ranges between features because of differences in the
standard deviation. Standardization can be implemented in scikit-learn by using
[StandardScaler()](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html).
* **Normalization:** scales all the features in a range between 0 and 1 but can
increase the effect of outliers because the standard deviation of each of the
different features is not taken into account. Normalization can be implemented
in scikit-learn by using
[MinMaxScaler()](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler).

In this example, we will be using Standardization and we will then take care of
our Outlier Values. If the dataset you are working with does not extensively
suffer from Outlier Values, scikit-learn provides also another Standardization
function called
[RobustScaler()](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
which can by default reduce the effect of outliers.

<script src="https://gist.github.com/pierpaolo28/f746f3b70db5cb5462f7b2d7dd04bc44.js"></script>

#### Automated Feature Engineering

Different techniques and packages have been developed during the last few years
in order to automate Feature Engineering processes. These can certainly result
useful when performing a first analysis of our dataset but they are still not
able to automate in full the whole Feature Engineering process. Domain Knowledge
about the data and expertise of the Data Scientist in modelling the raw data to
best fit the analysis purpose can’t yet be replaceable. One of the most popular
library for Automated Feature Selection in Python is
[Featuretools](https://docs.featuretools.com/#).

### Conclusion

It’s now time to finally to test our polished dataset prediction accuracy by
using a Random Forest Classifier. As shown below, our classifier is now
successfully able to achieve a 100% prediction accuracy.

<script src="https://gist.github.com/pierpaolo28/79c96639ed06bc3b662d38af9164916a.js"></script>

    1.40625
    [[1204    0]
     [   0 1196]]
                  precision    recall  f1-score   support
               0       1.00      1.00      1.00      1204
               1       1.00      1.00      1.00      1196
       micro avg       1.00      1.00      1.00      2400
       macro avg       1.00      1.00      1.00      2400
    weighted avg       1.00      1.00      1.00      2400

*****

*I hope you enjoyed this article, thank you for reading!*

### Bibliography

[1] What is One Hot Encoding and How to Do It. Michael DelSole, Medium. Accessed
at:
[https://medium.com/@michaeldelsole/what-is-one-hot-encoding-and-how-to-do-it-f0ae272f1179](https://medium.com/@michaeldelsole/what-is-one-hot-encoding-and-how-to-do-it-f0ae272f1179)
