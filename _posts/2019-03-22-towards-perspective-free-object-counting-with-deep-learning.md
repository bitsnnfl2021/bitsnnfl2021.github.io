---
layout: post
share: true
title: Towards perspective-free object counting with deep learning
author:
  name: Akash Sonth
  email: f2015265@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Easy
date: 2019-03-22 16:11:43 +0000

---
**Abstract**: In this paper we address the problem of counting objects instances in images. Our models are able to precisely estimate the number of vehicles in a traffic congestion, or to count the humans in a very crowded scene. Our first contribution is the proposal of a novel convolutional neural network solution, named Counting CNN (CCNN). Essentially, the CCNN is formulated as a regression model where the network learns how to map the appearance of the image patches to their corresponding object density maps. Our second contribution consists in a scale-aware counting model, the Hydra CNN, able to estimate object densities in different very crowded scenarios where no geometric information of the scene can be provided. Hydra CNN learns a multiscale non-linear regression model which uses a pyramid of image patches extracted at multiple scales to perform the final density prediction. We report an extensive experimental evaluation, using up to three different object counting benchmarks, where we show how our solutions achieve a state-of-the-art performance.

**Paper Link**: [http://agamenon.tsc.uah.es/Investigacion/gram/publications/eccv2016-onoro.pdf](http://agamenon.tsc.uah.es/Investigacion/gram/publications/eccv2016-onoro.pdf "http://agamenon.tsc.uah.es/Investigacion/gram/publications/eccv2016-onoro.pdf")

**Paper ID: 33**

**Guidelines:** 

1) The dataset mentioned in the paper is quite large and it would not be possible to train without a GPU. Therefore, either crop out small portions from the original dataset OR, create a synthetic dataset consisting of some background image with characters present at random locations on this image. 

2) Go through the paper, understand the training technique and the preprocessing involved to feed patches from the image to the network.

3) Implement the CountingCNN architecture from the paper for density prediction of either the vehicles or the characters (in case you create a synthetic dataset).