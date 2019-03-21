---
layout: post
share: true
title: 'SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model
  size'
author:
  name: Suvigya Vijay
  email: f2015606@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Easy
date: 2019-03-21 13:39:23 +0000

---
**Abstract:** Recent research on deep convolutional neural networks (CNNs) has focused primarily on improving accuracy. For a given accuracy level, it is typically possible to identify multiple CNN architectures that achieve that accuracy level. With equivalent accuracy, smaller CNN architectures offer at least three advantages: (1) Smaller CNNs require less communication across servers during distributed training. (2) Smaller CNNs require less bandwidth to export a new model from the cloud to an autonomous car. (3) Smaller CNNs are more feasible to deploy on FPGAs and other hardware with limited memory. To provide all of these advantages, we propose a small CNN architecture called SqueezeNet. SqueezeNet achieves AlexNet-level accuracy on ImageNet with 50x fewer parameters. Additionally, with model compression techniques, we are able to compress SqueezeNet to less than 0.5MB (510× smaller than AlexNet).

**Paper Link:** [https://arxiv.org/pdf/1602.07360.pdf](https://arxiv.org/pdf/1602.07360.pdf "https://arxiv.org/pdf/1602.07360.pdf")

1. Implement the architecture given in the paper preferrably not in Pytorch.
2. Plot the graphs and results for Imagenet and COCO dataset both.

**ID:** 93