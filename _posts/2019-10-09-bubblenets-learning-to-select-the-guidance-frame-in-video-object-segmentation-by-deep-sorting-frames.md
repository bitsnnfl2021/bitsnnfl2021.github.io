---
layout: post
share: true
title: 'BubbleNets: Learning to Select the Guidance Frame in Video Object Segmentation by Deep Sorting Frames (Paper ID: 151)'
author:
  name: Saksham Consul
  email: f2016424@pilani.bits-pilani.ac.in
categories:
- Computer Vision
tags:
- Hard
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Semi-supervised video object segmentation has made significant progress on real and challenging videos in recent years. The current paradigm for segmentation methods and benchmark datasets is to segment objects in video provided a single annotation in the first frame. However, we find that segmentation performance across the entire video varies dramatically when selecting an alternative frame for annotation. This paper address the problem of learning to suggest the single best frame across the video for user annotation—this is, in fact, never the first frame of video. We achieve this by introducing BubbleNets, a novel deep sorting network that learns to select frames using a performance-based loss function that enables the conversion of expansive amounts of training examples from already existing datasets. Using BubbleNets, we are able to achieve an 11% relative improvement in segmentation performance on the DAVIS benchmark without any changes to the underlying method of segmentation

**Paper Link:** [https://arxiv.org/pdf/1903.11779.pdf](https://arxiv.org/pdf/1903.11779.pdf)

**ID:** 151

**Guidelines:**

1. Implement the neural network
2. Implement the deep bubble sort algorithm
3. Replicate results in the paper

**Dataset Link**: [https://davischallenge.org/](https://davischallenge.org/)

