---
layout: post
share: true
title: Understanding Neural Networks Through Deep Visualization
date: 2018-03-24 03:41:32 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- " Computer Vision"
- Machine Learning Interpretability
tags:
- Hard
- Theory
- Brownie points
- Open Source Tool
---
**Abstract:** Recent years have produced great advances in training large, deep neural networks (DNNs), including notable successes in training convolutional neural networks (convnets) to recognize natural images. However, our understanding of how these models work, especially what computations they perform at intermediate layers, has lagged behind. Progress in the field will be further accelerated by the development of better tools for visualizing and interpreting neural nets. We introduce two such tools here. The first is a tool that visualizes the activations produced on each layer of a trained convnet as it processes an image or video (e.g. a live webcam stream). We have found that looking at live activations that change in response to user input helps build valuable intuitions about how convnets work. The second tool enables visualizing features at each layer of a DNN via regularized optimization in image space. Because previous versions of this idea produced less recognizable images, here we introduce several new regularization methods that combine to produce qualitatively clearer, more interpretable visualizations. Both tools are open source and work on a pretrained convnet with minimal setup.

**Paper Link:** [http://yosinski.com/media/papers/Yosinski__2015__ICML_DL__Understanding_Neural_Networks_Through_Deep_Visualization__.pdf](http://yosinski.com/media/papers/Yosinski__2015__ICML_DL__Understanding_Neural_Networks_Through_Deep_Visualization__.pdf "http://yosinski.com/media/papers/Yosinski__2015__ICML_DL__Understanding_Neural_Networks_Through_Deep_Visualization__.pdf")

**Task:** Implement the gradient ascent method described in the paper in python using TensoFlow, Pytorch or MXNet. Use Bokeh to create a dynamically updating  UI to visualise the change in features obtained by gradient ascent for each filter as the training progresses. Create a [slider](https://stackoverflow.com/questions/36985729/sliding-through-images-with-bokeh-slider?rq=1) to browser through visualisation history for a given filter.

**Brownie points:** Implement deconvolution based feature visualisation method.