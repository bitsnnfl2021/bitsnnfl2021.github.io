---
layout: post
author:
  name: Paper ID 29
  difficulty: Easy
share: true
title: Rethinking the Inception Architecture for Computer Vision
categories:
- optimization
- convolutional neural networks
tags: []

---
**Abstract** - Convolutional networks are at the core of most state-of-the-art computer vision solutions for a wide variety oftasks. Since 2014 very deep convolutional networks startedto become mainstream, yielding substantial gains in vari-ous benchmarks. Although increased model size and com-putational cost tend to translate to immediate quality gainsfor most tasks (as long as enough labeled data is providedfor training), computational efficiency and low parametercount are still enabling factors for various use cases such asmobile vision and big-data scenarios. Here we are explor-ing ways to scale up networks in ways that aim at utilizingthe added computation as efficiently as possible by suitablyfactorized convolutions and aggressive regularization. Webenchmark our methods on the ILSVRC 2012 classificationchallenge validation set demonstrate substantial gains overthe state of the art:21.2%top-1and5.6%top-5error forsingle frame evaluation using a network with a computa-tional cost of5billion multiply-adds per inference and withusing less than 25 million parameters. With an ensemble of4models and multi-crop evaluation, we report3.5%top-5error and17.3%top-1error.

**Paper** - [https://arxiv.org/pdf/1512.00567v3.pdf](https://arxiv.org/pdf/1512.00567v3.pdf)

**Dataset -** [http://www.image-net.org/download](http://www.image-net.org/download)
    