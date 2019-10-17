---
layout: post
share: true
title: 'U-Net: Convolutional Networks for Biomedical Image Segmentation (Paper ID:
  95)'
author:
  name: Parth Patel
  email: f2016150@pilani.bits-pilani.ac.in
categories:
- CNN
- Computer Vision
- Image Segmentation
tags:
- Medium
date: 2019-10-09 09:07:08 +0000

---
**Abstract:** There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU.

**Paper Link:** [https://arxiv.org/pdf/1505.04597.pdf](https://arxiv.org/pdf/1505.04597.pdf "https://arxiv.org/pdf/1505.04597.pdf")

1. Implement the U-Net architecture given in the paper using Keras.
2. Use Ultrasound Nerve Segmentation dataset([https://www.kaggle.com/c/ultrasound-nerve-segmentation/data](https://www.kaggle.com/c/ultrasound-nerve-segmentation/data)) or TGS Salt Identification Challenge dataset([https://www.kaggle.com/c/tgs-salt-identification-challenge/data](https://www.kaggle.com/c/tgs-salt-identification-challenge/data)), according to the amount of data that you can handle. This is different from the dataset mentioned in the paper.
3. Report the IoU object segmentation score on your validation dataset.

**Paper ID:** **95**
