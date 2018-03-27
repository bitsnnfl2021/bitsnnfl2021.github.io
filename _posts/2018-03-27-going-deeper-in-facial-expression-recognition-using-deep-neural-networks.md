---
layout: post
share: true
title: Going Deeper in Facial Expression Recognition using Deep Neural Networks
date: 2018-03-27 16:45:35 +0000
author:
  name: Shrikant Sharda
  email: f2014046@pilani.bits-pilani.ac.in
categories: []
tags: []
---
**Abstract**:

Automated Facial Expression Recognition (FER) has remained a challenging and interesting problem. Despite efforts made in developing various methods for FER, existing approaches traditionally lack generalizability when applied to unseen images or those that are captured in wild setting. Most of the existing approaches are based on engineered features (e.g. HOG, LBPH, and Gabor) where the classifier’s hyperparameters are tuned to give best recognition accuracies across a single database, or a small collection of similar databases. Nevertheless, the results are not significant when they are applied to novel data. This paper proposes a deep neural network architecture to address the FER problem across multiple well-known standard face datasets. Specifically, our network consists of two convolutional layers each followed by max pooling and then four Inception layers. The network is a single component architecture that takes registered facial images as the input and classifies them into either of the six basic or the neutral expressions. We conducted comprehensive experiments on seven publically available facial expression databases, viz. MultiPIE, MMI, CK+, DISFA, FERA, SFEW, and FER2013. The results of proposed architecture are comparable to or better than the state-of-the-art methods and better than traditional convolutional neural networks and in both accuracy and training time. 

**Paper Link**: [https://arxiv.org/pdf/1511.04110.pdf](https://arxiv.org/pdf/1511.04110.pdf "https://arxiv.org/pdf/1511.04110.pdf")

**Deliverables**: Implement the full network explained in fair detail in the paper using Tensorflow or Pytorch. Show the decrease in loss function with iterations.

**Dataset**: MMI or FER2013. FER2013 is freely available on Kaggle and MMI needs an account to be downloaded. [https://mmifacedb.eu](https://mmifacedb.eu "https://mmifacedb.eu")