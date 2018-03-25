---
layout: post
share: true
title: Generative Adversarial Nets
date: 2018-03-26 00:17:09 +0000
author:
  name: Nikhil Vinay Sharma
  email: nikhilvs999@gmail.com
categories: []
tags: []
---
**Abstract:** We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1 2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.  

**Paper Link:** [http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf](http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf "http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf")

**Task:** Implement the GANs using Tensorflow/PyTorch on the MNIST and CIFAR-10 datasets. Report the loss function graphs obtained by your code.