---
layout: post
permalink: blog/blog70/
categories: [Data Science]
---

![](https://miro.medium.com/max/1400/0*u8VdVhpcf4NqDvgR)Photo by [Jason Coudriet](https://unsplash.com/@jcoudriet?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

Embedding Interactive Python Plots on the Web
=============================================

A guide on how to use Plotly Chart Studio and Datapane to share Python plots on the web
---------------------------------------------------------------------------------------

Introduction
============

One of the most important steps in the Data Science pipeline is Data Visualization.

 In fact, thanks to Data Visualization, Data Scientists can be able to quickly gather insights about the data they have available and any possible anomaly.

Traditionally, Data Visualization consisted of creating static images and summary statistics which could then be exported as images (e.g. PNG, JPG, SVG) using Python and libraries such as Matplotlib. Although, thanks to the development of libraries such as Plotly, Bokeh or Altair it is now possible to create much more [interactive visualizations](/interactive-data-visualization-167ae26016e8) and even [online dashboards](/interactive-dashboards-for-data-science-51aa038279e5) which can be shared with colleagues and shareholders.

Once finished working on a project, there are typically two different approaches that you can use to share your visualizations and results with any interested party:

* Creating some form of [data-driven presentation](/creating-online-data-driven-presentations-6b25fc626072).
* Creating a project summary internal webpage with embedded any interactive plots created.

In this article we are now going to explore this second approach, presenting two possible solutions: **Plotly Chart Studio** and **Datapane**. All the code used for this article, is publicly available on my GitHub account at [this link](https://github.com/pierpaolo28/Data-Visualization/blob/master/Online%20Python%20Embeds/online-python-plots.ipynb).

Plotly Chart Studio
===================

[Plotly](https://github.com/plotly) is an open-source Python library built on plotly.js. Using Plotly, you can be able to create interactive graphs and dashboards using programming languages such as Python, R, Julia and Javascript.

In order to create easily sharable graphs, Plotly provides a [chart studio service](https://chart-studio.plotly.com/create/#/). Using this service, you can either create a plot as usual by programming and then add it to your online collection, or you can upload your data through the online user interface and create your graphs from there (without any need to code at all). Some examples of plots created using Plotly Chart Studio, are available at [this link.](https://chart-studio.plotly.com/feed/#/)

For this example, we are going to use the programming option using Python and the freely available [Kaggle Students Performance in Exams dataset](https://www.kaggle.com/datasets/satwikverma/students-performance-in-exams) [1]. In case you are interested in exploring also the user interface to create your graphs, Plotly provides a list of guided tutorials available at [this link.](https://plotly.com/chart-studio-help/tutorials/)

In order to get started with Plotly Chart Studio, we need first to [create an account](https://chart-studio.plotly.com/Auth/login/?action=signin#/) and then install the Python library using the following command:


```
pip install chart_studio
```
At this point, we need to save our account API key, so that to be able to share graphs created using Python into our online account. This can be found by logging in to your account, going to *Settings* and then *API Keys*. We are now ready to start our data exploratory analysis.

Data Visualization
------------------

First of all, we need to import all the necessary dependencies and inspect the head of the [Students Performance in Exams dataset](https://www.kaggle.com/datasets/satwikverma/students-performance-in-exams) (Figure 1).

<script src="https://gist.github.com/pierpaolo28/681655156601176c8b4d16284702fd9f.js"></script>

![](https://miro.medium.com/max/1400/1*u6I-s5zC2B9X9U64A_7wWA.png)
Figure 1: Students Performance in Exams dataset (Image by Author).

Using the following code snippet, we can then create a 3D scatterplot and save it to our online collection as ***3d\_embed\_ex*** (remember to add your Plotly Chart Studio username and the API Key you copied before from your account settings).

<script src="https://gist.github.com/pierpaolo28/751fcc98771764535054b323cff6ff5f.js"></script>

Going to your Plotly Chart Studio account and your *My Files* section, you should then be able to see the graph you just created in Python. Clicking on *Share* and then on the *Embed* tab, you would then be able to see the ***iframe*** and ***HTML*** code you can use to share your interactive plot anywhere on the web (as shown in Figure 2 below).

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~pierpaolo28/83.embed"></iframe>
Figure 2: 3D Scatterplot Plotly Chart Studio Embed (Image by Author).

Datapane
========

[Datapane](https://github.com/datapane/datapane) is a Python library designed in order to make it easier to share any form of data analysis through web embeds, automatically generated HTML files and much more. One of the main advantages of using Datapane, is its support to many data visualization libraries such as: *matplotlib*, *plotly*, *bokeh*, *pandas* and many more. Additionally, using Datapane, it is also possible to share, not just individual plots but also collections of plots and *Latex/Markdown* text.

In order to get started with Datapane, we need first to [create a free account](https://datapane.com/accounts/signup/) and get our API key in the same way we did with Plotly Chart Studio. The Python library can then be installed using the following command:

```
pip install datapane
```

Data Visualization
------------------

In order to provide a demonstration of how Datapane can be used, the [Students Performance in Exams dataset](https://www.kaggle.com/datasets/satwikverma/students-performance-in-exams) (shown in Figure 1), is going to be used again. Using then the following code snippet, a Datapane embed can be created (remember to add you Datapane API Key you copied before from your account settings). Additionally, using the ***save*** option, it can also be possible to create an HTML file version of your report which you could then share with anyone you want without having to make your report publicly available on the web.

<script src="https://gist.github.com/pierpaolo28/caf8525d668085c2245ac2a3a6dca05b.js"></script>

In order to share your newly created report, you can then just go to your Datapane account, click on *My Reports*, select the report you are interested in and click on *Share* (Figure 3).

<iframe src="https://datapane.com/reports/vAqxz2k/3d-embed-ex2/embed/" width="100%" height="540px" style="border: none;">IFrame not supported</iframe>
Figure 3: 3D Scatterplot Datapane Embed (Image by Author).

More complicated reports could then be created by adding more pages and visualizations (Figure 4). In the following example, a two pages report is created: one to show the first five rows of the dataset and one to show instead a 3D Scatter plot.

<script src="https://gist.github.com/pierpaolo28/12db2a433e856de7501dc4d45966865e.js"></script>

<iframe src="https://datapane.com/reports/wAwZRDk/3d-embed-ex3/embed/" width="100%" height="540px" style="border: none;">IFrame not supported</iframe>
Figure 4: 2 Pages Datapane Embed (Image by Author).

Conclusion
==========

In this article, we explored Plotly Chart Studio and Datapane as two possible options to embed interactive charts on the web. Creating interactive charts can also be useful not just for preparing and exploring data but also to create visualizations and interfaces about Machine Learning models. Two of the most common libraries used for these kinds of tasks are Streamlit and [Gradio.](/gradio-graphical-interfaces-for-machine-learning-models-fd4880964f8f) Additional information about this topic, is available in my [“Machine Learning Visualization” article](/machine-learning-visualization-fcc39a1e376a).


Bibliography
============

[1] “Student’s Performance in exams” (SATWIK VERMA, License [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)). Accessed at: <https://www.kaggle.com/datasets/satwikverma/students-performance-in-exams>
