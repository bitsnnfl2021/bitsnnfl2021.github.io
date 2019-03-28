---
layout: post
share: true
title: 'Deep Learning Human Mind for Automated Visual Classification (Paper ID: 124)'
author:
  name: Vikram Waradpande
  email: f2015454@pilani.bits-pilani.ac.in
categories:
- CNN
- LSTM
tags:
- Easy
date: 2019-03-22 02:23:36 +0000

---
**Abstract:** What if we could effectively read the mind and transfer human visual capabilities to computer vision methods? In this paper, we aim at addressing this question by developing the first visual object classifier driven by human brain signals. In particular, we employ EEG data evoked by visual object stimuli combined with Recurrent Neural Networks (RNN) to learn a discriminative brain activity manifold of visual categories in a reading the mind effort. Afterward, we transfer the learned capabilities to machines by training a Convolutional Neural Network (CNN)–based regressor to project images onto the learned manifold, thus allowing machines to employ human brain–based features for automated visual classification. We use a 128-channel EEG with active electrodes to record brain activity of several subjects while looking at images of 40 ImageNet object classes. The proposed RNN-based approach for discriminating object classes using brain signals reaches an average accuracy of about 83%, which greatly outperforms existing methods attempting to learn EEG visual object representations. As for automated object categorization, our human brain–driven approach obtains competitive performance, comparable to those achieved by powerful CNN models and it is also able to generalize over different visual datasets.

**Paper Link:** [http://openaccess.thecvf.com/content_cvpr_2017/papers/Spampinato_Deep_Learning_Human_CVPR_2017_paper.pdf](http://openaccess.thecvf.com/content_cvpr_2017/papers/Spampinato_Deep_Learning_Human_CVPR_2017_paper.pdf "http://openaccess.thecvf.com/content_cvpr_2017/papers/Spampinato_Deep_Learning_Human_CVPR_2017_paper.pdf")

**Tasks:**

1. Acquire the dataset from the sources mentioned by the authors in the paper.
2. Implement the RNN and autoencoder network to classify images into the 40 ImageNet classes
3. Bonus: Also implement the transfer of learnt categories to the CNN as mentioned in the paper.
4. Strictly DO NOT use any pre-exisiting implementations of this paper. Use a different framework.

**ID:** 124