---
layout: post
share: true
title: 'Dynamic Routing Between Capsules (Paper ID: 131)'
author:
  name: Parth Patel
  email: f2016150@pilani.bits-pilani.ac.in
categories:
- Capsule Nets
- Computer Vision
tags:
- Medium
date: 2019-10-08 06:21:58 +0000

---
**Abstract:** A capsule is a group of neurons whose activity vector represents the instantiation parameters of a specific type of entity such as an object or an object part. We use the length of the activity vector to represent the probability that the entity exists and its orientation to represent the instantiation parameters. Active capsules at one level make predictions, via transformation matrices, for the instantiation parameters of higher-level capsules. When multiple predictions agree, a higher level capsule becomes active. We show that a discrimininatively trained, multi-layer capsule system achieves state-of-the-art performance on MNIST and is considerably better than a convolutional net at recognizing highly overlapping digits. To achieve these results we use an iterative routing-by-agreement mechanism: A lower-level capsule prefers to send its output to higher level capsules whose activity vectors have a big scalar product with the prediction coming from the lower-level capsule.

**Paper Link:** [https://arxiv.org/pdf/1710.09829.pdf](https://arxiv.org/pdf/1710.09829.pdf)

**Guidelines/Tasks:**

1. Implement the architecture given in the paper using PyTorch with the following modifications: 
- In the given paper, the enoder consists of 3 layers: Convolutional Layer, PrimaryCaps Layer (which is basically a convolutional layer) and a Capsule Layer(DigitCaps layer). You need to have one more capsule layer between PrimaryCaps layer and DigitCaps layer. 
- In the given paper, the decoder consists of 3 fully connected (F.C.) layers. You can experiment with having 4 or more F.C. layers in the decoder as for STL-10 dataset (mentioned below), we need to reconstruct a larger 96x96 image as opposed to 28x28 for MNIST.
2. Use STL-10 dataset for training and validation. Note that you can easily access this dataset using PyTorch. Divide the dataset into train and validation sets. Report accuracy on the validation dataset. Since its not a very large dataset, you may perform image augmentation techniques.

**ID :** 131
