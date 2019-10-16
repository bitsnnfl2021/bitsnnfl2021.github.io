---
layout: post
share: true
title: 'Fractional Max-Pooling (Paper ID: 45)'
author:
  name: Dhaivata Pandya
  email: f2016020@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Easy
date: 2019-03-23 13:23:09 +0000

---
**Abstract:** Convolutional networks almost always incorporate some form of spatial pooling, and very often it is alpha times alpha max-pooling with alpha=2. Max-pooling act on the hidden layers of the network, reducing their size by an integer multiplicative factor alpha. The amazing by-product of discarding 75% of your data is that you build into the network a degree of invariance with respect to translations and elastic distortions. However, if you simply alternate convolutional layers with max-pooling layers, performance is limited due to the rapid reduction in spatial size, and the disjoint nature of the pooling regions. We have formulated a fractional version of max-pooling where alpha is allowed to take non-integer values. Our version of max-pooling is stochastic as there are lots of different ways of constructing suitable pooling regions. We find that our form of fractional max-pooling reduces overfitting on a variety of datasets: for instance, we improve on the state-of-the art for CIFAR-100 without even using dropout.

**Paper Link:** [https://arxiv.org/abs/1412.6071v4](https://arxiv.org/abs/1412.6071v4 "https://arxiv.org/abs/1412.6071v4")

**Paper ID:** **45**

**Guidelines:**

1. Understand the Fractional Max-Pooling method described in the paper.
2. Download the tiny imagenet dataset (Link: [https://tiny-imagenet.herokuapp.com/](https://tiny-imagenet.herokuapp.com/ "https://tiny-imagenet.herokuapp.com/"))
3. Build a simple CNN architecture (e.g. VGGNet) for Image classification on the tiny imagenet dataset.
4. Train two models of the CNN architecture, one with Max-Pooling and the other with Fractional Max-Pooling method. (Choose filter sizes etc accordingly)
5. Report the accuracy achieved by both the models for image classification on the tiny imagenet dataset and compare the results.
