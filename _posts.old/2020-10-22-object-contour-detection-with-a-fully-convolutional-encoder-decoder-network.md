---
layout: post
author:
  name: Paper ID 65
  difficulty: Medium
share: true
title: Object Contour Detection with a Fully Convolutional Encoder-Decoder Network
categories:
- Computer Vision
- FCNN
- Object Detection
tags: []

---
**Abstract** - We develop a deep learning algorithm for contour detection with a fully convolutional encoder-decoder network. Different from previous low-level edge detection, our algorithm focuses on detecting higher-level object contours. Our network is trained end-to-end on PASCAL VOC with refined ground truth from inaccurate polygon annotations, yielding much higher precision in object contour detection than previous methods. We find that the learned model generalizes well to unseen object classes from the same supercategories on MS COCO and can match state-of-the-art edge detection on BSDS500 with fine-tuning. By combining with the multiscale combinatorial grouping algorithm, our method can generate high-quality segmented object proposals, which significantly advance the state-of-the-art on PASCAL VOC (improving average recall from 0.62 to 0.67) with a relatively small amount of candidates (∼1660 per image).

**Paper** - [https://arxiv.org/pdf/1603.04530v1.pdf](https://arxiv.org/pdf/1603.04530v1.pdf "https://arxiv.org/pdf/1603.04530v1.pdf")

**Dataset -** [https://www.tensorflow.org/datasets/catalog/voc](https://www.tensorflow.org/datasets/catalog/voc "https://www.tensorflow.org/datasets/catalog/voc") (use voc 2012)