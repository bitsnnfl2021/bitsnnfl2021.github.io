---
layout: post
share: true
title: "[ID_64 r] Harmonic Convolutional Networks based on Discrete Cosine Transform"
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
categories:
- Edge Detection
- Image Classification
- Object Detection
- Faster R-CNN
tags: []

---
Abstract—Convolutional neural networks (CNNs) learn filters in order to capture local correlation patterns in feature space. In this paper, we propose to revert to learning combinations of preset spectral filters by switching to CNNs with harmonic blocks. We rely on the use of the Discrete Cosine Transform (DCT) filters which have excellent energy compaction properties and are widely used for image compression. The proposed harmonic blocks rely on DCT-modeling and replace conventional convolutional layers to produce partially or fully harmonic versions of new or existing CNN architectures. We demonstrate how the harmonic networks can be efficiently compressed in a straightforward manner by truncating high-frequency information in harmonic blocks which is possible due to the redundancies in the spectral domain. We report extensive experimental validation demonstrating the benefits of the introduction of harmonic blocks into state-of-the-art CNN models in image classification, segmentation and edge detection applications. Index Terms—Harmonic Network, Convolutional Neural Networks, Discrete Cosine Transform, Image Classification, Object Detection, Edge Detection.

Paper Link: [https://arxiv.org/pdf/2001.06570v1.pdf](https://arxiv.org/pdf/2001.06570v1.pdf "https://arxiv.org/pdf/2001.06570v1.pdf")

Tasks:

1. Train Faster R-CNN model based on harmonic ResNets mentioned in the paper for Object Detection and Segmentation on Pascal VOC (Topic 5 in the paper).
2. Implement a proper data-loader with any 2 data augmentation techniques.
3. Implementation is to be done in Tensorflow.
4. Show results in mAP (mean Average Precision).

ID: 64