---
layout: post
share: true
title: Fractional Max-Pooling
author:
  name: Amit Tiwary
  email: f2015818@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Easy
date: 2019-03-23 13:23:09 +0000

---
**Abstract:** Convolutional networks almost always incorporate some form of spatial pooling, and very often it is alpha times alpha max-pooling with alpha=2. Max-pooling act on the hidden layers of the network, reducing their size by an integer multiplicative factor alpha. The amazing by-product of discarding 75% of your data is that you build into the network a degree of invariance with respect to translations and elastic distortions. However, if you simply alternate convolutional layers with max-pooling layers, performance is limited due to the rapid reduction in spatial size, and the disjoint nature of the pooling regions. We have formulated a fractional version of max-pooling where alpha is allowed to take non-integer values. Our version of max-pooling is stochastic as there are lots of different ways of constructing suitable pooling regions. We find that our form of fractional max-pooling reduces overfitting on a variety of datasets: for instance, we improve on the state-of-the art for CIFAR-100 without even using dropout.

**Paper Link:** [https://arxiv.org/abs/1412.6071v4](https://arxiv.org/abs/1412.6071v4 "https://arxiv.org/abs/1412.6071v4")

**Paper ID:** **45**

**Guidelines:** Coming Soon.