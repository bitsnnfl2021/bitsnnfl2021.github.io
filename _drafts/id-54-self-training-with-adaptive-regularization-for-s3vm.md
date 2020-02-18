---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_54] ImageNet Classification with Deep Convolutional Neural Networks"
categories:
- CNN
- Overfitting
- Classification
tags: []

---
**Abstract:** We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art. The neural network, which has 60 million parameters and 650,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and three fully-connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of the convolution operation. To reduce overfitting in the fully-connected layers we employed a recently-developed regularization method called “dropout” that proved to be very effective. We also entered a variant of this model in the ILSVRC-2012 competition and achieved a winning top-5 test error rate of 15.3%, compared to 26.2% achieved by the second-best entry

**Paper Link:** [https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf "https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf")

**Published in:** [Advances in neural information processing systems](https://www.researchgate.net/journal/1049-5258_Advances_in_neural_information_processing_systems)

**Tasks:**

1. Implelement the model given in the paper using Tensorflow
2. Use a subset of the given dataset and apply augmentation techniques as specified in the paper. Clearly specify which subset is being used. Also, split the dataset for training and testing purposes.
3. Report the top-1 and top-5 test set error rates in your final report. 

**Data Set:** ILSVRC-2010 ([http://www.image-net.org/challenges/LSVRC/2010/](http://www.image-net.org/challenges/LSVRC/2010/ "http://www.image-net.org/challenges/LSVRC/2010/")

**Paper ID:** 54