---
layout: post
share: true
title: 'Focal Loss for Dense Object Detection (Paper ID: 182)'
author:
  name: Smith Shah
  email: f2016039@pilani.bits-pilani.ac.in
categories:
- Object Detection
- Computer Vision
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** The highest accuracy object detectors to date are based on a two-stage approach popularized by R-CNN, where a classifier is applied to a sparse set of candidate object locations. In contrast, one-stage detectors that are applied over a regular, dense sampling of possible object locations have the potential to be faster and simpler, but have trailed the accuracy of two-stage detectors thus far. In this paper, we investigate why this is the case. We discover that the extreme foreground-background class imbalance encountered during training of dense detectors is the central cause. We propose to address this class imbalance by reshaping the standard cross entropy loss such that it down-weights the loss assigned to well-classified examples. Our novel Focal Loss focuses training on a sparse set of hard examples and prevents the vast number of easy negatives from overwhelming the detector during training. To evaluate the effectiveness of our loss, we design and train a simple dense detector we call RetinaNet. Our results show that when trained with the focal loss, RetinaNet is able to match the speed of previous one-stage detectors while surpassing the accuracy of all existing state-of-the-art two-stage detectors.

**Paper Link:** [https://arxiv.org/pdf/1708.02002.pdf](https://arxiv.org/pdf/1708.02002.pdf)

**ID:** 182

**Guidelines:**

1. Implement the proposed architecture that gives the best results and train it on the MS COCO dataset as mentioned in the paper.
2. As a debug step train your model on a small number of examples (50-100) and see if your model is able to overfit on those examples.
3. Obtain the learning curves showing the validation and training loss after each epoch. Report your final results in the form of the Average Precision(AP) metric and Intersection over Union(IoU) as mentioned in the paper.

(Bonus): Comparison with other variants like OHEM or other models.

**Dataset Link**: [http://cocodataset.org/#home](http://cocodataset.org/#home)
