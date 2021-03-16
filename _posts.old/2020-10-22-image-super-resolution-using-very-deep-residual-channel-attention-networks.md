---
layout: post
author:
  name: Paper ID 42
  difficulty: Medium
share: true
title: Image Super-Resolution Using very deep Residual Channel Attention Networks.
categories:
- CNN
- Super Resolution
tags: []

---
**Abstract** - Convolutional neural network (CNN) depth is of crucial importance for image super-resolution (SR). However, we observe that deeper networks for image SR are more difficult to train. The low-resolution inputs and features contain abundant low-frequency information, which is treated equally across channels, hence hindering the representational ability of CNNs. To solve these problems, we propose the very deep residual channel attention networks (RCAN). Specifically, we propose a residual in residual (RIR) structure to form very deep network, which consists of several residual groups with long skip connections. Each residual group contains some residual blocks with short skip connections. Meanwhile, RIR allows abundant low-frequency information to be bypassed through multiple skip connections, making the main network focus on learning high-frequency information. Furthermore, we propose a channel attention mechanism to adaptively rescale channel-wise features by considering interdependencies among channels. Extensive experiments show that our RCAN achieves better accuracy and visual improvements against state-of-the-art methods. 

**Paper** - [https://arxiv.org/abs/1807.02758.pdf](https://arxiv.org/abs/1807.02758.pdf "https://arxiv.org/abs/1807.02758.pdf") 

**Dataset** - [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/ "https://data.vision.ee.ethz.ch/cvl/DIV2K/")