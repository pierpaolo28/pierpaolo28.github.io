---
layout: post
permalink: blog/blog23/
categories: [Data Science]
---

![](https://cdn-images-1.medium.com/max/2000/1*TX77o_zJ4zbpJ3vN4BkLsg.jpeg)
<span class="figcaption_hack">(Source:
[https://hackernoon.com/5-free-r-programming-courses-for-data-scientists-and-ml-programmers-5732cb9e10](https://hackernoon.com/5-free-r-programming-courses-for-data-scientists-and-ml-programmers-5732cb9e10))</span>

# Getting started with R Programming

## An end to end Data Analysis using R, the second most requested programming language in Data Science.

### Introduction

R is a programming language focused on statistical and graphical analysis. It is
therefore commonly used in statistical inference, data analysis and Machine
Learning. R is currently one of the most requested programming language in the
Data Science job market (Figure 1).

![](https://cdn-images-1.medium.com/max/2000/1*lsI8O_2yGfYoUpCT6kNynw.png) <br>
<span class="figcaption_hack">Figure 1: Most Requested programming languages for Data Science in 2019 [1]</span>

R is available to be installed from [r-project.org](http://www.r-project.org/)
and one of R most commonly used integrated development environment (IDE) is
certainly [RStudio](http://www.rstudio.com/ide/).

There are two main types of packages (libraries) which can be used to add
functionalities to R: base packages and distributed packages. Base packages come
with the installation of R, distributed packages can instead be downloaded for
free using
[CRAN](https://cran.r-project.org/web/packages/available_packages_by_date.html).

Once installed R we can then get started doing some data analysis!

### Demonstration

In this example, I will walk you through an end to end analysis of the [Mobile
Price Classification
Dataset](https://www.kaggle.com/iabhishekofficial/mobile-price-classification#train.csv)
to predict the price range of Mobile Phones. The code I used for this
demonstration is available on both my
[GitHub](https://github.com/pierpaolo28/R-Programming/blob/master/Smartphone%20Prices/workflow.r)
and
[Kaggle](https://www.kaggle.com/pierpaolo28/mobile-price-classification?scriptVersionId=20002929)
account.

#### Importing Libraries

First of all, we need to import all the necessary libraries.

Packages can be installed in R using the **install.packages()** command and then
loaded using the **library()** command. In this case, I decided to install first
PACMAN (Package Management Tool) and then use it to install and load all the
other packages. PACMAN makes loading library easier because it can install and
load all the necessary libraries in just one line of code.

<script src="https://gist.github.com/pierpaolo28/9d70a5451988d9a330b77254c064f2ec.js"></script>

The imported packages are used to add the following functionalities:

* **dplyr:** data processing and analysis.
* **ggplot2:** data visualization.
* **rio:** data import and export.
* **gridExtra:** to make plots graphical objects to which can be freely arranged on a page.
* **scales:** used to scale data in plots.
* **ggcorrplot:** is used to visualize correlation matrices using ggplot2 in the backend.
* **caret:** is used to train and plot classification and regression models.
* **e1071:** contains functions to perform Machine Learning algorithms such as Support Vector Machines, Naive Bayes, etc…

#### Data Pre-processing

We can now go on loading our dataset, displaying it’s first 5 columns (Figure 2)
and print a summary of the main characteristics of each feature (Figure 3). In
R, we can create new objects using the **<-** operator.

<script src="https://gist.github.com/pierpaolo28/65f657ea6d7065203efbe8cd16b5c563.js"></script>

![](https://cdn-images-1.medium.com/max/2600/1*RzDAdwpOXq7ORvz1crltzg.png) <br>
<span class="figcaption_hack">Figure 2: Dataset Head</span>

The summary function provides us with a brief statistical description of each
feature in our dataset. Depending on the nature of the feature in consideration,
different statistics will be provided:

* **Numeric Features:** Mean, Median, Mode, Range and Quartiles.
* **Factor Features:** Frequencies.
* **A mixture of Factor and Numeric Features:** Number of missing values.
* **Character Features:** Lenght of the class.

Factors are a type of data object used in R to categorize and store data (eg.
integers or strings) as levels. They can, for example, be used to one hot encode
a feature or to create Bar Charts (as we will see later on). Therefore they are
especially useful when working with columns with few unique values.

![](https://cdn-images-1.medium.com/max/2000/1*T-bvpDXlP_1u4Cjl719Hfg.png) <br>
<span class="figcaption_hack">Figure 3: Dataset Summary</span>

Finally, we can now check if our Dataset contains any Not A Numbers (NaNs) value
using the code shown below.

<script src="https://gist.github.com/pierpaolo28/003d1173ab6c27b3f20c796a9e875e7f.js"></script>

As we can see from Figure 4, no missing numbers have been found.

![](https://cdn-images-1.medium.com/max/2000/1*dLrXdkrfZCsRQ8vVskgJYQ.png) <br>
<span class="figcaption_hack">Figure 4: Percentage of NaNs in each feature</span>

#### Data Visualization

We can now start our Data Visualization by plotting a Correlation Matrix of our
dataset (Figure 5).

<script src="https://gist.github.com/pierpaolo28/dafb5a92a3f893d9c9105e0a85c552e6.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*hTwUWOHz4Aqw5CQ-eAjHBg.png) <br>
<span class="figcaption_hack">Figure 5: Correlation Matrix</span>

Successively, we can start analysing individual features using Bar and Box
plots. Before creating these plots, we need though to first convert the
considered features from Numeric to Factor (this allow us to bin our data and
then plot the binned data).

<script src="https://gist.github.com/pierpaolo28/0286daa120bf6f83aa10819d6b048506.js"></script>

We can now create 3 Bar Plots by storing them in there different variables (p1,
p2, p3) and then add them to **grid.arrange()** to create a subplot. In this
case, I decided to examine the Bluetooth, Dual Sim and 4G features. As we can
see from Figure 6, a slight majority of mobiles considered in this Dataset does
not support Bluetooth, is Dual Sim and has 4G support.

<script src="https://gist.github.com/pierpaolo28/bdec9c3bce257040da18eb6c224437ce.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*15BiE6Sl6xI10xgO0F6HZg.png) <br>
<span class="figcaption_hack">Figure 6: Bar Plot Analysis</span>

These plots have been created using R **ggplot2** library. When calling the
**ggplot()** function, we create a coordinate system on which we can add layers
on top of it [2].

The first argument we give to the **ggplot()** function is the dataset we are
going to use and the second one is instead an aesthetic function in which we
define the variables we want to plot. We can then go on adding other additional
arguments such us defining a desired geometric function (eg. barplot, scatter,
boxplot, histogram, etc…), adding a plot theme, axis limits, labels, etc…

Taking our analysis a step further, we can now calculate the precise percentages
of the difference between the different cases using the **prop.table()**
function. As we can see from the resulting output (Figure 7), 50.5% of the
considered mobile devices do not support Bluetooth, 50.9% is Dual Sim and 52.1%
has 4G.

<script src="https://gist.github.com/pierpaolo28/9c23c05b3623c012a8055a1104874630.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*ecc1dSMUIcruaGc_Ah-poQ.png) <br>
<span class="figcaption_hack">Figure 7: Classes Distribution Percentage</span>

We can now go on creating 3 different Box Plots using the same technique used
before. In this case, I decided to examine how having more battery power, phone
weight and RAM (Random Access Memory) can affect mobiles prices. In this
Dataset, we are not given the actual phone prices but a price range indicating
how high the price is (four different levels from 0 to 3).

<script src="https://gist.github.com/pierpaolo28/d03e76c61041adf5418afaf935e9b723.js"></script>

The results are summarised in Figure 8. Increasing Battery Power and RAM
consistently lead to an increase in Price. Instead, more expensive phones seem
to be overall more lightweight. In the RAM vs Price Range plot have
interestingly been registred some outliers values in the overall distribution.

![](https://cdn-images-1.medium.com/max/2000/1*CTX61Y3K4UG7_lKBLedwdg.png) <br>
<span class="figcaption_hack">Figure 8: Box Plot Analysis</span>

Finally, we are now going to examine the distribution of camera quality in
Megapixels for both the Front and Primary cameras (Figure 9). Interestingly, the
Front camera distribution seems to follow an exponentially decaying distribution
while the Primary camera roughly follows a uniform distribution. If you are
interested in finding out more about Probability Distributions, you can find
more information
[here](https://towardsdatascience.com/probability-distributions-in-data-science-cce6e64873a7).

<script src="https://gist.github.com/pierpaolo28/5fe61123a7fdd056c38afba7038f4811.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*g5gfU-x3F200_OltYlDDQg.png) <br>
<span class="figcaption_hack">Figure 9: Histogram Analysis</span>

#### Machine Learning

In order to perform our Machine Learning analysis, we need first to convert our
Factor variables in Numeric form and then divide our dataset into train and test
sets (75:25 ratios). Lastly, we divide the train and test sets into features and
labels (**price_range**).

<script src="https://gist.github.com/pierpaolo28/ee565c5f08a1a660b53dbecf3af0f6d6.js"></script>

It’s now time to train our Machine Learning model. In this example, I decided to
use [Support Vector Machines
(SVM)](https://towardsdatascience.com/svm-feature-selection-and-kernels-840781cc1a6c)
as our multiclass classifier. Using R **summary()** we can then inspect the
parameters of our trained model (Figure 10).

<script src="https://gist.github.com/pierpaolo28/5d4a393b8bdf1d55bafffc66daae8039.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*GDrVoWCUEQ__UHBqiEKquA.png) <br>
<span class="figcaption_hack">Figure 10: Machine Learning Model Summary</span>

Finally, we can now test our model making some predictions on the test set.
Using R **confusionMatrix()** function we can then get a complete report of our
model accuracy (Figure 11). In this case, an Accuracy of 96.6% was registered.

<script src="https://gist.github.com/pierpaolo28/f6ec3f283ffd770ce387fba2282489ef.js"></script>

![](https://cdn-images-1.medium.com/max/2000/1*mzj3sdAtFO9AcVs3uOBdqQ.png) <br>
<span class="figcaption_hack">Figure 11: Model Accuracy Report</span>

*****

*I hope you enjoyed this article, thank you for reading!*

### Bibliography

[1] Which languages are important for Data Scientists in 2019? Quora. Accessed
at:
[https://www.quora.com/Which-languages-are-important-for-Data-Scientists-in-2019](https://www.quora.com/Which-languages-are-important-for-Data-Scientists-in-2019)

[2] R for Data Science, Garrett Grolemund and Hadley Wickham.  Accessed at:
[https://www.bioinform.io/site/wp-content/uploads/2018/09/RDataScience.pdf](https://www.bioinform.io/site/wp-content/uploads/2018/09/RDataScience.pdf)
