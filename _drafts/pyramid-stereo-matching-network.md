---
layout: post
author:
  name: Rishav
  email: bitsnnfl@gmail.com
share: true
title: Pyramid Stereo Matching Network
categories: []
tags: []

---
Recent work has shown that depth estimation from a stereo pair of images can be formulated as a supervised learning task to be resolved with convolutional neural networks (CNNs). However, current architectures rely on patch-based Siamese networks, lacking the means to exploit context information for finding correspondence in ill-posed regions. To tackle this problem, we propose PSMNet, a pyramid stereo matching network consisting of two main modules: spatial pyramid pooling and 3D CNN. The spatial pyramid pooling module takes advantage of the capacity of global context information by the aggregating context in different scales and locations to form a cost volume. The 3D CNN learns to regularize cost volume using stacked multiple hourglass networks in conjunction with intermediate supervision. The proposed approach was evaluated on several benchmark datasets.

Paper: [https://arxiv.org/pdf/1803.08669.pdf](https://arxiv.org/pdf/1803.08669.pdf "https://arxiv.org/pdf/1803.08669.pdf")

Replace the CNN module with FPN (Feature Pyramid Network ) and implement the network.

Train it just on KITTI 2015 Stereo Dataset.