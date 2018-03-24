---
layout: post
share: true
title: Convex Neural Networks
date: 2018-03-24 16:20:05 +0000
author:
  name: Satwik Bhattamishra
  email: satwik55@gmail.com
categories:
- Core Deep Learning
tags:
- Hard
- Theory
- Algorithm
- Optimization
---
**Abstract:** Convexity has recently received a lot of attention in the machine learning community, and the lack of convexity has been seen as a major disadvantage of many learning algorithms, such as multi-layer artificial neural networks. We show that training multi-layer neural networks in which the number of hidden units is learned can be viewed as a convex optimization problem. This problem involves an infinite number of variables, but can be solved by incrementally inserting a hidden unit at a time, each time finding a linear classifier that minimizes a weighted sum of errors. 

**Paper Link:** [https://papers.nips.cc/paper/2800-convex-neural-networks](https://papers.nips.cc/paper/2800-convex-neural-networks "https://papers.nips.cc/paper/2800-convex-neural-networks")

**Task:** Implement the incremental Convex NN algorithm described in the paper in python using Numpy, TensorFlow, Pytorch or MXNet. Test your implementation on 2D double moon toy dataset.
