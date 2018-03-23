---
layout: post
share: true
title: Self-Replicating Neural Network
date: 2018-03-24 03:04:07 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- General Deep Learning
tags:
- Easy
- Theory
---
**Abstract:** Self-replication is a key aspect of biological life that has been largely overlooked in Artificial Intelligence systems. Here we describe how to build and train self-replicating neural networks. The network replicates itself by learning to output its own weights. The network is designed using a loss function that can be optimized with either gradient-based or nongradient-based methods. We also describe a method we call regeneration to train the network without explicit optimization, by injecting the network with predictions of its own parameters. The best solution for a self-replicating network was found by alternating between regeneration and optimization steps. Finally, we describe a design for a self-replicating neural network that can solve an auxiliary task such as MNIST image classification. We observe that there is a trade-off between the network’s ability to classify images and its ability to replicate, but training is biased towards increasing its specialization at image classification at the expense of replication. This is analogous to the trade-off between reproduction and other tasks observed in nature. We suggest that a selfreplication mechanism for artificial intelligence is useful because it introduces the possibility of continual improvement through natural selection.

**Paper Link:** [https://arxiv.org/pdf/1803.05859.pdf](https://arxiv.org/pdf/1803.05859.pdf "https://arxiv.org/pdf/1803.05859.pdf")

**Task:** Implement the architecture in python using Tensorflow, Pytorch, MXNet or NumPy. Train the network on MNIST and FashionMNIST.