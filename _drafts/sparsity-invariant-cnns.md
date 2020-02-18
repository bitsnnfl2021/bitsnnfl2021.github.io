---
layout: post
author:
  name: Rishav
  email: bitsnnfl@gmail.com
share: true
title: Sparsity Invariant CNNs
categories: []
tags: []

---
In this paper, we consider convolutional neural networks operating on sparse inputs with an application to depth upsampling from sparse laser scan data. First, we show that traditional convolutional networks perform poorly when applied to sparse data even when the location of missing data is provided to the network. To overcome this problem, we propose a simple yet effective sparse convolution layer that explicitly considers the location of missing data during the convolution operation. We demonstrate the benefits of the proposed network architecture in synthetic and real experiments with respect to various baseline approaches. Compared to dense baselines, the proposed sparse convolution network generalizes well to novel datasets and is invariant to the level of sparsity in the data.

Paper: [https://arxiv.org/pdf/1708.06500.pdf](https://arxiv.org/pdf/1708.06500.pdf "https://arxiv.org/pdf/1708.06500.pdf")

Implement the architecture and the convolution operation and train it on a subset of the KITTI 2015 benchmark.