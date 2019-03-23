---
layout: post
share: true
title: 'DSOD: Learning Deeply Supervised Object Detectors from Scratch'
author:
  name: Rishav
  email: f2016108@pilani.bits-pilani.ac.in
categories:
- Computer Vision
- Object Detection
- CNNs
- Difficult
tags:
- Medium
date: 2019-03-22 16:28:14 +0000

---
**Short Introduction:** Deeply Supervised Object Detector (DSOD) is a framework that can learn object detectors from **_scratch_**. State-of-the-art object objectors rely heavily on the off the-shelf networks pre-trained on large-scale classification datasets like ImageNet, which incurs learning bias due to the difference on both the loss functions and the category distributions between classification and detection tasks.

**I recommend going through the paper once to get a proper grasp of the subject.**

**Paper :** [https://arxiv.org/pdf/1708.01241.pdf](https://arxiv.org/pdf/1708.01241.pdf "https://arxiv.org/pdf/1708.01241.pdf")

**Paper ID : 73**

**_Expected Deliverables:_**

1. I recommend implementing the paper in Keras.(_Please don't implement it in Caffe_)
2. The network structure of DSOD can be divided into two parts: the backbone sub-network for feature extraction and the front-end sub-network for prediction over multi-scale response maps.
3. The backbone and front-end sub-net must be implemented with utmost care and you should develop proper understanding of all functions and methods that you will use for this purpose.
4. The paper isn't very difficult but I recommend reading it thoroughly to understand the principles. Don't start coding without properly understanding the design principles.
5. Try out different variants of DenseNet architecture as the backbone for **_DSOD (This is for bonus! , should not be difficult anyways_**_)_
6. **Dataset :** Use **_tiny_** **_MS-COCO_**
7. Feel free to contact me incase of any doubt.