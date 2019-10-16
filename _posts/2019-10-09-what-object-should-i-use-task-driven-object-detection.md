---
layout: post
share: true
title: 'What Object Should I Use? - Task Driven Object Detection (Paper ID: 162)'
author:
  name: Aashay Mehta
  email: f2016079@pilani.bits-pilani.ac.in
categories:
- CNN
- Object Detection
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** When humans have to solve everyday tasks, they simply pick the objects that are most suitable. While the question which object should one use for a specific task sounds trivial for humans, it is very difficult to answer for robots or other autonomous systems. This issue, however, is not addressed by current benchmarks for object detection that focus on detecting object categories. We therefore introduce the COCO-Tasks dataset which comprises about 40,000 images where the most suitable objects for 14 tasks have been annotated. We furthermore propose an approach that detects the most suitable objects for a given task. The approach builds on a Gated Graph Neural Network to exploit the appearance of each object as well as the global context of all present objects in the scene. In our experiments, we show that the proposed approach outperforms other approaches that are evaluated on the dataset like classification or ranking approaches.

**Paper Link:** [http://openaccess.thecvf.com/content_CVPR_2019/papers/Sawatzky_What_Object_Should_I_Use_-_Task_Driven_Object_Detection_CVPR_2019_paper.pdf](http://openaccess.thecvf.com/content_CVPR_2019/papers/Sawatzky_What_Object_Should_I_Use_-_Task_Driven_Object_Detection_CVPR_2019_paper.pdf)

**ID:** 162

**Guidelines:**

1. You have to implement the architecture given in the paper (Figure 5) using Tensorflow, Keras or PyTorch. You may replace the Resnet101 with Resnet50 to reduce the training time.
2. Compare your results on at least 3 different tasks with the simple Object Detector Baseline mentioned in the paper.


**Dataset Link**: [https://github.com/coco-tasks/dataset](https://github.com/coco-tasks/dataset)

