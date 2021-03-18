---
layout: post
author:
  name: Paper ID 9
  difficulty: Medium
share: true
title: One-Shot-Object-Detection-with-Co-Attention-and-Co-Excitation
categories:
- one-shot object detection
tags: []

---
**Abstract** - This paper aims to tackle the challenging problem of one-shot object detection. Given a query image patch whose class label is not included in the training data, the goal of the task is to detect all instances of the same class in a target image. To this end, we develop a novel co-attention and co-excitation (CoAE) framework that makes contributions in three key technical aspects. First, we propose to use the nonlocal operation to explore the co-attention embodied in each query-target pair and yield region proposals accounting for the one-shot situation. Second, we formulate a squeeze-and-co-excitation scheme that can adaptively emphasize correlated feature channels to help uncover relevant proposals and eventually the target objects. Third, we design a margin-based ranking loss for implicitly learning a metric to predict the similarity of a region proposal to the underlying query, no matter its class label is seen or unseen in training. The resulting model is therefore a two-stage detector that yields a strong baseline on both VOC and MS-COCO under one-shot setting of detecting objects from both seen and never-seen classes.

**Paper** - [https://arxiv.org/pdf/1911.12529v1.pdf](https://arxiv.org/pdf/1911.12529v1.pdf)

**Dataset -** [https://cocodataset.org/#download](https://cocodataset.org/#download)
    