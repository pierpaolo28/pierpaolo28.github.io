---
layout: post_body
date: 2019-08-24
title: Introduction to ml5.js
tags: [Artificial Intelligence, Machine Learning]
featured-img: ml5
img-type: jpg
permalink: Projects/ml5.js/ml5intro.html
summary: PoseNet is a vision model that can be used to estimate the pose of a person in an image or video by estimating where key body joints are.
github: https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Google%20AI%20tools/ml5.js
---

<script
  src="https://unpkg.com/ml5@0.3.1/dist/ml5.min.js"
  type="text/javascript"
></script>

## PoseNet Example

PoseNet is a vision model that can be used to estimate the pose of a
person in an image or video by estimating where key body joints are. In
this example, I used Google ml5.js and p5.js to quickly deploy online the
pre-trained PoseNet model.

<div style="text-align: center;">
  <canvas id="canvas" width="640" height="480"></canvas>
  <video
    id="video"
    width="640"
    height="480"
    autoplay
    style="display: none;"
  ></video>
  <script src="sketch.js"></script>
</div>
