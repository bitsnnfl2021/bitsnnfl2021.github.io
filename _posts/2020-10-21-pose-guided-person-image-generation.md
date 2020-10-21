---
layout: post
author:
  name: Paper ID 16
  difficulty: Easy
share: true
title: Pose Guided Person Image Generation
categories:
- GAN
- Computer Vision
- Pose Estimation
tags: []

---
**Abstract** - This paper proposes the novel Pose Guided Person Generation Network (PG2 ) that allows to synthesize person images in arbitrary poses, based on an image of that person and a novel pose. Our generation framework PG2 utilizes the pose information explicitly and consists of two key stages: pose integration and image refinement. In the first stage the condition image and the target pose are fed into a U-Net-like network to generate an initial but coarse image of the person with the target pose. The second stage then refines the initial and blurry result by training a U-Net-like generator in an adversarial way. Extensive experimental results on both 128×64 re-identification images and 256×256 fashion photos show that our model generates high-quality person images with convincing details.

**Paper** - [https://arxiv.org/pdf/1705.09368.pdf](https://arxiv.org/pdf/1705.09368.pdf "https://arxiv.org/pdf/1705.09368.pdf")

**Dataset -** [https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view](https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view "https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view")