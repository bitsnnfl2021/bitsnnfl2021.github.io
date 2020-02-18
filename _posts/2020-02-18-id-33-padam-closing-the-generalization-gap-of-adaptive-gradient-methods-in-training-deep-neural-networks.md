---
layout: post
author:
  name: 'Paper ID: 33'
  email: bitsnnfl@gmail.com
share: true
title: 'Padam: Closing the Generalization gap of adaptive gradient methods in training
  deep neural networks'
categories:
- optimizers
- hyperparameter tuning
tags:
- medium

---
**Abstract:** Adaptive gradient methods, which adopt historical gradient information to automatically adjust the learning rate, have been observed to generalize worse than stochastic gradient descent (SGD) with momentum in training deep neural networks. This leaves how to close the generalization gap of adaptive gradient methods an open problem. In this work, we show that adaptive gradient methods such as Adam, Amsgrad, are sometimes "over adapted". We design a new algorithm, called Partially adaptive momentum estimation method (Padam), which unifies the Adam/Amsgrad with SGD to achieve the best from both worlds. Experiments on standard benchmarks show that Padam can maintain fast convergence rate as Adam/Amsgrad while generalizing as well as SGD in training deep neural networks. These results would suggest practitioners pick up adaptive gradient methods once again for faster training of deep neural networks.

[https://arxiv.org/abs/1806.06763](https://arxiv.org/abs/1806.06763 "https://arxiv.org/abs/1806.06763")

***

**Task:**

1. Implement the PADAM Optimizer
2. Compare PADAM's generalization performance with Adam, SGD+Momentum and Amsgrad using a Resnet34.
3. Show results on 2 datasets: Imagenet and Imagewoof.

***

**Dataset:**

Show results on two different datasets (both available at [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette "https://github.com/fastai/imagenette")):  
1\. Imagenette (a simpler, easy subset of Imagenet)

2\. Imagewoof (a relatively harder subset of Imagenet)

**Framework:** You cannot use Tensorflow.