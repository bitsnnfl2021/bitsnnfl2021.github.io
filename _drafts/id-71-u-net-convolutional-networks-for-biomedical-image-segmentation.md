---
layout: post
share: true
title: "[ID:71]U-Net: Convolutional Networks for Biomedical Image Segmentation"
author:
  name: Team NNFL
  email: bitsnnfl.github.io
categories:
- CNN
- Semantic Segmentation
- Encoder-Decoder
tags: []

---
**Abstract:** There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for the segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU.

One of the few papers having a Wiki page([https://en.wikipedia.org/wiki/U-Net](https://en.wikipedia.org/wiki/U-Net "https://en.wikipedia.org/wiki/U-Net"))

**Paper Link:** [https://arxiv.org/pdf/1505.04597.pdf](https://arxiv.org/pdf/1505.04597.pdf "https://arxiv.org/pdf/1505.04597.pdf")

**Conference:** MICCAI 2015

**Task:**

1) Implement the proper data loader with any two augmentation techniques.

2)Implement the encoder-decoder architecture in a framework of your choice.

3)Add Skip Connections

4)Implement Shared Weights residual block

5)Calculate Precision and recall(Eventually calculating the F1-score)

6)Draw a ROC curve and compare your results with the paper.

**Dataset:** DRIVE

Register at ([https://drive.grand-challenge.org/DRIVE/](https://drive.grand-challenge.org/DRIVE/ "https://drive.grand-challenge.org/DRIVE/")) or download directly

[https://www.dropbox.com/sh/z4hbbzqai0ilqht/AAARqnQhjq3wQcSVFNR__6xNa?dl=0](https://www.dropbox.com/sh/z4hbbzqai0ilqht/AAARqnQhjq3wQcSVFNR__6xNa?dl=0 "https://www.dropbox.com/sh/z4hbbzqai0ilqht/AAARqnQhjq3wQcSVFNR__6xNa?dl=0")