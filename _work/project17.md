---
layout: post_book
date: 2020-04-28
title: Linear/Extended Kalman and Particle Filters
tags: [Reinforcement Learning]
featured-img: bound
img-type: PNG
github: https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Online%20Learning
---

In this project, is avaialable a practical Demonstration of Linear/Extended Kalman and Particle
Filters in actions in order to solve first a regression and then a
classification problem.

## Third Order Autoregressive Time Series with constant parameters

In this section, a Linear Kalman filter is implemented in order
to estimate the coefficients (1.2, -0.4 and 0.1) of a synthetic third
order Autoregressive (AR) Process.

![](/assets/img/posts/ARprocess_stat3.svg)

Overall 1.137, -0.367 and 0.0562 have been the final estimated
parameters using the Linear Kalman Filter.

![](/assets/img/posts/tree_par.svg)

## Autoregressive Time Series with slowly changing parameters

![](/assets/img/posts/ARprocess.svg)

In the following video, is shown how a Particle Filter Algorithm with
Resampling can be used in order to reliably estimate the
Autoregressive Time Series coefficients values (in this case X=1.4 and
Y=-0.7).

<video class="center" controls>
  <source
    src="/assets/img/posts/Alg2_anim.mp4"
    type="video/mp4"
  />
  Your browser does not support the video tag.
</video>

An analogous representation, showing how the algorithm converges
towards the actual coefficient values, is shown below.

![](/assets/img/posts/Alg2_parameter_est.svg)


## Binary classification using Extended Kalman Filter and Logistic Regression

In this example, has been used some syntetic data in which the class
conditional likelihoods are Gaussian distributed with distinct means
(-5 and 5) and a common covariance matrix. An Extended Kalman Filter
using Logistic Regression has then been implemented in order to
reliably estimate a classification boundary for this classification
problem.

<video controls>
    <source
    src="/assets/img/posts/Boundaryex.webm"
    type="video/mp4"
    />
</video>

In order to make this classification task more challenging, different
class distributions values have been tried (eg. -3, 3)

<video class="center" controls>
  <source
    src="/assets/img/posts/Boundary_anim2.mp4"
    type="video/mp4"
  />
  Your browser does not support the video tag.
</video>
