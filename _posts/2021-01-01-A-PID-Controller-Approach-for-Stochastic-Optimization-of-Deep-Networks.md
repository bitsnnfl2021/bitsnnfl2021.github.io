---
layout: post
author:
  name: Paper ID 67
  difficulty: Medium
share: true
title: A PID Controller Approach for Stochastic Optimization of Deep Networks
categories:
- Optimization
- Computer Vision
- PID
- medium

tags: []

---
**Abstract** - Deep neural networks have demonstrated their power in many computer vision applications. State-of-the-art deep architectures such as VGG, ResNet, and DenseNet are mostly optimized by the SGD-Momentum algorithm, which updates the weights by considering their past and current gradients. Nonetheless, SGD-Momentum suffers from the overshoot problem, which hinders the convergence of network training. Inspired by the prominent success of proportional-integral-derivative (PID) controller in automatic control, we propose a PID approach for accelerating deep network optimization. We first reveal the intrinsic connections between SGD-Momentum and PID based controller, then present the optimization algorithm which exploits the past, current, and change of gradients to update the network parameters. The proposed PID method reduces much the overshoot phenomena of SGD-Momentum, and it achieves up to 50% acceleration on popular deep network architectures with competitive accuracy, as verified by our experiments on the benchmark datasets including CIFAR10, CIFAR100, and Tiny-ImageNet.

**Paper** - [https://openaccess.thecvf.com/content_cvpr_2018/papers/An_A_PID_Controller_CVPR_2018_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2018/papers/An_A_PID_Controller_CVPR_2018_paper.pdf)

**Dataset -** [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)
    