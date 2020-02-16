---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID:124]OverFeat: Integrated Recognition, Localization and Detection using
  Convolutional Networks"
categories:
- Localization
- classification
- detection
- CNN
- OverFeat
tags: []

---
**Abstract :** We present an integrated framework for using Convolutional Networks for classification, localization and detection. We show how a multiscale and sliding window approach can be efficiently implemented within a ConvNet. We also introduce a novel deep learning approach to localization by learning to predict object boundaries. Bounding boxes are then accumulated rather than suppressed in order to increase detection confidence. We show that different tasks can be learned simultaneously using a single shared network. This integrated framework is the winner of the localization task of the ImageNet Large Scale Visual Recognition Challenge 2013 (ILSVRC2013) and obtained very competitive results for the detection and classifications tasks. In post-competition work, we establish a new state of the art for the detection task. Finally, we release a feature extractor from our best model called OverFeat.

Paper Link : [https://arxiv.org/pdf/1312.6229.pdf](https://arxiv.org/pdf/1312.6229.pdf "https://arxiv.org/pdf/1312.6229.pdf")

Conference : ICLR 2013

**Tasks**

1. Implement the proper dataloader with any 2 data augmentation techniques.
2. Build three different models as mentioned in the paper :
   * Classification
   * localisation
   * detection
3. For each model test them according to section 3.4, 4.4 and 5 respectively.
4. Calculate the mean average precision score for each model separately.

**Datasets** : Any dataset of your choice (please take a subset dataset of ImageNet if using ImageNet).