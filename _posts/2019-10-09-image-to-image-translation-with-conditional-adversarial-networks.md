---
layout: post
share: true
title: 'Image-to-Image Translation with Conditional Adversarial Networks (Pix2Pix) (Paper ID: 41)'
author:
  name: Parth Patel
  email: f2016150@pilani.bits-pilani.ac.in
categories:
- Unsupervised Learning
- GANs
tags:
- Medium
date: 2019-10-09 09:22:38 +0000

---
**Abstract:** We investigate conditional adversarial networks as a general-purpose solution to image-to-image translation problems. These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping. This makes it possible to apply the same generic approach to problems that traditionally would require very different loss formulations. We demonstrate that this approach is effective at synthesizing photos from label maps, reconstructing objects from edge maps, and colorizing images, among other tasks. Indeed, since the release of the pix2pix software associated with this paper, a large number of internet users (many of them artists) have posted their own experiments with our system, further demonstrating its wide applicability and ease of adoption without the need for parameter tweaking. As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either.

**Paper Link:** [https://arxiv.org/abs/1611.07004](https://arxiv.org/abs/1611.07004 "https://arxiv.org/abs/1611.07004")

**Paper ID: 41**

**Guidelines:**

1. Read the paper thoroughly and understand all the concepts (like conditional GANs, generator's architecture and its analysis, discriminator's architecture and its analysis, choice of objective function and its analysis),  therein (including the Appendix). **This is one of the best written papers till date.**
2. For the generator, you need to implement only the U-Net Architecture as described in the paper (see Appendix). No need to implement the encoder-decoder architecture.
3. For the discriminator, implement the 70x70 PatchGAN architecture as specified in the paper (see Appendix).
4. The loss function to be used is specified by equation 4 in the paper, with minor changes as specified in section 3.3.
5. Train a GAN model on any one dataset of your choice (from among the ones mentioned in section 4) and show the resulting images generated. You can use Tensorflow, PyTorch or Keras.

**Side Notes:**
1. For introduction to GANs, refer [https://medium.com/@jonathan_hui/gan-whats-generative-adversarial-networks-and-its-application-f39ed278ef09](https://medium.com/@jonathan_hui/gan-whats-generative-adversarial-networks-and-its-application-f39ed278ef09) .
