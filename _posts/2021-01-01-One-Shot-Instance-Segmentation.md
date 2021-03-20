---
layout: post
author:
  name: Paper ID 36
  difficulty: Difficulty - Medium
share: true
title: One-Shot Instance Segmentation
categories:
- One-Short Learning
- Segmentation
- Computer Vision
- medium

tags: []

---
**Abstract** - We tackle the problem of one-shot instance segmentation: Given an example image of a novel, previously unknown object category, find and segment all objects of this category within a complex scene. To address this challenging new task, we propose Siamese Mask R-CNN. It extends Mask R-CNN by a Siamese backbone encoding both reference image and scene, allowing it to target detection and segmentation towards the reference category. We demonstrate empirical results on MS Coco highlighting challenges of the one-shot setting: while transferring knowledge about instance segmentation to novel object categories works very well, targeting the detection network towards the reference category appears to be more difficult. Our work provides a first strong baseline for one-shot instance segmentation and will hopefully inspire further research into more powerful and flexible scene analysis algorithms.

**Paper** - [https://arxiv.org/pdf/1811.11507v2.pdf](https://arxiv.org/pdf/1811.11507v2.pdf)

**Dataset -** [https://cocodataset.org/#download](https://cocodataset.org/#download)
    