---
layout: post
author:
  name: Paper ID 97
  difficulty: Hard
share: true
title: Label-Noise Robust Generative Adversarial Networks
categories:
- GAN
- Text-to-Image
tags: []

---
**Abstract** - Generative adversarial networks (GANs) are a frame- work that learns a generative distribution through adver- sarial training. Recently, their class conditional exten- sions (e.g., conditional GAN (cGAN) and auxiliary classi- fier GAN (AC-GAN)) have attracted much attention owing to their ability to learn the disentangled representations and to improve the training stability. However, their training re- quires the availability of large-scale accurate class-labeled data, which are often laborious or impractical to collect in a real-world scenario. To remedy this, we propose a novel family of GANs called label-noise robust GANs (rGANs), which, by incorporating a noise transition model, can learn a clean label conditional generative distribution even when training labels are noisy. In particular, we propose two variants: rAC-GAN, which is a bridging model between AC-GAN and the label-noise robust classification model, and rcGAN, which is an extension of cGAN and solves this problem with no reliance on any classifier. In addition to providing the theoretical background, we demonstrate the effectiveness of our models through extensive experiments using diverse GAN configurations, various noise settings, and multiple evaluation metrics (in which we tested 402 conditions in total).

**Paper** - [https://openaccess.thecvf.com/content_CVPR_2019/papers/Kaneko_Label-Noise_Robust_Generative_Adversarial_Networks_CVPR_2019_paper.pdf](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kaneko_Label-Noise_Robust_Generative_Adversarial_Networks_CVPR_2019_paper.pdf "https://openaccess.thecvf.com/content_CVPR_2019/papers/Kaneko_Label-Noise_Robust_Generative_Adversarial_Networks_CVPR_2019_paper.pdf")

**Dataset** - [https://www.cs.toronto.edu/\~kriz/cifar.html](https://www.cs.toronto.edu/\~kriz/cifar.html "https://www.cs.toronto.edu/~kriz/cifar.html")