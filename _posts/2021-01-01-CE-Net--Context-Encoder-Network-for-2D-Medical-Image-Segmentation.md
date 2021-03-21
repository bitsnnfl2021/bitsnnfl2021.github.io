---
layout: post
author:
  name: Paper ID 10
  difficulty: Difficulty - Medium
share: true
title: CE-Net- Context Encoder Network for 2D Medical Image Segmentation
categories:
- Segmentation
- Object Detection
- Computer Vision
- medium

tags: []

---
**Abstract** - Abstract—Medical image segmentation is an important step
in medical image analysis. With the rapid development of
convolutional neural network in image processing, deep learning
has been used for medical image segmentation, such as optic
disc segmentation, blood vessel detection, lung segmentation, cell
segmentation, etc. Previously, U-net based approaches have been
proposed. However, the consecutive pooling and strided convolu-
tional operations lead to the loss of some spatial information. In
this paper, we propose a context encoder network (referred to as
CE-Net) to capture more high-level information and preserve
spatial information for 2D medical image segmentation. CE-
Net mainly contains three major components: a feature encoder
module, a context extractor and a feature decoder module. We
use pretrained ResNet block as the fixed feature extractor. The
context extractor module is formed by a newly proposed dense
atrous convolution (DAC) block and residual multi-kernel pooling
(RMP) block. We applied the proposed CE-Net to different 2D
medical image segmentation tasks. Comprehensive results show
that the proposed method outperforms the original U-Net method
and other state-of-the-art methods for optic disc segmentation,
vessel detection, lung segmentation, cell contour segmentation
and retinal optical coherence tomography layer segmentation.

**Paper** - [https://arxiv.org/pdf/1903.02740.pdf](https://arxiv.org/pdf/1903.02740.pdf)

**Dataset -** [https://drive.google.com/open?id=1vpcvvspgrfpnil932xgu3xc_wflusxjr](https://drive.google.com/open?id=1vpcvvspgrfpnil932xgu3xc_wflusxjr)
    