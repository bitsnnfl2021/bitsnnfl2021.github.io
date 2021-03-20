---
layout: post
author:
  name: Paper ID 68
  difficulty: Difficulty - Medium
share: true
title: On the Variance of the Adaptive Learning Rate and Beyond
categories:
- Optimization
- Computer Vision
- medium

tags: []

---
**Abstract** - The learning rate warmup heuristic achieves remarkable success in stabilizing training, accelerating convergence and improving generalization for adaptive stochastic optimization algorithms like RMSprop and Adam. Here, we study its mechanism in details. Pursuing the theory behind warmup, we identify a problem of the adaptive learning rate (i.e., it has problematically large variance in the early stage), suggest warmup works as a variance reduction technique, and provide both empirical and theoretical evidence to verify our hypothesis. We further propose RAdam, a new variant of Adam, by introducing a term to rectify the variance of the adaptive learning rate. Extensive experimental results on image classification, language modeling, and neural machine translation verify our intuition and demonstrate the effectiveness and robustness of our proposed method

**Paper** - [https://arxiv.org/abs/1908.03265v3](https://arxiv.org/abs/1908.03265v3)

**Dataset -** [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)

[ http://image-net.org/download]( http://image-net.org/download)
    