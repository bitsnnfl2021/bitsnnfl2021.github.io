---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_53] Controlled dropout: A different approach to using dropout on deep
  neural network"
categories:
- Dropout
- Fully Connected NN
- Matrix Operations
tags: []

---
**Abstract:**

Deep neural networks (DNNs), which show outstanding performance in various areas, consume considerable amounts of memory and time during training. Our research led us to propose a controlled dropout technique with the potential of reducing the memory space and training time of DNNs. Dropout is a popular algorithm that solves the overfitting problem of DNNs by randomly dropping units in the training process. The proposed controlled dropout intentionally chooses which units to drop compared to conventional dropout, thereby possibly facilitating a reduction in training time and memory usage. In this paper, we focus on validating whether controlled dropout can replace the traditional dropout technique to enable us to further our research aimed at improving the training speed and memory efficiency. A performance comparison between controlled dropout and traditional dropout is carried out by implementing an image classification experiment on data comprising handwritten digits from the MNIST dataset (Mixed National Institute of Standards and Technology dataset). The experimental results show that the proposed controlled dropout is as effective as traditional dropout. Furthermore, the experimental result implies that controlled dropout is more efficient when an appropriate dropout rate and number of hidden layers are used.

**Paper Link:** [https://ieeexplore.ieee.org/document/7881693](https://ieeexplore.ieee.org/document/7881693 "https://ieeexplore.ieee.org/document/7881693")

(Use [Sci Hub](https://sci-hub.tw/ "Sci-Hub") in case you are not able to access the paper)

**Published in:** [2017 IEEE International Conference on Big Data and Smart Computing (BigComp)](https://ieeexplore.ieee.org/xpl/conhome/7877084/proceeding)

 

**Tasks:**

1. Implement the model in Tensorflow
2. Compare results of traditional dropout and the proposed method. Vary some of the parameters from what is specified in the paper. 
3. Do not use the entire dataset, use a subset instead and specify which part is being used by you. 

**Data Set:** [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/ "http://yann.lecun.com/exdb/mnist/")

**Paper ID:** 53