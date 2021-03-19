---
layout: post
author:
  name: Paper ID 52
  difficulty: Easy
share: true
title: Weight Uncertainty in Neural Networks
categories:
- Reinforcement Learning
- Backpropagation
- Bayesian learning
- easy

tags: []

---
**Abstract** - We introduce a new, efficient, principled and backpropagation-compatible algorithm for learning a probability distribution on the weights of a neural network, called Bayes by Backprop. It regularises the weights by minimising a compression cost, known as the variational free energy or the expected lower bound on the marginal likelihood. We show that this principled kind of regularisation yields comparable performance to dropout on MNIST classification. We then demonstrate how the learnt uncertainty in the weights can be used to improve generalisation in non-linear regression problems, and how this weight uncertainty can be used to drive the exploration-exploitation trade-off in reinforcement learning.

**Paper** - [https://arxiv.org/pdf/1505.05424v2.pdf](https://arxiv.org/pdf/1505.05424v2.pdf)

**Dataset -** [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
    