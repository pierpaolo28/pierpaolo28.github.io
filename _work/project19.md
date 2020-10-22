---
layout: post_book
date: 2020-05-27
title: Mountain Car Problem
tags: [Reinforcement Learning]
featured-img: rotation
img-type: gif
github: https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Reinforcment%20Learning
---

In this project, is available a practical Demonstration of three different Reinforcement Learning
Approaches which can be used in order to solve the Open AI Gym
Mountain Car Problem. The Mountain Car problem is a classic
Reinforcement Learning exercise. In this scenario, the agent (a car)
is stuck in a valley and aims to drive up to the top of a hill by
optimising it’s velocity and position (continuous state space). In
this exercise, three different approaches have been considered in
order to solve this problem: using tabular Q-learning, approximating
the tabular representation using RBF and learning the weights of the
RBF approximation on-line using Q-learning.

## Tabular approximation, RBF Tabular approximation and Q-learning RBF approximation in action

In this section, is available a video demonstration of the 3 proposed
methods in action in order to solve the mountain car problem. As shown
in the following video, the Q-learning RBF approximation was the
method which performed best in order to solve this task with the less
amount of steps as possible.

<video class="center" controls>
  <source
    src="/assets/img/posts/mountain-car.mp4"
    type="video/mp4"
  />
  Your browser does not support the video tag.
</video>


## RBF Q-learning Approximation optimised Cost-to-go function
![](/assets/img/posts/rotation.gif)
