---
layout: post
share: true
title: 'ADAPTIVE GRADIENT METHODS WITH DYNAMIC BOUND OF LEARNING RATE (Paper ID: 161)'
author:
  name: Aashay Mehta
  email: f2016079@pilani.bits-pilani.ac.in
categories:
- Optimisation
tags:
- Easy
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Adaptive optimization methods such as ADAGRAD, RMSPROP and ADAM have been proposed to achieve a rapid training process with an element-wise scaling term on learning rates. Though prevailing, they are observed to generalize poorly compared with SGD or even fail to converge due to unstable and extreme learning rates. Recent work has put forward some algorithms such as AMSGRAD to tackle this issue but they failed to achieve considerable improvement over existing methods. In our paper, we demonstrate that extreme learning rates can lead to poor performance. We provide new variants of ADAM and AMSGRAD, called ADABOUND and AMSBOUND respectively, which employ dynamic bounds on learning rates to achieve a gradual and smooth transition from adaptive methods to SGD and give a theoretical proof of convergence. We further conduct experiments on various popular tasks and models, which is often insufficient in previous work. Experimental results show that new variants can eliminate the generalization gap between adaptive methods and SGD and maintain higher learning speed early in training at the same time. Moreover, they can bring significant improvement over their prototypes, especially on complex deep networks.

**Paper Link:** [https://arxiv.org/pdf/1902.09843.pdf](https://arxiv.org/pdf/1902.09843.pdf)

**ID:** 161

**Guidelines:**

1. Implement the optimizer AdaBound as described in the paper.
2. Compare its performance with popular optimizers like SGD, Adam and AdaGrad. You can use the CIFAR-10 dataset or the Penn treebank.
3. Try optimizing different architectures (min 2). Make sure that the architectures you use are sufficiently complex so that the performance differences can be seen.


**Dataset Link**: [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)

