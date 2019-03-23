---
layout: post
share: true
title: Learning to Learn by Gradient Descent by Gradient Descent
author:
  name: Kabir Ahuja
  email: f2015791@pilani.bits-pilani.ac.in
categories: []
tags: []
date: 2019-03-20 10:29:01 +0000

---
**Abstract:** The move from hand-designed features to learned features in machine learning has been wildly successful. In spite of this, optimization algorithms are still designed by hand. In this paper we show how the design of an optimization algorithm can be cast as a learning problem, allowing the algorithm to learn to exploit structure in the problems of interest in an automatic way. Our learned algorithms, implemented by LSTMs, outperform generic, hand-designed competitors on the tasks for which they are trained, and also generalize well to new tasks with similar structure. We demonstrate this on a number of tasks, including simple convex problems, training neural networks, and styling images with neural art.

**Paper Link:** [https://arxiv.org/abs/1606.04474](https://arxiv.org/abs/1606.04474 "https://arxiv.org/abs/1606.04474")

**Paper ID: 61**

**Guidelines**:

1. Implement the proposed algorithm (coordinate wise lstm) on the quadratic functions and a small fully connected neural network on MNIST and CIFAR10
2. Compare the results of the algorithm with other optimization methods like SGD, Adam, RMS Prop as done in the paper.
3. Use the gradient preprocessing technique mentioned in the appendix and compare it with the variant which does not use that preprocessing scheme.
4. Implement either Global averaging cells method or NTM BFGS or NTM L-BFGS on atleast one of the problems mentioned in first point.