---
layout: post
share: true
title: Maxout Networks
date: 2018-03-25 23:35:37 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- General Deep Learning
tags:
- Theory
- Medium
---
**Abstract:** We consider the problem of designing models to leverage a recently introduced approximate model averaging technique called dropout. We define a simple new model called maxout (so named because its output is the max of a set of inputs, and because it is a natural companion to dropout) designed to both facilitate optimization by dropout and improve the accuracy of dropout’s fast approximate model averaging technique. We empirically verify that the model successfully accomplishes both of these tasks. We use maxout and dropout to demonstrate state of the art classification performance on four benchmark datasets: MNIST, CIFAR-10, CIFAR100, and SVHN.

**Paper Link:** [https://arxiv.org/pdf/1302.4389.pdf](https://arxiv.org/pdf/1302.4389.pdf "https://arxiv.org/pdf/1302.4389.pdf")

**Task:** Implement the given method using **NumPy**. The submitted code would be checked for similarity with the implementations available online. Show results on MNIST and FashionMNIST using a multi-layer perception.