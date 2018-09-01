---
layout: post
share: true
title: Convolutional Pose Machines
date: 2018-08-26 08:17:23 +0530
author:
  name: Aakriti Agrawal
  email: f2015276@pilani.bits-pilani.ac.in
categories:
- CNN
- Human Pose Estimation
tags:
- 'Hard '

---
Pose Machines provide a sequential prediction framework for learning rich implicit spatial models. In this work we show a systematic design for how convolutional networks can be incorporated into the pose machine framework for learning image features and image-dependent spatial models for the task of pose estimation. The contribution of this paper is to implicitly model long-range dependencies between variables in structured prediction tasks such as articulated pose estimation. We achieve this by designing a sequential architecture composed of convolutional networks that directly operate on belief maps from previous stages, producing increasingly refined estimates for part locations, without the need for explicit graphical model-style inference. Our approach addresses the characteristic difficulty of vanishing gradients during training by providing a natural learning objective function that enforces intermediate supervision, thereby replenishing back-propagated gradients and conditioning the learning procedure. We demonstrate state-of-the-art performance and outperform competing methods on standard benchmarks including the MPII, LSP, and FLIC datasets.

Link: [https://arxiv.org/pdf/1602.00134.pdf](https://arxiv.org/pdf/1602.00134.pdf "https://arxiv.org/pdf/1602.00134.pdf")

ID : 12