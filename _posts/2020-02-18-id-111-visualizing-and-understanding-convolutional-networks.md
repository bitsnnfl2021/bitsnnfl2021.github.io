---
layout: post
author:
  name: 'Paper ID: 111'
  email: bitsnnfl@gmail.com
share: true
title: Visualizing and Understanding Convolutional Networks
categories:
- CNN
tags: []

---
**Abstract -** Large Convolutional Network models have recently demonstrated impressive classification performance on the ImageNet benchmark Krizhevsky et al. \[18\]. However, there is no clear understanding of why they perform so well, or how they might be improved. In this paper, we explore both issues. We introduce a novel visualization technique that gives insight into the function of intermediate feature layers and the operation of the classifier. Used in a diagnostic role, these visualizations allow us to find model architectures that outperform Krizhevsky et al. on the ImageNet classification benchmark. We also perform an ablation study to discover the performance contribution from different model layers. We show our ImageNet model generalizes well to other datasets: when the softmax classifier is retrained, it convincingly beats the current state-of-the-art results on Caltech-101 and Caltech-256 datasets.

**Paper** - [https://arxiv.org/pdf/1311.2901.pdf](https://arxiv.org/pdf/1311.2901.pdf "https://arxiv.org/pdf/1311.2901.pdf")

**Dataset** - [http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#data](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#data "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#data")

**Problem Statement** - 

1. Implement the model on VOC2012 dataset mentioned in the link above.
2. Implement the model with a different loss function so that it can detect multiple objects in the same image.
3. Choice of the loss function has to be justified, either on a mathematical basis or experimental basis.