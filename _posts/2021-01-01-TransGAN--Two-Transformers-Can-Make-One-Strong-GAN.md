---
layout: post
author:
  name: Paper ID 60
  difficulty: Difficulty - Medium
share: true
title: TransGAN- Two Transformers Can Make One Strong GAN
categories:
- Transformers
- GAN
- Image Generation
- medium

tags: []

---
**Abstract** - The recent explosive interest on transformers has suggested their potential to become powerful "universal" models for computer vision tasks, such as classification, detection, and segmentation. However, how further transformers can go - are they ready to take some more notoriously difficult vision tasks, e.g., generative adversarial networks (GANs)? Driven by that curiosity, we conduct the first pilot study in building a GAN \textbf{completely free of convolutions}, using only pure transformer-based architectures. Our vanilla GAN architecture, dubbed \textbf{TransGAN}, consists of a memory-friendly transformer-based generator that progressively increases feature resolution while decreasing embedding dimension, and a patch-level discriminator that is also transformer-based. We then demonstrate TransGAN to notably benefit from data augmentations (more than standard GANs), a multi-task co-training strategy for the generator, and a locally initialized self-attention that emphasizes the neighborhood smoothness of natural images. Equipped with those findings, TransGAN can effectively scale up with bigger models and high-resolution image datasets. Specifically, our best architecture achieves highly competitive performance compared to current state-of-the-art GANs based on convolutional backbones. Specifically, TransGAN sets \textbf{new state-of-the-art} IS score of 10.10 and FID score of 25.32 on STL-10. It also reaches competitive 8.64 IS score and 11.89 FID score on Cifar-10, and 12.23 FID score on CelebA 64×64, respectively. We also conclude with a discussion of the current limitations and future potential of TransGAN.

**Paper** - [https://arxiv.org/abs/2102.07074v2](https://arxiv.org/abs/2102.07074v2)

**Dataset -** [https://cs.stanford.edu/~acoates/stl10/ ](https://cs.stanford.edu/~acoates/stl10/ )

[ https://www.cs.toronto.edu/~kriz/cifar.html]( https://www.cs.toronto.edu/~kriz/cifar.html)
    