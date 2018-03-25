---
layout: post
share: true
title: Auto-Encoding Variational Bayes
date: 2018-03-26 00:24:51 +0000
author:
  name: Nikhil Vinay Sharma
  email: nikhilvs999@gmail.com
categories:
- General Deep Learning
tags:
- Medium
- Theory
---
**Abstract:** How can we perform efficient inference and learning in directed probabilistic models, in the presence of continuous latent variables with intractable posterior distributions, and large datasets? We introduce a stochastic variational inference and learning algorithm that scales to large datasets and, under some mild differentiability conditions, even works in the intractable case. Our contributions is two-fold. First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods. Second, we show that for i.i.d. datasets with continuous latent variables per datapoint, posterior inference can be made especially efficient by fitting an approximate inference model (also called a recognition model) to the intractable posterior using the proposed lower bound estimator. Theoretical advantages are reflected in experimental results.   

**Paper Link:** [https://arxiv.org/pdf/1312.6114.pdf](https://arxiv.org/pdf/1312.6114.pdf "https://arxiv.org/pdf/1312.6114.pdf")

**Task:** Implement the auto-encoder given in the paper on MNIST dataset using Tensorflow/PyTorch/MXNet. Report both the graphs of loss function obtained by your code and the one present in the paper.