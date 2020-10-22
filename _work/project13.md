---
layout: post_book
date: 2019-09-22
title: Plotly.js End to end online Data Visualization
tags: [Data Science]
featured-img: plotly
img-type: jpg
github: https://github.com/pierpaolo28/Data-Visualization/tree/master/Javascript%20Visualization%20Libraries
---

The dataset used is for this example is the "Wine Data Set" dataset.
The features contained in this dataset are:
1. Fixed acidity
2. Volatile acidity
3. Citric acid
4. Residual sugar
5. Chlorides
6. Free sulfur dioxide
7. Total sulfur dioxide
8. Density
9. PH
10. Sulphates
11. Alcohol
12. Quality
And the label column (called style) identifies if a certain wine is white (1) or red (0). This dataset is available to download [at this link.](https://www.kaggle.com/sgus1318/winedata)

The graphs below have been realised right now in real time. Using the Plotly.js library, a javascript file is retrieving the Wine Dataset from an URL online and is then creating all the plots shown below right when this page is loading.


<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
<!-- Plotly.js -->
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<div id="myDiv" style="text-align:center"></div>

<script>
  function makeplot() {
    Plotly.d3.csv(
      "https://raw.githubusercontent.com/pierpaolo28/Artificial-Intelligence-Projects/master/Google%20AI%20tools/tensorflow.js/wine_data.csv",
      function(data) {
        processData(data);
      }
    );
  }

  function processData(allRows) {
    var fixed_acidity = [],
      volatile_acidity = [],
      citric_acid = [];
    residual_sugar = [];
    chlorides = [];
    free_sulfur_dioxide = [];
    total_sulfur_dioxide = [];
    density = [];
    sulphates = [];
    alcohol = [];
    pH = [];
    quality = [];
    style = [];

    for (var i = 0; i < allRows.length; i++) {
      row = allRows[i];
      fixed_acidity.push(row["fixed_acidity"]);
      volatile_acidity.push(row["volatile_acidity"]);
      citric_acid.push(row["citric_acid"]);
      residual_sugar.push(row["residual_sugar"]);
      chlorides.push(row["chlorides"]);
      free_sulfur_dioxide.push(row["free_sulfur_dioxide"]);
      total_sulfur_dioxide.push(row["total_sulfur_dioxide"]);
      density.push(row["density"]);
      sulphates.push(row["sulphates"]);
      alcohol.push(row["alcohol"]);
      pH.push(row["pH"]);
      quality.push(row["quality"]);
      style.push(row["style"]);
    }
    makePlotly(
      fixed_acidity,
      volatile_acidity,
      free_sulfur_dioxide,
      total_sulfur_dioxide,
      density,
      alcohol,
      quality,
      style
    );
  }

  function makePlotly(x, y, x2, y2, x3, x4, y34, label) {
    var plotDiv = document.getElementById("plot");
    var trace1 = {
      x: x,
      y: y,
      mode: "markers",
      type: "scatter",
      name: "Fixed Acidity vs Volatile Acidity"
    };

    var trace2 = {
      x: x2,
      y: y2,
      mode: "markers",
      type: "scatter",
      xaxis: "x2",
      yaxis: "y2",
      name: "Free Sulfur Dioxide vs Total Sulfur Dioxide"
    };

    var trace3 = {
      x: x3,
      y: y34,
      mode: "markers",
      type: "scatter",
      xaxis: "x3",
      yaxis: "y3",
      name: "Density vs Quality"
    };

    var trace4 = {
      x: x4,
      y: y34,
      mode: "markers",
      type: "scatter",
      xaxis: "x4",
      yaxis: "y4",
      name: "Alcohol vs Quality"
    };

    var trace5 = {
      x: x,
      type: "histogram",
      xaxis: "x5",
      yaxis: "y5",
      name: "Fixed Acidity Distribution"
    };

    var trace6 = {
      x: y34,
      type: "histogram",
      xaxis: "x6",
      yaxis: "y6",
      name: "Quality Distribution"
    };

    var trace7 = {
      x: x3,
      type: "histogram",
      xaxis: "x7",
      yaxis: "y7",
      name: "Density Distribution"
    };

    var trace8 = {
      x: label,
      type: "histogram",
      xaxis: "x8",
      yaxis: "y8",
      name: "Wine Style (Labels) Disrtibution"
    };

    var layout = {
      grid: { rows: 4, columns: 2, pattern: "independent" },
      autosize: false,
      width: 800,
      height: 800,
      yaxis: { title: "Volatile Acidity" },
      yaxis2: { title: "Total Sulfur Dioxide" },
      yaxis3: { title: "Quality" },
      yaxis4: { title: "Quality" },
      xaxis: { title: "Fixed Acidity" },
      xaxis2: { title: "Free Sulfur Dioxide" },
      xaxis3: { title: "Density" },
      xaxis4: { title: "Alcohol" },
      xaxis5: { title: "Fixed Acidity Distribution" },
      xaxis6: { title: "Quality Distribution" },
      xaxis7: { title: "Density Disrtibution" },
      xaxis8: { title: "Wine Style (Labels) Disrtibution" }
    };

    data = [
      trace1,
      trace2,
      trace3,
      trace4,
      trace5,
      trace6,
      trace7,
      trace8
    ];

    Plotly.newPlot("myDiv", data, layout);
  }

  makeplot();
</script>
