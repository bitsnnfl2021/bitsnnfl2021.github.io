---
layout: post
author:
  name: Paper ID 58
  difficulty: Medium
share: true
title: Pixel Deconvolutional Network
categories:
- Image Segmentation
- Computer Vision
tags: []

---
**Abstract** - Deconvolutional layers have been widely used in a variety of deep models for up-sampling, including encoder-decoder networks for semantic segmentation and deep generative models for unsupervised learning. One of the key limitations of deconvolutional operations is that they result in the so-called checkerboard problem. This is caused by the fact that no direct relationship exists among adjacent pixels on the output feature map. To address this problem, we propose the pixel deconvolutional layer (PixelDCL) to establish direct relationships among adjacent pixels on the up-sampled feature map. Our method is based on a fresh interpretation of the regular deconvolution operation. The resulting PixelDCL can be used to replace any deconvolutional layer in a plug-and-play manner without compromising the fully trainable capabilities of original models. The proposed PixelDCL may result in slight decrease in efficiency, but this can be overcome by an implementation trick. Experimental results on semantic segmentation demonstrate that PixelDCL can consider spatial features such as edges and shapes and yields more accurate segmentation outputs than deconvolutional layers. When used in image generation tasks, our PixelDCL can largely overcome the checkerboard problem suffered by regular deconvolution operations.

**Paper** - [https://arxiv.org/abs/1705.06820](https://arxiv.org/abs/1705.06820 "https://arxiv.org/abs/1705.06820")

**Dataset -** [https://www.kaggle.com/huanghanchina/pascal-voc-2012](https://www.kaggle.com/huanghanchina/pascal-voc-2012 "https://www.kaggle.com/huanghanchina/pascal-voc-2012")