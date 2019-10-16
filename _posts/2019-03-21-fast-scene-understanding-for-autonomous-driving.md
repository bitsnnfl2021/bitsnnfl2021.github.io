---
layout: post
share: true
title: 'Fast Scene Understanding for Autonomous Driving (Paper ID : 24)'
author:
  name: Aditi Agarwal
  email: f2016095@pilani.bits-pilani.ac.in
categories:
- Semantic Segmentation
- Instance Segmentation
tags:
- Medium
date: 2019-03-21 20:46:08 +0000

---
**Abstract:** Most approaches for instance-aware semantic labeling traditionally focus on accuracy. Other aspects like runtime and memory footprint are arguably as important for realtime applications such as autonomous driving. Motivated by this observation and inspired by recent works that tackle multiple tasks with a single integrated architecture \[13\], \[20\], \[22\], in this paper we present a real-time efficient implementation based on ENet \[18\] that solves three autonomous driving related tasks at once: semantic scene segmentation, instance segmentation and monocular depth estimation. Our approach builds upon a branched ENet architecture with a shared encoder but different decoder branches for each of the three tasks. The presented method can run at 21 fps at a resolution of 1024x512 on the Cityscapes dataset without sacrificing accuracy compared to running each task separately.

**Paper Link:** [https://arxiv.org/pdf/1708.02550.pdf](https://arxiv.org/pdf/1708.02550.pdf "https://arxiv.org/pdf/1708.02550.pdf")

**Task:**

1. Implement the above paper in Python using PyTorch, Keras or Tensorflow.(paper was originally implemented using Torch, written in Lua).
2. Semantic Segmentation needs to be implemented. You must also implement one of instance segmentation and depth.
3. Compare your results with the state of the art-models.

**Paper ID :** **24**
