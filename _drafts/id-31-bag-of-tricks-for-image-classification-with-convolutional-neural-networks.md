---
layout: post
share: true
title: "[ID:31] Bag of Tricks for Image Classification with Convolutional Neural Networks"
author:
  name: BITS NNFL
  email: bitsnnfl@gmail.com
categories:
- cnn
tags: []

---
[https://arxiv.org/abs/1812.01187](https://arxiv.org/abs/1812.01187 "https://arxiv.org/abs/1812.01187")

The paper is about implementing a lot of the recent developments in CNNs to train networks better. These include:

1. LR Warmup Scheduling
2. Cosine Learning Rate Decay
3. No Bias Decay
4. FP16 Training
5. Zero Gamma for Batchnorm (Initialize both batchnorm parameters as 0,0 instead of 1,0)
6. Mixup Training
7. Label Smoothing
8. Tweaks to ResNets

Training can be done on a subset of Imagenet such as Imagenette or Imagewoof (by FastAI)

All these add up to improve training significantly. I'm thinking of giving this paper to two groups both of which can implement disjoint halves of these 8 improvements.

Will add more details soon.