---
layout: post
share: true
title: Deep Embedded Clustering
date: 2018-03-24 16:01:48 +0000
categories:
- General Deep Learning
- Unsupervised Learning
tags:
- Intermediate
- Theory
- Representation Learning
author:
  name: Satwik Bhattamishra
  email: satwik55@gmail.com
---
**Abstract:** Clustering is central to many data-driven application domains and has been studied extensively in terms of distance functions and grouping algorithms. Relatively little work has focused on learning representations for clustering. In this paper, we propose Deep Embedded Clustering (DEC), a method that simultaneously learns feature representations and cluster assignments using deep neural networks. DEC learns a mapping from the data space to a lower-dimensional feature space in which it iteratively optimizes a clustering objective. Our experimental evaluations on image and text corpora show significant improvement over state-of-the-art methods.

**Paper Link:** [https://arxiv.org/abs/1511.06335](https://arxiv.org/abs/1511.06335)

**Task:** Implement the deep embedded clustering method described in the paper in python using TensorFlow, Pytorch or MXNet. Test your implementation on MNIST dataset. 

**Brownie points:** Compare your result with AutoEncoder + K-means and try to get results similar to the one mentioned in the paper.