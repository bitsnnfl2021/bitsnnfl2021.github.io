---
layout: post
share: true
title: Single Trial P300 Classification Using Convolutional LSTM
author:
  name: Amit Tiwary
  email: f2015818@pilani.bits-pilani.ac.in
categories:
- LSTM
- EEG
tags:
- Medium
date: 2019-03-23 10:07:26 +0000

---
**Abstract:** EEG signals have shown to elicit a positive deflection known as the P300 event related potential during odd ball experiments. BCIs based on these experiments rely on detection of the P300 potential. EEG signals are noisy, and therefore P300 detection is performed on an average of multiple trials, thus making them inappropriate for BCI applications. We propose a neural network model based on Convolutional Long Short Term Memory (ConvLSTM) for single trial P300 classification. EEG data encodes both spatial and temporal information using multiple EEG sensors. Convolutional neural networks (CNNs) have been known to capture spatial information whereas LSTMs are known to capture temporal information. Our experiments show that the proposed method outperforms previous CNN based approaches on raw EEG signals. The approaches were evaluated on publicly available dataset II of BCI competition III.

**Paper Link:** [https://sci-hub.tw/10.1007/978-3-030-04021-5_1](https://sci-hub.tw/10.1007/978-3-030-04021-5_1 "https://sci-hub.tw/10.1007/978-3-030-04021-5_1")

**Paper ID: 43**

**Guidelines:**

1. Read the paper thoroughly and understand the concepts and architectures enlisted therein.
2. Download the BCI III competition dataset. (Contact me if you face difficulties with the same.)
3. Implement only the ConvLSTM model as described in the paper.
4. As the dataset has a class imbalance issue (1:6 ratio for the data of both the classes), tackle it using Random Oversampling and Random Undersampling and compare the results of the two models trained.