---
layout: post
share: true
title: 'Deep Learning EEG Response Representation for Brain Computer Interfaces (Paper
  ID: 12)'
author:
  name: Achal Agarwal
  email: f2015436@pilani.bits-pilani.ac.in
categories:
- BCI
- EEG
- CNN
- Deep Learning
tags:
- Hard
date: 2019-03-19 10:13:45 +0000

---
**Abstract:** In this paper, the multi-scale deep convolutional neural networks are introduced to deal with the representation for imagined motor Electroencephalography (EEG) signals. We propose to learn a set of high-level feature representations through deep learning algorithm, referred to as Deep Motor Features (DeepMF), for brain computer interface (BCI) with imagined motor tasks. As the extracted DeepMF are dissimilar for different tasks and alike for the same tasks, it is convenient to separate the diverse EEG signals for imagined motor tasks apart. Our approach achieves 100% accuracy for 4 classes imagined motor EEG signals classification on Project BCI - EEG motor activity dataset. Moreover, thanks to the highly abstract features DeepMF learned, only 4.125 seconds trials of training data are needed, compared with the conventional BLDA algorithm for 8.75 seconds trials demand to achieve the same accuracy, accordingly the BCI response time and the required trials for training are almost declined by half. Experiments are provided to illustrate the effectiveness of the proposed design approach.

**Link to Paper:** [https://slack-files.com/TFF2Y6CJ3-FH219DUAE-8f778e05f5](https://slack-files.com/TFF2Y6CJ3-FH219DUAE-8f778e05f5 "Link to Paper")

**ID:** 12

**Soft Restrictions:** Preferably avoid Theano for your framework of choice.

**Dataset:** Project BCI - EEG motor activity data set (BCI Research) at NUST.

**Requirements**: 

1. Build the network as specified in Fig 1. and Section 3.2.
2. Perform experiments on your network in accordance with Section 4.
3. Modify your network by removing the third Convolutional and Pooling layers and adjusting the size of your Fully Connected Layer.
4. Perform experiments with the new network as carried out in 2.
5. Compare the results obtained in 2. and 4.