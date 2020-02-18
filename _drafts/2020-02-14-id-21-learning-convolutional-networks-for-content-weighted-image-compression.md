---
layout: post
author:
  name: 'Paper ID: 23'
  email: bitsnnfl@gmail.com
share: true
title: End-to-end people detection in crowded scenes
categories:
- Object Detection
- CNN
tags: []

---
**Abstract:** Current people detectors operate either by scanning an image in a sliding window fashion or by classifying a discrete set of proposals. We propose a model that is based on decoding an image into a set of people detections. Our system takes an image as input and directly outputs a set of distinct detection hypotheses. Because we generate predictions jointly, common post-processing steps such as non-maximum suppression are unnecessary. We use a recurrent LSTM layer for sequence generation and train our model end-to-end with a new loss function that operates on sets of detections. We demonstrate the effectiveness of our approach on the challenging task of detecting people in crowded scenes.

Paper Link: [https://arxiv.org/pdf/1506.04878.pdf](https://arxiv.org/pdf/1506.04878.pdf "https://arxiv.org/pdf/1506.04878.pdf")

Conference : CVPR 2016

**Task:**

1\. Implement the architecture proposed in the paper.

2\. Implement the proper dataloader with any 2 data augmentation techniques.

3\. Compare results to the ones in the paper.

4\. You can use any framework you want.

**Dataset** Use any publicly available crowd detection dataset. You may use [https://www.crowdhuman.org/](https://www.crowdhuman.org/ "https://www.crowdhuman.org/")

**ID:** 23