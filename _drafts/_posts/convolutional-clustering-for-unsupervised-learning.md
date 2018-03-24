---
layout: post
share: true
title: Convolutional Clustering for Unsupervised Learning
date: 2018-03-24 20:04:09 +0000
author:
  name: Satwik Bhattamishra
  email: satwik55@gmail.com
categories:
- General Deep Learning
- Unsupervised Learning
tags:
- Medium
- Image-Data
- Application
---
**Abstract:** The task of labeling data for training deep neural networks is daunting and tedious, requiring millions of labels to achieve the current state-of-the-art results. Such reliance on large amounts of labeled data can be relaxed by exploiting hierarchical features via unsupervised learning techniques. In this work, we propose to train a deep convolutional network based on an enhanced version of the k-means clustering algorithm, which reduces the number of correlated parameters in the form of similar filters, and thus increases test categorization accuracy. We call our algorithm convolutional k-means clustering. We further show that learning the connection between the layers of a deep convolutional neural network improves its ability to be trained on a smaller amount of labeled data. Our experiments show that the proposed algorithm outperforms other techniques that learn filters unsupervised. Specifically, we obtained a test accuracy of 74.1% on STL-10 and a test error of 0.5% on MNIST.

**Paper Link:** [https://arxiv.org/pdf/1511.06241.pdf](https://arxiv.org/pdf/1511.06241.pdf)

**Task:** Implement the described network architecture explained in the paper in python using TensorFlow, Numpy, Pytorch or MXNet. Test your implementation on MNIST or Basic MNIST dataset.