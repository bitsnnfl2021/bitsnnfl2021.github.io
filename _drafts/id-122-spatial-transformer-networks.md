---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID:122]-Spatial Transformer Networks"
categories:
- CNN
- Classification
tags: []

---
**Abstract :** Convolutional Neural Networks define an exceptionally powerful class of models, but are still limited by the lack of ability to be spatially invariant to the input data in a computationally and parameter efficient manner. In this work we introduce a new learnable module, the Spatial Transformer, which explicitly allows the spatial manipulation of data within the network. This differentiable module can be inserted into existing convolutional architectures, giving neural networks the ability to actively spatially transform feature maps, conditional on the feature map itself, without any extra training supervision or modification to the optimisation process. We show that the use of spatial transformers results in models which learn invariance to translation, scale, rotation and more generic warping, resulting in state-of-the-art performance on several benchmarks, and for a number of classes of transformations.

Paper Link : [https://arxiv.org/pdf/1506.02025.pdf](https://arxiv.org/pdf/1506.02025.pdf "https://arxiv.org/pdf/1506.02025.pdf")

Conference : NIPS

**Task :**

1. Implement the model discussed in paper in three parts:
   * Localisation Network
   * Parameterised Sampling Grid
   * Differentiable Image Sampling.
2.  Implement the proper dataloader with any 2 data augmentation techniques.
3. All three of the above should be implemented separately such that they can be tested individually.
4. Test the model according to the sections 4.1 and 4.2 of the Paper.You can use any dataset available. You can also use the 2 datasets mentioned in the paper . Refer to this link for reducing the size of datasets : [https://stackoverflow.com/questions/44634007/how-to-subset-a-mnist-dataset](https://stackoverflow.com/questions/44634007/how-to-subset-a-mnist-dataset "https://stackoverflow.com/questions/44634007/how-to-subset-a-mnist-dataset")

**Dataset:** Already mentioned in 2 point of Tasks (MNIST and SVNH).