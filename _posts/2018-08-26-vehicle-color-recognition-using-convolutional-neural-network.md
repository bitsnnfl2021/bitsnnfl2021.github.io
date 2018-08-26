---
layout: post
share: true
title: Vehicle Color Recognition using Convolutional Neural Network
date: 2018-08-26 12:06:56 +0530
author:
  name: Rohitkumar Arasanipalai
  email: f2015666@pilani.bits-pilani.ac.in
categories: []
tags: []

---
Vehicle color information is one of the important elements in ITS (Intelligent Traffic System). In this paper, we present a vehicle color recognition method using convolutional neural network (CNN). Naturally, CNN is designed to learn classification method based on shape information, but we proved that CNN can also learn classification based on color distribution. In our method, we convert the input image to two different color spaces, HSV and CIE Lab, and run it to some CNN architecture. The training process follow procedure introduce by Krizhevsky, that learning rate is decreasing by factor of 10 after some iterations. To test our method, we use publicly vehicle color recognition dataset provided by Chen. The results, our model outperform the original system provide by Chen with 2% higher overall accuracy.  

Link: [https://arxiv.org/abs/1510.07391v3](https://arxiv.org/abs/1510.07391v3 "https://arxiv.org/abs/1510.07391v3")