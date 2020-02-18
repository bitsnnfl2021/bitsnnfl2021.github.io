---
layout: post
author:
  name: 'Paper ID: 51'
  email: bitsnnfl@gmail.com
share: true
title: Mask R-CNN
categories:
- 'Image Detection '
- CNN
- Instance Segmentation
tags: []

---
**Abstract:**

We present a conceptually simple, flexible, and general framework for object instance segmentation. Our approach efficiently detects objects in an image while simultaneously generating a high-quality segmentation mask for each instance. The method, called Mask R-CNN, extends Faster R-CNN by adding a branch for predicting an object mask in parallel with the existing branch for bounding box recognition. Mask R-CNN is simple to train and adds only a small overhead to Faster R-CNN, running at 5 fps. Moreover, Mask R-CNN is easy to generalize to other tasks, e.g., allowing us to estimate human poses in the same framework. We show top results in all three tracks of the COCO suite of challenges, including instance segmentation, boundingbox object detection, and person keypoint detection. Without bells and whistles, Mask R-CNN outperforms all existing, single-model entries on every task, including the COCO 2016 challenge winners. We hope our simple and effective approach will serve as a solid baseline and help ease future research in instance-level recognition.

**Paper Link:** [https://arxiv.org/pdf/1703.06870.pdf](https://arxiv.org/pdf/1703.06870.pdf "https://arxiv.org/pdf/1703.06870.pdf")

**Tasks:**

1. Implement the model on Tensorflow and Keras.  
2. Use subsets for the paper implementation. Clearly report the number of data samples of each category in training and testing sets.
3. Instance Segmentation - Follow the architecture given in the paper and show bounding box predictions for the test set. Report the accuracy of your model. 
4. Human Pose Estimation - Implement using only keypoint detection and report your results. (You may take fewer keypoints than the ones specified in the paper for the implementation)

**Data Set:** Subsets of the [COCO](http://cocodataset.org/#home "COCO") dataset

**Paper ID:** 51