---
layout: post
share: true
title: Population Based Training of Neural Networks
date: 2018-08-26 11:58:07 +0530
author:
  name: Rohitkumar Arasanipalai
  email: f2015666@pilani.bits-pilani.ac.in
categories:
- Neural Networks
- Hyperparameter Optimization
tags:
- Hard

---
Neural networks dominate the modern machine learning landscape, but their training and success still suffer from sensitivity to empirical choices of hyperparameters such as model architecture, loss function, and optimisation algorithm. In this work we present Population Based Training (PBT), a simple asynchronous optimisation algorithm which effectively utilises a fixed computational budget to jointly optimise a population of models and their hyperparameters to maximise performance. Importantly, PBT discovers a schedule of hyperparameter settings rather than following the generally sub-optimal strategy of trying to find a single fixed set to use for the whole course of training. With just a small modification to a typical distributed hyperparameter training framework, our method allows robust and reliable training of models. We demonstrate the effectiveness of PBT on deep reinforcement learning problems, showing faster wall-clock convergence and higher final performance of agents by optimising over a suite of hyperparameters. In addition, we show the same method can be applied to supervised learning for machine translation, where PBT is used to maximise the BLEU score directly, and also to training of Generative Adversarial Networks to maximise the Inception score of generated images. In all cases PBT results in the automatic discovery of hyperparameter schedules and model selection which results in stable training and better final performance.  

Link: [https://arxiv.org/abs/1711.09846](https://arxiv.org/abs/1711.09846 "https://arxiv.org/abs/1711.09846")