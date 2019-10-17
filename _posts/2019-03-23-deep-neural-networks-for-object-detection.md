---
layout: post
share: true
title: 'Deep Neural Networks for Object Detection (Paper ID: 81)'
author:
  name: Sahil Ranadive
  email: f2016097@pilani.bits-pilani.ac.in
categories:
- Computer Vision
- Object Detection
tags:
- Medium
date: 2019-03-23 09:53:33 +0000

---
**Abstract:** Deep Neural Networks (DNNs) have recently shown outstanding performance on image classification tasks \[14\]. In this paper we go one step further and address the problem of object detection using DNNs, that is not only classifying but also precisely localizing objects of various classes. We present a simple and yet powerful formulation of object detection as a regression problem to object bounding box masks. We define a multi-scale inference procedure which is able to produce high-resolution object detections at a low cost by a few network applications. State-of-the-art performance of the approach is shown on Pascal VOC.

**Paper Link:** [http://papers.nips.cc/paper/5207-deep-neural-networks-for-object-detection.pdf](http://papers.nips.cc/paper/5207-deep-neural-networks-for-object-detection.pdf "http://papers.nips.cc/paper/5207-deep-neural-networks-for-object-detection.pdf")

**ID:** 81

**Guidelines:**

1. Implement the model architecture as given in the paper.
2. Train your model on Pascal VOC 2007 dataset.
3. As a debug step train your model on small number of examples (50-100) and see if your model is able to overfit on those examples.
4. Obtain the learning curves showing the validation and training loss after each epoch. Report your final results using a suitable metric.
