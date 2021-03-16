---
layout: post
author:
  name: Paper ID 26
  difficulty: Medium
share: true
title: Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel
  Convolutional Neural Network
categories:
- CNN
- Pixel Shuffle
tags: []

---
**Abstract** - Recently, several models based on deep neural networks have achieved great success in terms of both reconstruction accuracy and computational performance for single image super-resolution. In these methods, the low resolution (LR) input image is upscaled to the high resolution (HR) space using a single filter, commonly bicubic interpolation, before reconstruction. This means that the super-resolution (SR) operation is performed in HR space. We demonstrate that this is sub-optimal and adds computational complexity. In this paper, we present the first convolutional neural network (CNN) capable of real-time SR of 1080p videos on a single K2 GPU. To achieve this, we propose a novel CNN architecture where the feature maps are extracted in the LR space. In addition, we introduce an efficient sub-pixel convolution layer which learns an array of upscaling filters to upscale the final LR feature maps into the HR output. By doing so, we effectively replace the handcrafted bicubic filter in the SR pipeline with more complex upscaling filters specifically trained for each feature map, whilst also reducing the computational complexity of the overall SR operation. We evaluate the proposed approach using images and videos from publicly available datasets and show that it performs significantly better (+0.15dB on Images and +0.39dB on Videos) and is an order of magnitude faster than previous CNN-based methods.

**Paper** - [https://arxiv.org/pdf/1609.05158v2.pdf](https://arxiv.org/pdf/1609.05158v2.pdf "https://arxiv.org/pdf/1609.05158v2.pdf")

**Dataset -** [https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/ "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/")