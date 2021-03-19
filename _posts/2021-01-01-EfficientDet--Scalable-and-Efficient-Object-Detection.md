---
layout: post
author:
  name: Paper ID 30
  difficulty: Medium
share: true
title: EfficientDet- Scalable and Efficient Object Detection
categories:
- Object Detection
- Computer Vision
- medium

tags: []

---
**Abstract** - Model efficiency has become increasingly important incomputer vision. In this paper, we systematically study neu-ral network architecture design choices for object detectionand propose several key optimizations to improve efficiency.First, we propose a weighted bi-directional feature pyra-mid network (BiFPN), which allows easy and fast multi-scale feature fusion; Second, we propose a compound scal-ing method that uniformly scales the resolution, depth, andwidth for all backbone, feature network, and box/class pre-diction networks at the same time. Based on these optimiza-tions and better backbones, we have developed a new familyof object detectors, called EfficientDet, which consistentlyachieve much better efficiency than prior art across a widespectrum of resource constraints. In particular, with single-model and single-scale, our EfficientDet-D7 achieves state-of-the-art55.1 APon COCOtest-devwith 77M param-eters and 410B FLOPs1, being4x – 9xsmaller and using13x – 42xfewer FLOPs than previous detectors.

**Paper** - [https://arxiv.org/pdf/1911.09070.pdf](https://arxiv.org/pdf/1911.09070.pdf)

**Dataset -** [https://cocodataset.org/#download](https://cocodataset.org/#download)
    