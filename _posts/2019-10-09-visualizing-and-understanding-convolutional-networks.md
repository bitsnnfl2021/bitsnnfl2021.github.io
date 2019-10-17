---
layout: post
share: true
title: 'Visualizing and Understanding Convolutional Networks (Paper ID: 181)'
author:
  name: Smith Shah
  email: f2016039@pilani.bits-pilani.ac.in
categories:
- CNN
- Computer Vision
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Large Convolutional Network models have recently demonstrated impressive classification performance on the ImageNet benchmark (Krizhevsky et al., 2012). However there is no clear understanding of why they perform so well, or how they might be improved. In this paper we address both issues. We introduce a novel visualization technique that gives insight into the function of intermediate feature layers and the operation of the classifier. Used in a diagnostic role, these visualizations allow us to find model architectures that outperform Krizhevsky et al. on the ImageNet classification benchmark. We also perform an ablation study to discover the performance contribution from different model layers. We show our ImageNet model generalizes well to other datasets: when the softmax classifier is retrained, it convincingly beats the current state-of-the-art results on Caltech-101 and Caltech-256 datasets.

**Paper Link:** [https://arxiv.org/pdf/1311.2901.pdf](https://arxiv.org/pdf/1311.2901.pdf)

**ID:** 181

**Guidelines:**

1. Visualize the pre-trained alexnet feature maps using deconvnet.
2. Modify the alexnet architecture as mentioned in section 4.1 and visualize the new model alongside the pretrained alexnet as shown in Fig. 6 using deconvnet.
3. Also, try to replicate the single model results mentioned in section 5.1. Ignore the rest of section 5.1.
4. No need to reproduce the results on other datasets as mentioned in section 5.2, 5.3.
5. Use the ImageNet 2012 dataset.

Bonus: Ablation studies in Section 4.2 and 4.3.

Useful Links: https://medium.com/coinmonks/paper-review-of-zfnet-the-winner-of-ilsvlc-2013-image-classification-d1a5a0c45103

**Dataset Link**: [http://image-net.org](http://image-net.org)

