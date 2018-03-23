---
layout: post
share: true
title: Neocognitron
date: 2018-03-24 03:00:53 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- Computer Vision
- Antique Architectures
tags:
- Medium
- Theory
---
**Abstract**: Deep neural networks have proved to be a very effective way to perform classification tasks. They excel when the input data is high dimensional, the relationship between the input and the output is complicated, and the number of labeled training examples is large \[Szegedy et al., 2015, Wu et al., 2016, Jozefowicz et al., 2016, Graves et al., 2013\]. But it is hard to explain why a learned network makes a particular classification decision on a particular test case. This is due to their reliance on distributed hierarchical representations. If we could take the knowledge acquired by the neural net and express the same knowledge in a model that relies on hierarchical decisions instead, explaining a particular decision would be much easier. We describe a way of using a trained neural net to create a type of soft decision tree that generalizes better than one learned directly from the training data.

**PDF link:** [http://www.rctn.org/bruno/public/papers/Fukushima1980.pdf](http://www.rctn.org/bruno/public/papers/Fukushima1980.pdf "http://www.rctn.org/bruno/public/papers/Fukushima1980.pdf")

**Task:** Implement the architecture in python using Tensorflow, Pytorch, MXNet or NumPy. Train the network on MNIST and FashionMNIST.