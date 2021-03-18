---
layout: post
author:
  name: Paper ID 7
  difficulty: Hard
share: true
title: FairMOT:-On-the-Fairness-of-Detection-and-Re-Identification-in-Multiple-Object-Tracking
categories:
- object tracking
tags: []

---
**Abstract** - There has been remarkable progress on object detection and re-identification (re-ID) in recent years which are the key components of multi-object tracking. However, little attention has been focused on jointly accomplishing the two tasks in a single network. Our study shows that the previous attempts ended up with degraded accuracy mainly because the re-ID task is not fairly learned which causes many identity switches. The unfairness lies in two-fold: (1) they treat re-ID as a secondary task whose accuracy heavily depends on the primary detection task. So training is largely biased to the detection task but ignores the re-ID task; (2) they use ROI-Align to extract re-ID features which is directly borrowed from object detection. However, this introduces a lot of ambiguity in characterizing objects because many sampling points may belong to disturbing instances or background. To solve the problems, we present a simple approach FairMOT which consists of two homogeneous branches to predict pixel-wise objectness scores and re-ID features. The achieved fairness between the tasks allows FairMOT to obtain high levels of detection and tracking accuracy and outperform previous state-of-the-arts by a large margin on several public datasets

**Paper** - [https://arxiv.org/pdf/2004.01888v5.pdf](https://arxiv.org/pdf/2004.01888v5.pdf)

**Dataset -** [https://motchallenge.net/data/mot20/](https://motchallenge.net/data/mot20/)
    