---
layout: post
share: true
title: Training a Feedback Loop for Hand Pose Estimation
author:
  name: Vikram Waradpande
  email: f2015454@pilani.bits-pilani.ac.in
categories:
- CNN
- Architecture
tags:
- Hard
date: 2019-03-22 01:07:00 +0000

---
**Abstract:** We propose an entirely data-driven approach to estimating the 3D pose of a hand given a depth image. We show that we can correct the mistakes made by a Convolutional Neural Network trained to predict an estimate of the 3D pose by using a feedback loop. The components of this feedback loop are also Deep Networks, optimized using training data. They remove the need for fitting a 3D model to the input data, which requires both a carefully designed fitting function and algorithm. We show that our approach outperforms state-of-the-art methods, and is efficient as our implementation runs at over 400 fps on a single GPU.

**Paper Link:** [https://arxiv.org/pdf/1609.09698.pdf](https://arxiv.org/pdf/1609.09698.pdf "https://arxiv.org/pdf/1609.09698.pdf")

**Tasks:** 

1. Implement the updater, synthesiser and predictor functions as given in section 3 of the paper.
2. Develop the architecture of the network as depicted in figure 5.

**ID:** 123