---
layout: post
author:
  name: Paper ID 92
  difficulty: Hard
share: true
title: Multi-Object Tracking with Quadruplet Convolutional Neural Networks
categories:
- CNN
- Computer Vision
tags: []

---
**Abstract** - We propose Quadruplet Convolutional Neural Networks (Quad-CNN) for multi-object tracking, which learn to associate object detections across frames using quadruplet losses. The proposed networks consider target appearances together with their temporal adjacencies for data association. Unlike conventional ranking losses, the quadruplet loss enforces an additional constraint that makes temporally adjacent detections more closely located than the ones with large temporal gaps. We also employ a multi-task loss to jointly learn object association and bounding box regression for better localization. The whole network is trained end-to-end. For tracking, the target association is performed by minimax label propagation using the metric learned from the proposed network. We evaluate performance of our multi-object tracking algorithm on public MOT Challenge datasets, and achieve outstanding results.

**Paper** - [https://openaccess.thecvf.com/content_cvpr_2017/papers/Son_Multi-Object_Tracking_With_CVPR_2017_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2017/papers/Son_Multi-Object_Tracking_With_CVPR_2017_paper.pdf "https://openaccess.thecvf.com/content_cvpr_2017/papers/Son_Multi-Object_Tracking_With_CVPR_2017_paper.pdf")

**Dataset** - [https://motchallenge.net/data/2D_MOT_2015/](https://motchallenge.net/data/2D_MOT_2015/ "https://motchallenge.net/data/2D_MOT_2015/")