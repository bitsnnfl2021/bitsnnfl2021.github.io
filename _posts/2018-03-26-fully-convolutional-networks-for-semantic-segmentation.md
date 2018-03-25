---
layout: post
share: true
title: Fully Convolutional Networks for Semantic Segmentation
date: 2018-03-26 00:09:46 +0000
author:
  name: Nikhil Vinta Sharma
  email: nikhilvs999@gmail.com
categories:
- Computer Vision
tags:
- Medium
- Application
---
**Abstract:** Convolutional networks are powerful visual models that yield hierarchies of features. We show that convolutional networks by themselves, trained end-to-end, pixelsto-pixels, exceed the state-of-the-art in semantic segmentation. Our key insight is to build “fully convolutional” networks that take input of arbitrary size and produce correspondingly-sized output with efficient inference and learning. We define and detail the space of fully convolutional networks, explain their application to spatially dense prediction tasks, and draw connections to prior models. We adapt contemporary classification networks (AlexNet, the VGG net, and GoogLeNet) into fully convolutional networks and transfer their learned representations by fine-tuning \[4\] to the segmentation task. We then define a novel architecture that combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations. Our fully convolutional network achieves state-of-the-art segmentation of PASCAL VOC (20% relative improvement to 62.2% mean IU on 2012), NYUDv2, and SIFT Flow, while inference takes less than one fifth of a second for a typical image.   

**Paper Link:** [https://arxiv.org/pdf/1411.4038v2.pdf](https://arxiv.org/pdf/1411.4038v2.pdf "https://arxiv.org/pdf/1411.4038v2.pdf")

**Task:** Focus on implementing the CNN using Tensorflow/PyTorch. Use VGG-16 only instead of using all three CNNs. Report graphs of loss function obtained by your code as well as the one in the paper.