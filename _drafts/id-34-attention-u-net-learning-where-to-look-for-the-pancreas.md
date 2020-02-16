---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_34] Attention U-Net: Learning Where to Look for the Pancreas"
categories:
- cnn
- computer vision
- attention
tags:
- hard

---
**Abstract:** We propose a novel attention gate (AG) model for medical imaging that automatically learns to focus on target structures of varying shapes and sizes. Models trained with AGs implicitly learn to suppress irrelevant regions in an input image while highlighting salient features useful for a specific task. This enables us to eliminate the necessity of using explicit external tissue/organ localisation modules of cascaded convolutional neural networks (CNNs). AGs can be easily integrated into standard CNN architectures such as the U-Net model with minimal computational overhead while increasing the model sensitivity and prediction accuracy. The proposed Attention U-Net architecture is evaluated on two large CT abdominal datasets for multi-class image segmentation. Experimental results show that AGs consistently improve the prediction performance of U-Net across different datasets and training sizes while preserving computational efficiency. The code for the proposed architecture is publicly available.

***

**Task:**

1. Implement the network architecture
2. Try and replciate the results on the relevant metrics in the paper

**Dataset:**

[https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT](https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT "https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT")