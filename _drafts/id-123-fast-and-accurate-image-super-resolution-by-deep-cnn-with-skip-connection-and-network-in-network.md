---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID:123]Fast and Accurate Image Super Resolution by Deep CNN with Skip Connection
  and Network in Network"
categories:
- CNN
- Super Resolution
- Image Reconstruction
tags: []

---
**Abstract:** We propose a highly efficient and faster Single Image Super-Resolution (SISR) model with Deep Convolutional neural networks (Deep CNN). Deep CNN have recently shown that they have a significant reconstruction performance on single-image super-resolution. The current trend is using deeper CNN layers to improve performance. However, deep models demand larger computation resources and are not suitable for network edge devices like mobile, tablet and IoT devices. Our model achieves state-of-the-art reconstruction performance with at least 10 times lower calculation cost by Deep CNN with Residual Net, Skip Connection and Network in Network (DCSCN). A combination of Deep CNNs and Skip connection layers are used as a feature extractor for image features on both local and global areas. Parallelized 1x1 CNNs, like the one called Network in Network, are also used for image reconstruction. That structure reduces the dimensions of the previous layer’s output for faster computation with less information loss, and make it possible to process original images directly. Also we optimize the number of layers and filters of each CNN to significantly reduce the calculation cost. Thus, the proposed algorithm not only achievesstateof-the-art performance but also achieves faster and more efficient computation.

Paper Link: [https://arxiv.org/ftp/arxiv/papers/1707/1707.05425.pdf](https://arxiv.org/ftp/arxiv/papers/1707/1707.05425.pdf "https://arxiv.org/ftp/arxiv/papers/1707/1707.05425.pdf")

Conference :CVPR

**Task:**

1. Implement the CNN model discussed in paper in an framework other than PyTorch.
2. Show the Train and test the models for atleast two different datasets and do comparison on the basis of PSNR.

**Dataset** : Use any publicly available dataset with high quality images. You may use  [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/)