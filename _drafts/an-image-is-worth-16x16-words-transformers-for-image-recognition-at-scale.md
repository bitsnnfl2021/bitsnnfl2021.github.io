---
layout: post
author:
  name: Paper ID 27
  difficulty: Medium
share: true
title: 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale'
categories:
- GELU
- Dropout
- Transformer
- Image Recognition
tags: []

---
**Abstract** - While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer can perform very well on image classification tasks when applied directly to sequences of image patches. When pre-trained on large amounts of data and transferred to multiple recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer attain excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.

**Paper** - [https://openreview.net/pdf?id=YicbFdNTTy](https://openreview.net/pdf?id=YicbFdNTTy "https://openreview.net/pdf?id=YicbFdNTTy")

**Dataset -** [https://www.tensorflow.org/datasets/catalog/imagenet2012](https://www.tensorflow.org/datasets/catalog/imagenet2012 "https://www.tensorflow.org/datasets/catalog/imagenet2012")