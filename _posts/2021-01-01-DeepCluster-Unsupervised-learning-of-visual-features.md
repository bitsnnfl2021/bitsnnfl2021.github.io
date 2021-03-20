---
layout: post
author:
  name: Paper ID 53
  difficulty: Medium
share: true
title: DeepCluster Unsupervised learning of visual features
categories:
- Unsupervised Learning
- Clustering
- medium

tags: []

---
**Abstract** - Clustering is a class of unsupervised learning methods that has been extensively applied and studied in computer vision. Little work has been done to adapt it to the end-to-end training of visual features on large scale datasets. In this work, we present DeepCluster, a clustering method that jointly learns the parameters of a neural network and the cluster assignments of the resulting features. DeepCluster iteratively groups the features with a standard clustering algorithm, k-means, and uses the subsequent assignments as supervision to update the weights of the network. We apply DeepCluster to the unsupervised training of convolutional neural networks on large datasets like ImageNet and YFCC100M. The resulting model outperforms the current state of the art by a significant margin on all the standard benchmarks.

**Paper** - [https://arxiv.org/abs/1807.05520](https://arxiv.org/abs/1807.05520)

**Dataset -** [http://image-net.org ](http://image-net.org )

[ http://projects.dfki.uni-kl.de/yfcc100m/]( http://projects.dfki.uni-kl.de/yfcc100m/)
    