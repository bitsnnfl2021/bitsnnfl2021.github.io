---
layout: post
author:
  name: Paper ID 12
  difficulty: Easy
share: true
title: Rotation-invariant convolutional neural networks for galaxy morphology prediction
categories:
- CNN
- Computer Vision
- Galaxy Morphology
- Rotation Invariance
tags: []

---
**Abstract** - Measuring the morphological parameters of galaxies is a key requirement for studying their formation and evolution. Surveys such as the Sloan Digital Sky Survey (SDSS) have resulted in the availability of very large collections of images, which have permitted population-wide analyses of galaxy morphology. Morphological analysis has traditionally been carried out mostly via visual inspection by trained experts, which is time-consuming and does not scale to large (& 104 ) numbers of images. Although attempts have been made to build automated classification systems, these have not been able to achieve the desired level of accuracy. The Galaxy Zoo project successfully applied a crowdsourcing strategy, inviting online users to classify images by answering a series of questions. Unfortunately, even this approach does not scale well enough to keep up with the increasing availability of galaxy images. We present a deep neural network model for galaxy morphology classification which exploits translational and rotational symmetry. It was developed in the context of the Galaxy Challenge, an international competition to build the best model for morphology classification based on annotated images from the Galaxy Zoo project. For images with high agreement among the Galaxy Zoo participants, our model is able to reproduce their consensus with near-perfect accuracy (> 99%) for most questions. Confident model predictions are highly accurate, which makes the model suitable for filtering large collections of images and forwarding challenging images to experts for manual annotation. This approach greatly reduces the experts’ workload without affecting accuracy. The application of these algorithms to larger sets of training data will be critical for analysing results from future surveys such as the LSST.

**Paper** - [https://arxiv.org/pdf/1503.07077.pdf](https://arxiv.org/pdf/1503.07077.pdf "https://arxiv.org/pdf/1503.07077.pdf")

**Dataset -** [https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data "https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data")