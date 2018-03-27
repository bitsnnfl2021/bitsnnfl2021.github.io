---
layout: post
share: true
title: Cost-Effective Active Learning for Deep Image Classification
date: 2018-03-27 16:28:46 +0000
author:
  name: Shrikant Sharda
  email: f2014046@pilani.bits-pilani.ac.in
categories: []
tags: []
---
**Abstract:**

Recent successes in learning-based image classifi- cation, however, heavily rely on the large number of annotated training samples, which may require considerable human efforts. In this paper, we propose a novel active learning framework, which is capable of building a competitive classifier with optimal feature representation via a limited amount of labeled training instances in an incremental learning manner. Our approach ad- vances the existing active learning methods in two aspects. First, we incorporate deep convolutional neural networks into active learning. Through the properly designed framework, the feature representation and the classifier can be simultaneously updated with progressively annotated informative samples. Second, we present a cost-effective sample selection strategy to improve the classification performance with less manual annotations. Unlike traditional methods focusing on only the uncertain samples of low prediction confidence, we especially discover the large amount of high confidence samples from the unlabeled set for feature learn- ing. Specifically, these high confidence samples are automatically selected and iteratively assigned pseudo-labels. We thus call our framework “ Cost-Effective Active Learning” (CEAL) standing for the two advantages. Extensive experiments demonstrate that the proposed CEAL framework can achieve promising results on two challenging image classification datasets, i.e., face recognition on CACD database \[1\] and object categorization on Caltech-256 \[2\]. 

**Deliverables**: Active Learning algorithm implemented in Python and CNN implemented using TF/Pytorch. Use CACD Dataset which is publicly available. And show the accuracy vs % labelled samples graph. Can also use Caltech 256 if computation requirements for CACD are not met.

**Paper Link**: [https://arxiv.org/pdf/1701.03551.pdf](https://arxiv.org/pdf/1701.03551.pdf "https://arxiv.org/pdf/1701.03551.pdf")