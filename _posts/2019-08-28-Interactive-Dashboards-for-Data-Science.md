---
layout: post
permalink: blog/blog21/
categories: [Data Science, Deployment]
---

![](https://cdn-images-1.medium.com/max/1200/1*PnO6VgeNnVquirfLfZLdEA.gif)
[Facebook Data Analysis Dashboard](https://salty-tor-65518.herokuapp.com/)

<!--end_excerpt-->

# Interactive Dashboards for Data Science

## Creating an online dashboard in Python to analyse Facebook Stock Market Prices and Performance Metrics.


### Introduction

Creating an online Data Science Dashboard can be a really powerful way of communicating the results of a Data Science project. A good Dashboard can:

-   Summarise the main results of a data analysis.
-   Enable the customers/company managers to test how varying some parameters can affect a certain outcome.
-   Fetch continuously new data to update its graphs and summaries.
-   Allow us to make predictions online using either pre-trained Machine Learning models or training them online.

Nowadays, there are many different services which can be used to create Dashboards. Some examples are:

-   **Dash by Plotly**
-   **Bokeh Dashboards**
-   **Google Data Studio**
-   **Tableau**

The first two examples require a good Python programming knowledge in order to create Dashboards, instead, the last two don't necessarily require any programming knowledge (they provide although fewer customisation options).

![](https://cdn-images-1.medium.com/max/1200/1*DcCGgeWS21ASglctx9OfFQ.png)

Figure 1: [Titanic Data Set Dashboard made using Tableau.](https://github.com/pierpaolo28/Data-Visualization/tree/master/Tableau%20%26%20Google%20Data%20Studio)

In this article, I will walk you through how to create and deploy online a Dashboard using Plotly Dash. All the code used in this article (and more!) is available in on my [GitHub account](https://github.com/pierpaolo28/Data-Visualization/tree/master/Dash).

My final version of the Dashboard is available to be tested online at [this link.](https://salty-tor-65518.herokuapp.com/)

### Dash

![](https://cdn-images-1.medium.com/max/800/1*u7HD-JoDZcwKHM5P4dKU2Q.png)

Figure 2: Dash [1]

Dash is an Open Source Python library designed by Plotly for creating reactive, Web-based applications. This library is built on top of other packages such as: Flask, Plotly.js, React and React Js.

Every Dash App is composed of two main parts:

-   **Layout** = is used to define how all the content should be laid out on the application.
-   **Callbacks** = are used to make each of the desired components of the Dashboard interactive.

Additionally, Dash provides a collection of HTML classes to generate HTML code in Python (***dash-html-components***), Markdown and App Authentication support.

All the necessary libraries needed to get started with Dash are listed below.

    pip install dash
    pip install dash-renderer
    pip install dash-html-components
    pip install dash-core-components
    pip install plotly

In order to create the following dashboard, I made use of two different datasets. The first one is the [Huge Stock Market Dataset by Boris Marjanovic](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs) and the second one is the [Facebook metrics Data Set by Moro, S., Rita, P., & Vala, B](https://archive.ics.uci.edu/ml/datasets/Facebook+metrics).

Before loading the first dataset on the dashboard application, I performed some pre-processing analysis, the resulting dataset is available [here.](https://raw.githubusercontent.com/pierpaolo28/Data-Visualization/master/Dash/stock_data.csv)

In this demonstration, we will create together a Dashboard composed of two tabs. The first tab will show the High, Low and Volume Stock market indicators of companies such as Facebook, Apple, Microsoft and Tesla. The second tab will instead show the distributions of each of the features available in the Facebook Performance Metrics dataset (Figure 3).

![](https://cdn-images-1.medium.com/max/1200/1*Q5SO4evwH8s63cBgC7Pn4g.gif)

Figure 3: Final Dashboard which we will create in this tutorial

If you are interested in adding more features to this App, on [my GitHub repository](https://github.com/pierpaolo28/Data-Visualization/tree/master/Dash) is available a more advanced version.

### Demonstration

First of all, we need to create a Python file called **a*pp.py*** and import all the required dependencies. In this file, we will write all the code necessary to launch our Dashboard.

<script src="https://gist.github.com/pierpaolo28/55fef8332fad2e3630d0f3e112babc73.js"></script>

The datasets we are going to work with will have a structure like shown in Figure 4 and 5.

![](https://cdn-images-1.medium.com/max/800/1*I2MJa0z0YXPehn2w7DC00A.png)

Figure 4: Stock Dataset

![](https://cdn-images-1.medium.com/max/2560/1*MgVW5ekvk1ZXAea_V63hug.png)

Figure 5: Performance Metrics Dataset

We can then set-up our App and its layout using the code shown below. The layout is stored in ***app.layout***, and all the desired HTML components such as Div, H1, H2, P, etc have been added using the ***dash_html_components*** ***(html)*** library. Finally, we can add interactive components to our dashboard (eg. tabs, dropdowns, radio buttons) using the ***dash_core_components (dcc)*** library.

In this case, I decided to divide this Dashboard into two tabs. In the first one, will be analysed the Stock Prices dataset and in the second one the Performance Metrics dataset. The layout of the first tab is subsequently divided into other two parts each of them formed by an H1 title, a dropdown menu with four different options and a time-series graph. The second tab is instead formed by just an H1 title, a dropdown menu with 18 different options and a histogram.

<script src="https://gist.github.com/pierpaolo28/0eb023e79e91c73035d1d83775cb7d04.js"></script>

Once defined the layout of our Dashboard, we can then go on and design the graphs and their interaction with the dropdown menus. The graphs can be designed creating functions and instead the interactions between the graphs and the dropdown menus can be designed using callbacks.

The code below can be divided in 3 main sections: a High-Low Stock Prices Time Series graph, a Market Volume Time Series graph and a Performance Metrics Feature Distributions graph.

The first two sections are really similar, in fact, they are designed to create the same type of graph. The only difference is that in the second graph just one feature is considered instead of two.

In each of the 3 sections, the callbacks (***@app.callback***) are used to take the selected values from the dropdowns, send them as input to the graph function and then take the variable returned by the function to pass it to the graph declared in the layout. These callbacks will automatically get called every-time the values in the dropdowns changes. The callbacks can automatically identify which of the different dropdowns available on the Dashboard changed value and which graph to subsequently update thanks to the unique ***id***   values set before in the Dashboard Layout.

Each of the three functions shown below use [Plotly syntax](https://plot.ly/python/) to create the graphs. If you have never used Plotly before, in one of my previous articles I have already talked about [Interactive Data Visualization](https://towardsdatascience.com/interactive-data-visualization-167ae26016e8).

<script src="https://gist.github.com/pierpaolo28/ce642cb1ac02cf63d0a4c9603565c243.js"></script>

The fist function will generate the graph shown below.

![](https://cdn-images-1.medium.com/max/800/1*6vRSM7mg5ZzXrl81WPw8Hw.png)

Figure 6: Facebook Stocks, High vs Lows

The second one will instead create the graph shown in Figure 7.

![](https://cdn-images-1.medium.com/max/800/1*bxsBT9l6D_KpxSCKFnL5Ng.png)

Figure 7: Facebook Market Volume

Lastly, the third function will generate the feature distribution histogram on the second tab of the Dashboard (Figure 8).

![](https://cdn-images-1.medium.com/max/800/1*Bse1AWFpOSp2dO9mapVzzg.png)

Figure 8: Facebook Metrics Distribution

Finally, we can start a local server and make our application run by using the following two lines of code.

<script src="https://gist.github.com/pierpaolo28/786e725643c6f00d1e5aee4a0bf408b9.js"></script>

Now that our app is ready, we can simply lunch it by opening our computer terminal in our current working directory and typing ***python app.py***. This will start a web server at <http://127.0.0.1:8050/>, going at this link we will see our final Python App running.

It is possible to easily deploy online Dash Apps for free hosting our application on Heroku. If you are interested in doing so, I wrote another article about [Flask and Heroku for online Machine Learning deployment](https://towardsdatascience.com/flask-and-heroku-for-online-machine-learning-deployment-425beb54a274). Additionally, also the Dash [documentation](https://dash.plot.ly/deployment) provides guidance on how to deploy Dash Apps on Heroku.

### Conclusion

This Dashboard can be further developed by adding additional features such as:

-   Use a web-scraping mechanism to fetch new Stock Market data in real-time to update all the related graphs.
-   Add more [Data Visualisation](https://towardsdatascience.com/interactive-data-visualization-167ae26016e8) charts.
-   Create Machine Learning models to make predictions (eg. [ARIMA](https://towardsdatascience.com/stock-market-analysis-using-arima-8731ded2447a), LSTM).
-   Improve the Dashboard overall design.

A more advanced version of this dashboard is available to be tested online at [this link.](https://salty-tor-65518.herokuapp.com/)

If you need any help to add any of these additional features, the [Dash documentation](https://dash.plot.ly/) is a great place where to start.

* * * * *

*I hope you enjoyed this article, thank you for reading!*

### Bibliography

[1] Dash operationalizes Python & R models at scale, Plotly. Accessed at: <https://plot.ly/dash>
