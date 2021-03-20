---
layout: post
author:
  name: Paper ID 45
  difficulty: Medium
share: true
title: You Only Look Once-Unified, Real-Time Object Detection
categories:
- Object Detection
- Computer Vision
- medium

tags: []

---
**Abstract** - We present YOLO, a new approach to object detection.Prior work on object detection repurposes classifiers to per-form detection. Instead, we frame object detection as a re-gression problem to spatially separated bounding boxes andassociated class probabilities. A single neural network pre-dicts bounding boxes and class probabilities directly fromfull images in one evaluation. Since the whole detectionpipeline is a single network, it can be optimized end-to-enddirectly on detection performance.Our unified architecture is extremely fast. Our baseYOLO model processes images in real-time at 45 framesper second. A smaller version of the network, Fast YOLO,processes an astounding 155 frames per second whilestill achieving double the mAP of other real-time detec-tors. Compared to state-of-the-art detection systems, YOLOmakes more localization errors but is less likely to predictfalse positives on background. Finally, YOLO learns verygeneral representations of objects. It outperforms other de-tection methods, including DPM and R-CNN, when gener-alizing from natural images to other domains like artwork

**Paper** - [https://homes.cs.washington.edu/~ali/papers/YOLO.pdf](https://homes.cs.washington.edu/~ali/papers/YOLO.pdf)

**Dataset -** [http://www.image-net.org/download](http://www.image-net.org/download)
    