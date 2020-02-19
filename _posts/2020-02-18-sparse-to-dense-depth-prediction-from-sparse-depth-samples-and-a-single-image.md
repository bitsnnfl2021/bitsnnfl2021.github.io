---
layout: post
author:
  name: "101"
  email: bitsnnfl@gmail.com
share: true
title: 'Sparse-to-Dense: Depth Prediction from Sparse Depth Samples and a Single Image'
categories: []
tags: []

---
We consider the problem of dense depth prediction from a sparse set of depth measurements and a single RGB image. Since depth estimation from monocular images alone is inherently ambiguous and unreliable, to attain a higher level of robustness and accuracy, we introduce additional sparse depth samples, which are either acquired with a low-resolution depth sensor or computed via visual Simultaneous Localization and Mapping (SLAM) algorithms. We propose the use of a single deep regression network to learn directly from the RGB-D raw data and explore the impact of a number of depth samples on prediction accuracy. Our experiments show that, compared to using only RGB images, the addition of 100 spatially random depth samples reduces the prediction root-mean-square error by 50% on the NYU-Depth-v2 indoor dataset. It also boosts the percentage of reliable prediction from 59% to 92% on the KITTI dataset.

Just train on a small subset of KITTI.

Replace the feature extractor from RESNET-18 to VGGNet for KITTI

Use Nearest Neighbour upsampling instead of bilinear interpolation.

Use Uniform random sampling with depth points restricted in numbers to 20000.

Compare results with the paper.