---
layout: post
share: true
title: 'Fully Convolutional Networks for Semantic Segmentation (Paper ID: 85)'
author:
  name: Sanskriti Sharma
  email: f2015553@pilani.bits-pilani.ac.in
categories:
- Image Segmentation
- CNN
- FCN
tags:
- Medium
date: 2019-03-23 10:28:34 +0000

---
**Abstract:** Convolutional networks are powerful visual models that yield hierarchies of features. We show that convolutional networks by themselves, trained end-to-end, pixelsto-pixels, exceed the state-of-the-art in semantic segmentation. Our key insight is to build “fully convolutional” networks that take input of arbitrary size and produce correspondingly-sized output with efficient inference and learning. We define and detail the space of fully convolutional networks, explain their application to spatially dense prediction tasks, and draw connections to prior models. We adapt contemporary classification networks (AlexNet \[20\], the VGG net \[31\], and GoogLeNet \[32\]) into fully convolutional networks and transfer their learned representations by fine-tuning \[3\] to the segmentation task. We then define a skip architecture that combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations. Our fully convolutional network achieves stateof-the-art segmentation of PASCAL VOC (20% relative improvement to 62.2% mean IU on 2012), NYUDv2, and SIFT Flow, while inference takes less than one fifth of a second for a typical image.

**Link:** [https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf "https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf")

**ID**: 85

**Guidelines**:

1. Implement the architecture for fully convolutionalized classifiers on the VGG-16 net.
2. Train the network on the Pascal VOC 2012 dataset.
3. Implement the skip architecture as described in section 4.2 and depict improvement in results obtained.