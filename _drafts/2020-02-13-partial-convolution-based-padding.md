---
layout: post
author:
  name: 'Paper ID: 81'
  email: bitsnnfl@gmail.com
share: true
title: 'Reprojection R-CNN: A Fast and Accurate Object Detector for 360◦ Images'
categories:
- R-CNN
tags: []

---
**Abstract:** 360◦ images are usually represented in either equirectangular projection (ERP) or multiple perspective projections. Different from the flat 2D images, the detection task is challenging for 360◦ images due to the distortion of ERP and the inefficiency of perspective projections. However, existing methods mostly focus on one of the above representations instead of both, leading to limited detection performance. Moreover, the lack of appropriate bounding-box annotations as well as the annotated datasets further increases the difficulties of the detection task. In this paper, we present a standard object detection framework for 360◦ images. Specifically, we adapt the terminologies of the traditional object detection task to the omnidirectional scenarios, and propose a novel two-stage object detector, i.e., Reprojection R-CNN by combining both ERP and perspective projection. Owing to the omnidirectional field-ofview of ERP, Reprojection R-CNN first generates coarse region proposals efficiently by a distortion-aware spherical region proposal network. Then, it leverages the distortionfree perspective projection and refines the proposed regions by a novel reprojection network. We construct two novel synthetic datasets for training and evaluation. Experiments reveal that Reprojection R-CNN outperforms the previous state-of-the-art methods on the mAP metric. In addition, the proposed detector could run at 178ms per image in the panoramic datasets, which implies its practicability in realworld applications.

Paper Link: [https://arxiv.org/pdf/1907.11830.pdf](https://arxiv.org/pdf/1907.11830.pdf "https://arxiv.org/pdf/1907.11830.pdf")

Conference :

**Task:**

1\. Implement the proper dataloader with any two augmentation techniques.

2\. Implement the Reprojection R-CNN architecture

3\. Compare the performance of the architecture on VOC360 and COCO-MEN datasets. (Refer table 2)

4\. You can use any framework.

**Dataset**: VOC360. You may download it from here: [https://researchdata.sfu.ca/islandora/object/sfu%3A2724](https://researchdata.sfu.ca/islandora/object/sfu%3A2724 "https://researchdata.sfu.ca/islandora/object/sfu%3A2724")

**ID:** 81