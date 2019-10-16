---
layout: post
share: true
title: 'Densely Connected Convolutional Networks (Paper ID: 104)'
author:
  name: Sahil Ranadive
  email: f2016097@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Medium
date: 2019-03-20 09:11:17 +0000

---
**Abstract:** Recent work has shown that convolutional networks can be substantially deeper, more accurate, and efficient to train if they contain shorter connections between layers close to the input and those close to the output. In this paper, we embrace this observation and introduce the Dense Convolutional Network (DenseNet), which connects each layer to every other layer in a feed-forward fashion. Whereas traditional convolutional networks with L layers have L connections—one between each layer and its subsequent layer—our network has L(L+1) 2 direct connections. For each layer, the feature-maps of all preceding layers are used as inputs, and its own feature-maps are used as inputs into all subsequent layers. DenseNets have several compelling advantages: they alleviate the vanishing-gradient problem, strengthen feature propagation, encourage feature reuse, and substantially reduce the number of parameters. We evaluate our proposed architecture on four highly competitive object recognition benchmark tasks (CIFAR-10, CIFAR-100, SVHN, and ImageNet). DenseNets obtain significant improvements over the state-of-the-art on most of them, whilst requiring less computation to achieve high performance.

**Paper link:** [https://arxiv.org/pdf/1608.06993.pdf](https://arxiv.org/pdf/1608.06993.pdf "https://arxiv.org/pdf/1608.06993.pdf")

Tasks:

1. Implement the architecture used in the paper and test it on Imagenet and CIFAR.
2. Change the number of blocks and number of layers in each block and then compare the results.

**ID:** 104
