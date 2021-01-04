---
layout: post
date: 2021-01-04
---

# Foundations of Data Structures and Algorithms

> "Computer Science is no more about **computers** than astronomy is about **telescopes**"
> --Edgar W.Dijkstra

## Object Oriented Programming

- **Object**: **Instance** of a class.
- **Class**: **Template** for constructing objects (an abstraction of a real entity used to store and manipulate data however we think it is necessary). When we use a class to construct distinct objects, we call these objects instances.

Classes have two main components fields and methods. The **fields** describe the state of the object (e.g. length/width of a rectangle). The **methods** instead describe the behaviour of the object (e.g. a function created in order to modify the different parameters of a rectangle).

When trying to create complex programs, it might happen that different classes share similar characteristics. In this case, it might be useful to make use of **inheritance** (e.g. if we are creating a class for creating squares, and we already have a class for creating rectangles, then we can just inherit the information from the class to create rectangles and add some constrains to create a class to instantiate squares).

**Primitive Operation**: any operation that corresponds to a low-level instruction that runs in constant time (e.g. assigning a value to a variable, calling a method,..).

## Analysis of Algorithms

Many computer science tasks are heavily based on algorithms. In order to decide if an algorithm is overall better than another for a specific task, it is then necessary to set up a consistent way to judge them. Using primitive operations takes time, and therefore when designing an algorithm we should aim to minimize as much as we can the number of times we use them (in order to make our algorithm run faster).

The key question we should ask ourselves in order to design good algorithms is: How does the number of primitive operations relate to the size of our input?

**Big O notation**: refers to the limiting behaviour of a function (worst case scenario). If we execute our algorithm multiple times and vary the input size, we can then plot the number of operations used to solve the problem against the number of provided input elements. The resulting curve will then represent which trend our algorithm follows as we increase the input size. Our objective in this case is to minimize the area under the curve (Figure 1). The Big O Notation can then be used to quantify the efficiency of the different algorithms. When we talk about the Big O Notation, we typically take into account the algorithm behaviour for very large input values (because of that we generally ignore constants).

![](/assets/img/bigocomplexitychart.jpeg)<br>
[Figure 1: Amitshahi.dev, Big 'O' Notation](https://amitshahi.dev/blog/2019-06-23-big-o-notation/)

Time complexities examples:
- **O(1)**: constant time (the runtime of the algorithm is not dependent on the size of the input). The plot will therefore be a flat spectrogram.
- **O(log(n))**: we cut our input size in half repeatedly, which is modelled by log base two (e.g. binary search).
- **O(n)**: linear time (number of operations = input size).
- **O(nlog(n))**: typically seen in sorting and divide and conquer style Algorithms (e.g. running something O(n), log(n) times or  O(log(n)), n times).
- **O(n<sup>2</sup>)**: is slower than linear time and often occurs when working with 2 nested loops.

This same type of reasoning can be applied not just to time complexity (how fast an algorithm runs), but as well to space complexity (how much memory it needs to run).

## Recursion
In the world of problem solving, recursion is about taking a big problem and then breaking it down into smaller and smaller components until we reach a base case (e.g. factorial computation).

Therefore, a recursive function refers back to itself until reaching a base case (this generates a recursive trace, in which at each call information is stored about the computed result waited to be used once reached the base condition). One problem with using recursion is that each function call is stored on the stack trace (making too many calls to the recursive function could therefore potentially lead to memory issues in the long run).

## Resources and References
- [Reducible](https://www.youtube.com/channel/UCK8XIGR5kRidIw2fWqwyHRA/videos)
- [Zeved](https://www.youtube.com/channel/UC0dnuYW1-BKqBLBBC3E_diA)
