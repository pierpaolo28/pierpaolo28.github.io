---
layout: post_body
date: 2020-06-07
title: Online Variational Autoencoder (VAE)
tags: [Machine Learning]
featured-img: manifold
img-type: gif
permalink: Projects/ONNX/home.html
github: https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Online%20Learning/ONNX
---

Online VAE trained on 3 different versions of the MNIST dataset (Standard, Rotated, Rotated and Translated) and deployed using ONNX. Currently this model is supported just on desktop devices (no touchscreen input allowed).

<link rel="stylesheet" href="style.css" />

<div class="main_body">
  <div class="card elevation" style="height: 318px; width: 250px;">
    <h3 style="text-align: center;">
      Choose your preferred model
    </h3>
    <div
      class="button"
      id="model1"
      style="text-align: center; width: 215px;"
    >
      MNIST
    </div>
    <div
      class="button"
      id="model2"
      style="text-align: center; width: 215px;"
    >
      MNIST ROTATED
    </div>
    <div
      class="button"
      id="model3"
      style="text-align: center; width: 215px;"
    >
      MNIST ROTATED AND TRANSLATED
    </div>
  </div>
  <div class="card elevation">
    <canvas
      class="canvas elevation"
      id="canvas"
      width="280"
      height="280"
    ></canvas>

    <div class="button" id="clear-button" style="margin: 0 auto;">
      CLEAR
    </div>
  </div>
  <div class="card elevation">
    <canvas class="canvas elevation" id="canvas2" width="28" height="28">
    </canvas>

    <div class="button" id="save-button" style="margin: 0 auto;">SAVE</div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/onnxjs/dist/onnx.min.js"></script>
<script src="script.js"></script>
