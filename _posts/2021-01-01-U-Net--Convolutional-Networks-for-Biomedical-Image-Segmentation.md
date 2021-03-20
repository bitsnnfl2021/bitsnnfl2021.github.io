---
layout: post
author:
  name: Paper ID 14
  difficulty: Difficulty - Easy
share: true
title: U-Net- Convolutional Networks for Biomedical Image Segmentation
categories:
- Segmentation
- Computer Vision
- easy

tags: []

---
**Abstract** - There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU. The full implementation (based on Caffe) and the trained networks are available at this http URL . 

**Paper** - [https://arxiv.org/pdf/1505.04597v1.pdf](https://arxiv.org/pdf/1505.04597v1.pdf)

**Dataset -** [http://brainiac2.mit.edu/isbi_challenge/home](http://brainiac2.mit.edu/isbi_challenge/home)
    