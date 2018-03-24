---
layout: post
share: true
title: SqueezeNet
date: 2018-03-24 19:33:18 +0000
author:
  name: Satwik Bhattamishra
  email: satwik55@gmail.com
categories:
- General Deep Learning
- Computer Vision
tags:
- Medium
- Application
- Theory
- Compression
---
**Abstract:** Recent research on deep convolutional neural networks (CNNs) has focused primarily on improving accuracy. For a given accuracy level, it is typically possible to identify multiple CNN architectures that achieve that accuracy level. With equivalent accuracy, smaller CNN architectures offer at least three advantages: (1) Smaller CNNs require less communication across servers during distributed train- ing. (2) Smaller CNNs require less bandwidth to export a new model from the cloud to an autonomous car. (3) Smaller CNNs are more feasible to deploy on FP- GAs and other hardware with limited memory. To provide all of these advantages, we propose a small CNN architecture called SqueezeNet. SqueezeNet achieves AlexNet-level accuracy on ImageNet with 50x fewer parameters. Additionally, with model compression techniques, we are able to compress SqueezeNet to less than 0.5MB (510× smaller than AlexNet).

**Paper Link:** [https://arxiv.org/pdf/1602.07360.pdf](https://arxiv.org/pdf/1602.07360.pdf)

**Task:** Implement the described squeeze network architecture explained in the paper in python using TensorFlow, Pytorch or MXNet. Test your implementation on mini-ImageNet dataset.

**Brownie points:** Compare the size of your model with that of general Alex Net architecture.