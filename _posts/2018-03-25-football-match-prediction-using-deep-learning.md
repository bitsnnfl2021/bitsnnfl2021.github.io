---
layout: post
share: true
title: Football Match Prediction using Deep Learning
date: 2018-03-25 22:48:11 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- General Deep Learning
tags:
- Medium
- Application
---
**Abstract:** In this thesis, the deep learning method Recurrent Neural Networks (RNNs) has been investigated for predicting the outcomes of football matches. The dataset consists of previous recorded matches from multiple seasons of leagues and tournaments from 63 different countries and 3 tournaments that include multiple countries. In the thesis work, we have studied several different ways of forming up input data sequences, as well as different LSTM architectures of RNNs that may lead to effective prediction, along with LSTM hyper-parameter tuning and testing. Extensive tests have been conducted through many case studies for the prediction and classification of football match winners. Using the proposed LSTM architectures, we show that the classification accuracy of the football outcome is 98.63% for many-to-one strategy, and 88.68% for manyto-many strategy. The prediction accuracy starts from 33.35% for many-to-one and 43.96% for many-to-many, and is increasing when more information about a match from longer time duration of data sequence is fed to the network. Using the full time data sequence, the RNN accuracy reached 98.63% for many-to-one, and 88.68% for many-to-many strategy. Our test results have shown that deep learning may be used for successfully predicting the outcomes of football matches. For further increasing the performance of the prediction, prior information about each team, player and match would be desirable.

**Paper Link:** [http://publications.lib.chalmers.se/records/fulltext/250411/250411.pdf](http://publications.lib.chalmers.se/records/fulltext/250411/250411.pdf "http://publications.lib.chalmers.se/records/fulltext/250411/250411.pdf")

**Task:** mplement the core algorithm in python using Tensorflow, Pytorch, MXNet or NumPy. Train the network using [European Soccer Database]().