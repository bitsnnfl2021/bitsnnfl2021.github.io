---
layout: post
author:
  name: Paper ID 95
  difficulty: Medium
share: true
title: Robust Facial Landmark Detection via a Fully-Convolutional Local-Global Context
  Network
categories:
- CNN
- Computer Vision
tags: []

---
**Abstract** - While fully-convolutional neural networks are very strong at modeling local features, they fail to aggregate global context due to their constrained receptive field. Mod- ern methods typically address the lack of global context by introducing cascades, pooling, or by fitting a statisti- cal model. In this work, we propose a new approach that introduces global context into a fully-convolutional neural network directly. The key concept is an implicit kernel con- volution within the network. The kernel convolution blurs the output of a local-context subnet, which is then refined by a global-context subnet using dilated convolutions. The kernel convolution is crucial for the convergence of the net- work because it smoothens the gradients and reduces over- fitting. In a postprocessing step, a simple PCA-based 2D shape model is fitted to the network output in order to filter outliers. Our experiments demonstrate the effectiveness of our approach, outperforming several state-of-the-art meth- ods in facial landmark detection.

**Paper** - [https://openaccess.thecvf.com/content_cvpr_2018/papers/Merget_Robust_Facial_Landmark_CVPR_2018_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2018/papers/Merget_Robust_Facial_Landmark_CVPR_2018_paper.pdf "https://openaccess.thecvf.com/content_cvpr_2018/papers/Merget_Robust_Facial_Landmark_CVPR_2018_paper.pdf")

**Dataset** - [https://ibug.doc.ic.ac.uk/resources/300-W/](https://ibug.doc.ic.ac.uk/resources/300-W/ "https://ibug.doc.ic.ac.uk/resources/300-W/")