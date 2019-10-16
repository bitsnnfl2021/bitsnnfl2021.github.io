---
layout: post
share: true
title: 'Deep Learning With Convolutional Neural Networks for EEG Decoding and Visualization
  (Paper ID: 13)'
author:
  name: Vivek Golani
  email: f2016196@pilani.bits-pilani.ac.in
categories:
- EEG
- BCI
- CNN
tags:
- Easy
date: 2019-03-19 10:09:57 +0000

---
**Abstract:** In this paper, the multi-scale deep convolutional neural networks are introduced to deal with the representation for imagined motor Electroencephalography (EEG) signals. We propose to learn a set of high-level feature representations through deep learning algorithm, referred to as Deep Motor Features (DeepMF), for brain computer interface (BCI) with imagined motor tasks. As the extracted DeepMF are dissimilar for different tasks and alike for the same tasks, it is convenient to separate the diverse EEG signals for imagined motor tasks apart. Our approach achieves 100% accuracy for 4 classes imagined motor EEG signals classification on Project BCI - EEG motor activity dataset. Moreover, thanks to the highly abstract features DeepMF learned, only 4.125 seconds trials of training data are needed, compared with the conventional BLDA algorithm for 8.75 seconds trials demand to achieve the same accuracy, accordingly the BCI response time and the required trials for training are almost declined by half. Experiments are provided to illustrate the effectiveness of the proposed design approach.

**Link to Paper:** [https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.23730](https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.23730 "Link to Paper")

**ID:** 13

**Restrictions:** Torch Framework (this includes PyTorch and other derivatives).

**Dataset:** [2a](http://www.bbci.de/competition/iv/#datasets "DataSet")

**Requirements**:

1. Build the network as specified in section titled ConvNet Architecture.
2. Perform training as specified in the paper.
3. Evaluate results and compare with those in the paper.
