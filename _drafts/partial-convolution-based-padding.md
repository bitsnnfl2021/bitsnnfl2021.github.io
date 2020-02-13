---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: Image Super-Resolution Using Deep Convolutional Networks
categories:
- CNN
tags: []

---
**Abstract:** We propose a deep learning method for single image super-resolution (SR). Our method directly learns an end-to-end mapping between the low/high-resolution images. The mapping is represented as a deep convolutional neural network (CNN) that takes the low-resolution image as the input and outputs the high-resolution one. We further show that traditional sparse-coding-based SR methods can also be viewed as a deep convolutional network. But unlike traditional methods that handle each component separately, our method jointly optimizes all layers. Our deep CNN has a lightweight structure, yet demonstrates state-of-the-art restoration quality, and achieves fast speed for practical on-line usage. We explore different network structures and parameter settings to achieve trade-offs between performance and speed. Moreover, we extend our network to cope with three color channels simultaneously, and show better overall reconstruction quality.

Paper Link: [https://arxiv.org/abs/1501.00092](https://arxiv.org/abs/1501.00092 "https://arxiv.org/abs/1501.00092")

Conference : IEEE PAMI 2016

**Task:**

1\. Implement the architecture given in the paper using PyTorch.

2\. Implement the proper dataloader with any 2 data augmentation techniques.

3\. Show reconstructed images and calculate the corresponding PSNR/SSIM metrics.

4\. (Bonus):You can try to implement the binarizer function. It is non-differentiable so you may choose to write your own forward pass and backward pass for this unit using this [link](https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_custom_function.html). The bonus is just for you to learn more from this project. Do it only if you have time left towards the end.

**Dataset** Use any publicly available dataset with high quality images. You may use [http://www.image-net.org/](http://www.image-net.org/ "ImageNet")

**ID:** 21