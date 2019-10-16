---
layout: post
share: true
title: 'Phonocardiographic Sensing using Deep Learning for Abnormal Heartbeat Detection (Paper ID: 141)'
author:
  name: Sahil Ranadive
  email: f2016097@pilani.bits-pilani.ac.in
categories:
- RNN
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Cardiac auscultation involves expert interpretation of abnormalities in heart sounds using stethoscope. Deep learning based cardiac auscultation is of significant interest to the healthcare community as it can help reducing the burden of manual auscultation with automated detection of abnormal heartbeats. However, the problem of automatic cardiac auscultation is complicated due to the requirement of reliability and high accuracy, and due to the presence of background noise in the heartbeat sound. In this work, we propose a Recurrent Neural Networks (RNNs) based automated cardiac auscultation solution. Our choice of RNNs is motivated by the great success of deep learning in medical applications and by the observation that RNNs represent the deep learning configuration most suitable for dealing with sequential or temporal data even in the presence of noise. We explore the use of various RNN models, and demonstrate that these models deliver the abnormal heartbeat classification score with significant improvement. Our proposed approach using RNNs can be potentially be used for real-time abnormal heartbeat detection in the Internet of Medical Things for remote monitoring applications.

**Paper Link:** [https://arxiv.org/abs/1801.08322](https://arxiv.org/abs/1801.08322)

**ID:** 141

**Guidelines:**

1. https://physionet.org/content/hss/1.0/ 
Use this link to train your feature extractor.
2. Use simple RNN, GRU and LSTM separately to classify the heartbeats and compare their performance.

**Dataset Link**: [https://physionet.org/content/mitdb/1.0.0/](https://physionet.org/content/mitdb/1.0.0/)


