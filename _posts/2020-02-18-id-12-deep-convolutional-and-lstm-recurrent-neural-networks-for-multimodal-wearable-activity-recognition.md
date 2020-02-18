---
layout: post
author:
  name: 'Paper ID: 12'
  email: bitsnnfl@gmail.com
share: true
title: Deep Convolutional and LSTM Recurrent Neural Networks for Multimodal Wearable
  Activity Recognition
categories:
- LSTM
- Sensor
- CNN
tags: []

---
Abstract-Human activity recognition (HAR) tasks have traditionally been solved using engineered features obtained by heuristic processes. Current research suggests that deep convolutional neural networks are suited to automate feature extraction from raw sensor inputs. However, human activities are made of complex sequences of motor movements, and capturing this temporal dynamics is fundamental for successful HAR. Based on the recent success of recurrent neural networks for time series domains, we propose a generic deep framework for activity recognition based on convolutional and LSTM recurrent units, which: (i) is suitable for multimodal wearable sensors; (ii) can perform sensor fusion naturally; (iii) does not require expert knowledge in designing features; and (iv) explicitly models the temporal dynamics of feature activations. We evaluate our framework on two datasets, one of which has been used in a public activity recognition challenge. Our results show that our framework outperforms competing deep non-recurrent networks on the challenge dataset by 4% on average; outperforming some of the previous reported results by up to 9%. Our results show that the framework can be applied to homogeneous sensor modalities, but can also fuse multimodal sensors to improve performance. We characterise key architectural hyperparameters’ influence on performance to provide insights about their optimisation.

Paper - [https://www.mdpi.com/1424-8220/16/1/115](https://www.mdpi.com/1424-8220/16/1/115 "https://www.mdpi.com/1424-8220/16/1/115")

**Task:**

1. Implement the network architecture of DeepConvLSTM only 3.1
2. Try and replicate the results on the relevant metrics in the paper for Opportunity dataset only. Task A and Task B with and without Null class(4.1.1)(4.2)(5.1).
3. Multimodal Fusion Analysis (5.2)

**Data set:**

1. Opportunity Dataset. 2012. Available online: [**https://archive.ics.uci.edu/ml/datasets/OPPORTUNITY+Activity+Recognition**](https://archive.ics.uci.edu/ml/datasets/OPPORTUNITY+Activity+Recognition "https://archive.ics.uci.edu/ml/datasets/OPPORTUNITY+Activity+Recognition") 