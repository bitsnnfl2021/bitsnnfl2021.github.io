---
layout: post
share: true
title: 'Adam: A Method for Stochastic Optimization'
date: 2018-03-26 00:56:47 +0000
author:
  name: Nikhil Vinay Sharma
  email: nikhilvs999@gmail.com
categories:
- General Deep Learning
tags:
- Easy
- Theory
- Brownie Points
---
**Abstract:** We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments. The method is straightforward to implement, is computationally efficient, has little memory requirements, is invariant to diagonal rescaling of the gradients, and is well suited for problems that are large in terms of data and/or parameters. The method is also appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require little tuning. Some connections to related algorithms, on which Adam was inspired, are discussed. We also analyze the theoretical convergence properties of the algorithm and provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization framework. Empirical results demonstrate that Adam works well in practice and compares favorably to other stochastic optimization methods. Finally, we discuss AdaMax, a variant of Adam based on the infinity norm.   

**Paper Link:** [https://arxiv.org/pdf/1412.6980.pdf](https://arxiv.org/pdf/1412.6980.pdf "https://arxiv.org/pdf/1412.6980.pdf")

**Task:** Implement the given method using **NumPy only**. The submitted code would be checked for similarity with the implementations available online. Show results on MNIST and CIFAR- 10 datasets using a multi-layer perception neural network.

**Brownie Points:** Implement one more different algorithm for optimization of your choice.