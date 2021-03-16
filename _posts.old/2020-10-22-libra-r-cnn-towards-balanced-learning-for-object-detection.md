---
layout: post
author:
  name: Paper ID 75
  difficulty: Hard
share: true
title: 'Libra R-CNN: Towards Balanced Learning for Object Detection'
categories:
- CNN
- Computer Vision
- Deep Learning
- Object Detection
tags: []

---
**Abstract** - Compared with model architectures, the training process, which is also crucial to the success of detectors, has received relatively less attention in object detection. In this work, we carefully revisit the standard training practice of detectors, and find that the detection performance is often limited by the imbalance during the training process, which generally consists in three levels – sample level, feature level, and objective level. To mitigate the adverse effects caused thereby, we propose Libra R-CNN, a simple but effective framework towards balanced learning for object detection. It integrates three novel components: IoU-balanced sampling, balanced feature pyramid, and balanced L1 loss, respectively for reducing the imbalance at sample, feature, and objective level. Benefitted from the overall balanced design, Libra R-CNN significantly improves the detection performance. Without bells and whistles, it achieves 2.5 points and 2.0 points higher Average Precision (AP) than FPN Faster R-CNN and RetinaNet respectively on MSCOCO. 1 

**Paper** - [https://arxiv.org/pdf/1904.02701v1.pdf](https://arxiv.org/pdf/1904.02701v1.pdf "https://arxiv.org/pdf/1904.02701v1.pdf") 

**Dataset** - [https://cocodataset.org/#download](https://cocodataset.org/#download "https://cocodataset.org/#download")