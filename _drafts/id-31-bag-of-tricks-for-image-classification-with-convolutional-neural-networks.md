---
layout: post
share: true
title: "[ID_31] Bag of Tricks for Image Classification with Convolutional Neural Networks"
author:
  name: BITS NNFL
  email: bitsnnfl@gmail.com
categories:
- cnn
- tuning
tags:
- easy

---
**Abstract:** Much of the recent progress made in image classification research can be credited to training procedure refinements, such as changes in data augmentations and optimization methods. In the literature, however, most refinements are either briefly mentioned as implementation details or only visible in source code. In this paper, we will examine a collection of such refinements and empirically evaluate their impact on the final model accuracy through ablation study. We will show that, by combining these refinements together, we are able to improve various CNN models significantly. For example, we raise ResNet-50's top-1 validation accuracy from 75.3% to 79.29% on ImageNet. We will also demonstrate that improvement on image classification accuracy leads to better transfer learning performance in other application domains such as object detection and semantic segmentation.

**Paper Link**: [https://arxiv.org/abs/1812.01187](https://arxiv.org/abs/1812.01187 "https://arxiv.org/abs/1812.01187")

***

_This paper will be taken up by two separate groups._

**Task:**

Both groups have to show their results on two different datasets (both available at [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette "https://github.com/fastai/imagenette")):  
1\. Imagenette (a simpler, easy subset of Imagenet)

2. Imagewoof (a relatively harder subset of Imagenet)

Each group has to implement all the methods mentioned for them and show the improvements in metrics for each added tweak to the model training process.

Tasks for group 1:

1. Learning Rate Warmup
2. FP16 Training
3. Mixup Data Augmentation
4. Zero Gamma For Batchnorm

Tasks for group 2:

1. Cosine Learning Rate Decay
2. Label Smoothing
3. No Bias Decay
4. Resnet-D (Model Tweak)

**Dataset:**

Both groups have to show their results on two different datasets (both available at [https://github.com/fastai/imagenette](https://github.com/fastai/imagenette "https://github.com/fastai/imagenette")):  
1\. Imagenette (a simpler, easy subset of Imagenet)

2. Imagewoof (a relatively harder subset of Imagenet)

Bonus: After implementing the tasks assigned to you, try and implement the tweaks assigned to the other group if you have time left.

**Framework Restriction:** You cannot use FastAI. Any other library is allowed.