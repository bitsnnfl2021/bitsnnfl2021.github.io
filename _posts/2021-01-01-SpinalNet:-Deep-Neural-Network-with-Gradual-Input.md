---
layout: post
author:
  name: Paper ID 56
  difficulty: Easy
share: true
title: SpinalNet: Deep Neural Network with Gradual Input
categories:
- image classification
- computer vision
tags: []

---
**Abstract** - Over the past few years, deep neural networks (DNNs) have garnered remarkable success in a diverse range of real-world applications. However, DNNs consider a large number of inputs and consist of a large number of parameters, resulting in high computational demand. We study the human somatosensory system and propose the SpinalNet to achieve higher accuracy with less computational resources. In a typical neural network (NN) architecture, the hidden layers receive inputs in the first layer and then transfer the intermediate outcomes to the next layer. In the proposed SpinalNet, the structure of hidden layers allocates to three sectors: 1) Input row, 2) Intermediate row, and 3) output row. The intermediate row of the SpinalNet contains a few neurons. The role of input segmentation is in enabling each hidden layer to receive a part of the inputs and outputs of the previous layer. Therefore, the number of incoming weights in a hidden layer is significantly lower than traditional DNNs. As all layers of the SpinalNet directly contributes to the output row, the vanishing gradient problem does not exist. We also investigate the SpinalNet fully-connected layer to several well-known DNN models and perform traditional learning and transfer learning. We observe significant error reductions with lower computational costs in most of the DNNs. We have also obtained the state-of-the-art (SOTA) performance for QMNIST, Kuzushiji-MNIST, EMNIST (Letters, Digits, and Balanced), STL-10, Bird225, Fruits 360, and Caltech-101 datasets.

**Paper** - [https://arxiv.org/pdf/2007.03347v2.pdf](https://arxiv.org/pdf/2007.03347v2.pdf)

**Dataset -** [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)
    