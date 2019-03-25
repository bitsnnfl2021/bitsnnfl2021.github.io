---
layout: post
share: true
title: Deep Face Recognition
author:
  name: Akash Sonth
  email: f2015265@pilani.bits-pilani.ac.in
categories:
- CNN
- Computer Vision
tags:
- Hard
date: 2019-03-25 09:08:34 +0000

---
**Abstract:** The goal of this paper is face recognition – from either a single photograph or from a set of faces tracked in a video. Recent progress in this area has been due to two factors: (i) end to end learning for the task using a convolutional neural network (CNN), and (ii) the availability of very large scale training datasets. We make two contributions: first, we show how a very large scale dataset (2.6M images, over 2.6K people) can be assembled by a combination of automation and human in the loop, and discuss the trade off between data purity and time; second, we traverse through the complexities of deep network training and face recognition to present methods and procedures to achieve comparable state of the art results on the standard LFW and YTF face benchmarks.

**Paper Link:** [http://www.robots.ox.ac.uk/\~vgg/publications/2015/Parkhi15/parkhi15.pdf](http://www.robots.ox.ac.uk/\~vgg/publications/2015/Parkhi15/parkhi15.pdf "http://www.robots.ox.ac.uk/~vgg/publications/2015/Parkhi15/parkhi15.pdf")

**Paper ID: 35**

**Guidelines:**

1. Go through the paper, understand the training technique and the preprocessing involved to recognize faces.
2. Modify the training approach using transfer learning to recognize new faces. Note that only one instance of a new face to be used for training. You can also use the network weights given in the paper.
3. Suggested frameworks: Keras, Matlab