---
layout: post
author:
  name: Rishav
  email: bitsnnfl@gmail.com
share: true
title: 'PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume'
categories:
- Deep Learning
- " Optical Flow"
tags: []

---
We present a compact but effective CNN model for optical flow, called PWC-Net. PWC-Net has been designed according to simple and well-established principles: pyramidal processing, warping, and the use of a cost volume. Cast in a learnable feature pyramid, PWC-Net uses the current optical flow estimate to warp the CNN features of the second image. It then uses the warped features and features of the first image to construct a cost volume, which is processed by a CNN to estimate the optical flow. PWCNet is 17 times smaller in size and easier to train than the recent FlowNet2 model. Moreover, it outperforms all published optical flow methods on the MPI Sintel final pass and KITTI 2015 benchmarks, running at about 35 fps on Sintel resolution (1024×436) images.

Replace the feature extractor used in the paper with an FPN and use the decoder features thereafter for the final training.

Train just on KITTI 2015 optical flow dataset. It is publicly available.

Paper: [https://arxiv.org/pdf/1709.02371.pdf](https://arxiv.org/pdf/1709.02371.pdf "https://arxiv.org/pdf/1709.02371.pdf")