---
layout: post
author:
  name: Paper ID 64
  difficulty: Medium
share: true
title: 'DualGAN: Unsupervised Dual Learning for Image-to-Image Translation'
categories:
- GAN
- Computer Vision
- CNN
- Image to Image Translation
tags: []

---
**Abstract** - Conditional Generative Adversarial Networks (GANs) for cross-domain image-to-image translation have made much progress recently. Depending on the task complexity, thousands to millions of labeled image pairs are needed to train a conditional GAN. However, human labeling is expensive, even impractical, and large quantities of data may not always be available. Inspired by dual learning from natural language translation, we develop a novel dual-GAN mechanism, which enables image translators to be trained from two sets of unlabeled images from two domains. In our architecture, the primal GAN learns to translate images from domain U to those in domain V, while the dual GAN learns to invert the task. The closed loop made by the primal and dual tasks allows images from either domain to be translated and then reconstructed. Hence a loss function that accounts for the reconstruction error of images can be used to train the translators. Experiments on multiple image translation tasks with unlabeled data show considerable performance gain of DualGAN over a single GAN. For some tasks, DualGAN can even achieve comparable or slightly better results than conditional GAN trained on fully labeled data.

**Paper** - [https://arxiv.org/abs/1704.02510](https://arxiv.org/abs/1704.02510 "https://arxiv.org/abs/1704.02510")

**Dataset -** [http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/](http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/ "http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/") (maps dataset)