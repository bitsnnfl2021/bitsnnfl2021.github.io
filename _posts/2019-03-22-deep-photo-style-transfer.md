---
layout: post
share: true
title: Deep Photo Style Transfer
author:
  name: Harsh Jaiswal
  email: f2015525@pilani.bits-pilani.ac.in
categories:
- Computer Vision
tags:
- Medium
date: 2019-03-22 16:01:30 +0000

---
**Abstract:** This paper introduces a deep-learning approach to photographic style transfer that handles a large variety of image content while faithfully transferring the reference style. Our approach builds upon the recent work on painterly transfer that separates style from the content of an image by considering different layers of a neural network. However, as is, this approach is not suitable for photorealistic style transfer. Even when both the input and reference images are photographs, the output still exhibits distortions reminiscent of a painting. Our contribution is to constrain the transformation from the input to the output to be locally affine in colorspace, and to express this constraint as a custom fully differentiable energy term. We show that this approach successfully suppresses distortion and yields satisfying photorealistic style transfers in a broad variety of scenarios, including transfer of the time of day, weather, season, and artistic edits.

**Paper Link:** [https://arxiv.org/pdf/1703.07511v1.pdf](https://arxiv.org/pdf/1703.07511v1.pdf "https://arxiv.org/pdf/1703.07511v1.pdf")

**Paper ID: 54**

**Guidelines:** 

1. Implement only the algorithm prescribed by the paper no need to do comparison with other algorithms
2. Implement the paper using Keras framework.