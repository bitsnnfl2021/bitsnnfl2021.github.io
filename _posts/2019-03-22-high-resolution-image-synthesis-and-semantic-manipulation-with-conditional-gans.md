---
layout: post
share: true
title: 'High-Resolution Image Synthesis and Semantic Manipulation with Conditional
  GANs (Paper ID: 71)'
author:
  name: Rishav
  email: f2016108@pilani.bits-pilani.ac.in
categories:
- GANs
- Computer Vision
- CNN
tags:
- Hard
date: 2019-03-22 16:21:10 +0000

---
**Short Introduction:** The paper presents a method for synthesising high resolution photo-realistic images from semantic label maps using conditional generative adversarial networks (conditional GANs). This is a challenging paper but worth doing as it promises a exponential learning curve.

This method has a wide range of applications. For example, we can use it to create synthetic training data for training visual recognition algorithms, since it is much easier to create semantic labels for desired scenarios than to generate training images. Using semantic segmentation methods, we can transform images into a semantic label domain, edit the objects in the label domain, and then transform them back to the image domain.

**Paper:** [https://arxiv.org/pdf/1711.11585](https://arxiv.org/pdf/1711.11585 "https://arxiv.org/pdf/1711.11585")

**Paper ID: 71**

**_Expected Deliverables:_**

1. Develop a proper understanding of adversarial loss and why is it better?
2. You can implement the paper using only the Semantic maps and not the instance map _(refer paper for details)_, if curious enough you can implement that too.
3. **Implementation of pix2pix based architecture with modifications carries the highest credit**.
4. Save atleast 3 result images.
5. You are free to code in any framework of your choice.
6. Dataset Recommended: **_Cityscapes_**
7. You can use **_small part_** of the Dataset if you have machine limitations, **_more focus for this particular paper will be on your implementation and not high accuracy_**.
8. Feel free to contact me in case of any doubt.

**Side Notes:**
1. For introduction to GANs, refer [https://medium.com/@jonathan_hui/gan-whats-generative-adversarial-networks-and-its-application-f39ed278ef09](https://medium.com/@jonathan_hui/gan-whats-generative-adversarial-networks-and-its-application-f39ed278ef09) .
