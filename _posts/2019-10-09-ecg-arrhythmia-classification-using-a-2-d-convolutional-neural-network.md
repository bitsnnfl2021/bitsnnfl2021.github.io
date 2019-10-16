---
layout: post
share: true
title: 'ECG arrhythmia classification using a 2-D convolutional neural network (Paper ID: 142)'
author:
  name: Sahil Ranadive
  email: f2016097@pilani.bits-pilani.ac.in
categories:
- CNN
- Wave Segmentation
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** In this paper, we propose an effective electrocardiogram (ECG) arrhythmia classification method using a deep two-dimensional convolutional neural network (CNN) which recently shows outstanding performance in the field of pattern recognition. Every ECG beat was transformed into a two-dimensional grayscale image as an input data for the CNN classifier. Optimization of the proposed CNN classifier includes various deep learning techniques such as batch normalization, data augmentation, Xavier initialization, and dropout. In addition, we compared our proposed classifier with two well-known CNN models; AlexNet and VGGNet. ECG recordings from the MIT-BIH arrhythmia database were used for the evaluation of the classifier. As a result, our classifier achieved 99.05% average accuracy with 97.85% average sensitivity. To precisely validate our CNN classifier, 10-fold cross-validation was performed at the evaluation which involves every ECG recording as a test data. Our experimental results have successfully validated that the proposed CNN classifier with the transformed ECG images can achieve excellent classification accuracy without any manual pre-processing of the ECG signals such as noise filtering, feature extraction, and feature reduction.

**Paper Link:** [https://arxiv.org/abs/1804.06812](https://arxiv.org/abs/1804.06812)

**ID:** 142

**Guidelines:**

1. Convert the .wav/.atr(your choice) datafiles to images (segmentation).
2. You need not perform the augmentation step. 
3.  Apply the model mentioned in the paper to detect the type of heartbeat and derive accuracy, sensitivity, precision, f measure and confusion matrix.
Note: You may use lesser layers if the training step is time consuming.

**Dataset Link**: [https://physionet.org/content/mitdb/1.0.0/](https://physionet.org/content/mitdb/1.0.0/)

