---
layout: post
author:
  name: Paper ID 71
  difficulty: Medium
share: true
title: Identity Mappings in Deep Residual Networks
categories: []
tags:
- CNN
- Deep Residual Networks

---
**Abstract** - Deep residual networks \[1\] have emerged as a family of extremely deep architectures showing compelling accuracy and nice convergence behaviors. In this paper, we analyze the propagation formulations behind the residual building blocks, which suggest that the forward and backward signals can be directly propagated from one block to any other block, when using identity mappings as the skip connections and after-addition activation. A series of ablation experiments support the importance of these identity mappings. This motivates us to propose a new residual unit, which further makes training easy and improves generalization. We report improved results using a 1001-layer ResNet on CIFAR-10 (4.62% error) and CIFAR-100, and a 200-layer ResNet on ImageNet. 

**Paper** - [https://arxiv.org/pdf/1603.05027v2.pdf](https://arxiv.org/pdf/1603.05027v2.pdf "https://arxiv.org/pdf/1603.05027v2.pdf") 

**Dataset** - [https://www.cs.toronto.edu/\~kriz/cifar.html](https://www.cs.toronto.edu/\~kriz/cifar.html "https://www.cs.toronto.edu/~kriz/cifar.html")