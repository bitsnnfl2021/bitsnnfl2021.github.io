---
layout: post
share: true
title: Spatial Transformer Networks
date: 2018-03-26 01:27:01 +0000
author:
  name: Nikhil Vinay Sharma
  email: nikhilvs999@gmail.com
categories:
- General Deep Learning
tags:
- Easy
- Theory
---
**Abstract:** Convolutional Neural Networks define an exceptionally powerful class of models, but are still limited by the lack of ability to be spatially invariant to the input data in a computationally and parameter efficient manner. In this work we introduce a new learnable module, the Spatial Transformer, which explicitly allows the spatial manipulation of data within the network. This differentiable module can be inserted into existing convolutional architectures, giving neural networks the ability to actively spatially transform feature maps, conditional on the feature map itself, without any extra training supervision or modification to the optimisation process. We show that the use of spatial transformers results in models which learn invariance to translation, scale, rotation and more generic warping, resulting in state-of-the-art performance on several benchmarks, and for a number of classes of transformations.

**Paper Link:** [http://papers.nips.cc/paper/5854-spatial-transformer-networks.pdf](http://papers.nips.cc/paper/5854-spatial-transformer-networks.pdf "http://papers.nips.cc/paper/5854-spatial-transformer-networks.pdf")

**Task:** Implement the given method using Tensorflow/Pytorch. The submitted code would be checked for plagiarism with the implementations available online. Show results on the MNIST dataset.