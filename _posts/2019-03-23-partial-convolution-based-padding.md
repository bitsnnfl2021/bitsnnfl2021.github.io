---
layout: post
share: true
title: 'Partial Convolution based Padding (Paper ID: 42)'
author:
  name: Vivek Golani
  email: f2016196@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Easy
date: 2019-03-23 09:41:34 +0000

---
**Abstract:** In this paper, we present a simple yet effective padding scheme that can be used as a drop-in module for existing convolutional neural networks. We call it partial convolution based padding, with the intuition that the padded region can be treated as holes and the original input as non-holes. Specifically, during the convolution operation, the convolution results are re-weighted near image borders based on the ratios between the padded area and the convolution sliding window area. Extensive experiments with various deep network models on ImageNet classification and semantic segmentation demonstrate that the proposed padding scheme consistently outperforms standard zero padding with better accuracy.

**Paper link:** [https://arxiv.org/abs/1811.11718](https://arxiv.org/abs/1811.11718 "https://arxiv.org/abs/1811.11718")

**Paper ID: 42**

**Guidelines:**

1. Understand the Partial Convolution based Padding method described in the paper.
2. Download the tiny imagenet dataset (Link: [https://tiny-imagenet.herokuapp.com/](https://tiny-imagenet.herokuapp.com/ "https://tiny-imagenet.herokuapp.com/"))
3. Build a simple CNN architecture (e.g. VGGNet) for Image classification on the tiny imagenet dataset.
4. Train two models of the CNN architecture, one with Zero padding and the other with partial convolution based padding method. (Choose filter sizes etc accordingly)
5. Report the accuracy achieved by both the models for image classification on the tiny imagenet dataset and compare the results.
