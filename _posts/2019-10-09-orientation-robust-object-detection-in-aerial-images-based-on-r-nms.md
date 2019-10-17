---
layout: post
share: true
title: 'Orientation Robust Object Detection in Aerial Images Based on R-NMS (Paper ID: 192)'
author:
  name: Abhilash Neog
  email: f2016004@pilani.bits-pilani.ac.in
categories:
- Object Detection
tags:
- Hard
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Object detection in aerial images is a challenging task which plays an important role in many fields, such as intelligent traffic management, fishery management and so on. Different from object detection in natural images, the orientation of objects in aerial images is arbitrary. The axis-aligned bounding box detection, which is always used in traditional object detection methods, will cover a lot of redundant information and deteriorate the detection results when it is used to locate the object in aerial images. Therefore, traditional object detection methods are no longer applicable for aerial images. In order to promote the object detection performance in aerial images, we propose a novel orientation robust object detection model based on rotated non-maximum suppression (R-NMS). In addition, we adjust the anchor setting according to the diversity shapes of the aerial objects to enhance the performance of the model. Our model is tested on the public DOTA dataset, and the mAP is 16.31% higher than the baseline, indicating that our method is very effective and competitive in the object detection of aerial image.

**Paper Link:** [https://www.sciencedirect.com/science/article/pii/S1877050919308725](https://www.sciencedirect.com/science/article/pii/S1877050919308725)

**ID:** 192

**Guidelines:**

1. Implement the given architecture as in the paper. It is not mandatory to perform rotated-NMS. Can implement the traditional NMS technique as well.  
2. The loss functions can be standard ones, specific to the ones used in the standard faster R-CNN network, and may not be the one proposed in the paper.
3. Report the accuracy in the form of IoU or MAP metrics.

**Dataset Link**: [https://captain-whu.github.io/DOTA/dataset.html](https://captain-whu.github.io/DOTA/dataset.html)
