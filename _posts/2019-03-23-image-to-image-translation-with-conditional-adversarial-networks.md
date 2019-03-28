---
layout: post
share: true
title: 'Image-to-Image Translation with Conditional Adversarial Networks (Pix2Pix)
  (Paper ID: 41)'
author:
  name: Amit Tiwary
  email: f2015818@pilani.bits-pilani.ac.in
categories:
- Unsupervised Learning
- GANs
tags:
- Medium
date: 2019-03-23 09:21:38 +0000

---
**Abstract:** We investigate conditional adversarial networks as a general-purpose solution to image-to-image translation problems. These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping. This makes it possible to apply the same generic approach to problems that traditionally would require very different loss formulations. We demonstrate that this approach is effective at synthesizing photos from label maps, reconstructing objects from edge maps, and colorizing images, among other tasks. Indeed, since the release of the pix2pix software associated with this paper, a large number of internet users (many of them artists) have posted their own experiments with our system, further demonstrating its wide applicability and ease of adoption without the need for parameter tweaking. As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either.

**Paper Link:** [https://arxiv.org/abs/1611.07004](https://arxiv.org/abs/1611.07004 "https://arxiv.org/abs/1611.07004")

**Paper ID: 41**

**Guidelines:**

1. Read the paper thoroughly and understand the all the concepts therein (including the Appendix). This is one of the best written papers till date.
2. Implement only the U-Net Architecture for the Generator as described in the paper.
3. The loss function MUST be conditioned on the input. Don't use just the L1or L2 loss.
4. Train two models on **TWO different datasets** and show the resulting images generated.