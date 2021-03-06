---
layout: post
author:
  name: Paper ID 39
  difficulty: Difficulty - Medium
share: true
title: PULSE- Self-Supervised Photo Upsampling via Latent Space Exploration of Generative Models
categories:
- Computer Vision
- Image processing
- Generative Adversarial Networks
- medium

tags: []

---
**Abstract** - The primary aim of single-image super-resolution is to construct high-resolution (HR) images from corresponding low-resolution (LR) inputs. In previous approaches, which have generally been supervised, the training objective typically measures a pixel-wise average distance between the super-resolved (SR) and HR images. Optimizing such metrics often leads to blurring, especially in high variance (detailed) regions. We propose an alternative formulation of the super-resolution problem based on creating realistic SR images that downscale correctly. We present an algorithm addressing this problem, PULSE (Photo Upsampling via Latent Space Exploration), which generates high-resolution, realistic images at resolutions previously unseen in the literature. It accomplishes this in an entirely self-supervised fashion and is not confined to a specific degradation operator used during training, unlike previous methods (which require supervised training on databases of LR-HR image pairs). Instead of starting with the LR image and slowly adding detail, PULSE traverses the high-resolution natural image manifold, searching for images that downscale to the original LR image. This is formalized through the "downscaling loss," which guides exploration through the latent space of a generative model. By leveraging properties of high-dimensional Gaussians, we restrict the search space to guarantee realistic outputs. PULSE thereby generates super-resolved images that both are realistic and downscale correctly. We show proof of concept of our approach in the domain of face super-resolution (i.e., face hallucination). We also present a discussion of the limitations and biases of the method as currently implemented with an accompanying model card with relevant metrics. Our method outperforms state-of-the-art methods in perceptual quality at higher resolutions and scale factors than previously possible.

**Paper** - [https://arxiv.org/abs/2003.03808](https://arxiv.org/abs/2003.03808)

**Dataset -** [https://www.kaggle.com/lamsimon/celebahq](https://www.kaggle.com/lamsimon/celebahq)
    