---
layout: post
share: true
title: 'SSD: Single Shot MultiBox Detector (Paper ID: 23)'
author:
  name: Aditya Rana
  email: f2016182@pilani.bits-pilani.ac.in
categories:
- Object Detection
- Computer Vision
tags:
- Medium
date: 2019-03-21 20:21:09 +0000

---
**Abstract:** We present a method for detecting objects in images using a single deep neural network. Our approach, named SSD, discretizes the output space of bounding boxes into a set of default boxes over different aspect ratios and scales per feature map location. At prediction time, the network generates scores for the presence of each object category in each default box and produces adjustments to the box to better match the object shape. Additionally, the network combines predictions from multiple feature maps with different resolutions to naturally handle objects of various sizes. SSD is simple relative to methods that require object proposals because it completely eliminates proposal generation and subsequent pixel or feature resampling stages and encapsulates all computation in a single network. This makes SSD easy to train and straightforward to integrate into systems that require a detection component. Experimental results on the PASCAL VOC, COCO, and ILSVRC datasets confirm that SSD has competitive accuracy to methods that utilize an additional object proposal step and is much faster, while providing a unified framework for both training and inference. For 300 × 300 input, SSD achieves 74.3% mAP1 on VOC2007 test at 59 FPS on a Nvidia Titan X and for 512 × 512 input, SSD achieves 76.9% mAP, outperforming a comparable state-of-the-art Faster R-CNN model. Compared to other single stage methods, SSD has much better accuracy even with a smaller input image size

**Paper Link:** [https://arxiv.org/pdf/1512.02325.pdf](https://arxiv.org/pdf/1512.02325.pdf "https://arxiv.org/pdf/1512.02325.pdf")

**Task:**

1. The paper has been implemented using Caffe. Your job is to implement the core model using Keras, Tensorflow or PyTorch on any one of the above datasets.
2. Compare your results with the state of the art-models.

**ID :** 23