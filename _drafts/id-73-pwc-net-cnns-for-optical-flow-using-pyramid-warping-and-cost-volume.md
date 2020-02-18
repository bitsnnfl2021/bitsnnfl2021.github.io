---
layout: post
author:
  name: 'Paper ID: 73'
  email: bitsnnfl@gmail.com
share: true
title: 'PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume'
categories:
- Optical Flow
- Warping
- Cost Volume
- Pyramidal Processing
- Dense Pixel Matching
tags: []

---
**Abstract:** We present a compact but effective CNN model for optical flow, called PWC-Net. PWC-Net has been designed according to simple and well-established principles: pyramidal processing, warping, and the use of a cost volume. Cast in a learnable feature pyramid, PWC-Net uses the current optical flow estimate to warp the CNN features of the second image. It then uses the warped features and features of the first image to construct a cost volume, which is processed by a CNN to estimate the optical flow. PWC-Net is 17 times smaller in size and easier to train than the recent FlowNet2 model. Moreover, it outperforms all published optical flow methods on the MPI Sintel final pass and KITTI 2015 benchmarks, running at about 35 fps on Sintel resolution (1024x436) images.

**Link to paper:** [https://arxiv.org/abs/1709.02371](https://arxiv.org/abs/1709.02371 "https://arxiv.org/abs/1709.02371")  
**Conference:** CVPR 2018

**Task:**

1)Implement the warping module

2)Implement the model in PyTorch using a custom data loader 

3)Use Sintel Dataset

4)Compare your results with the paper