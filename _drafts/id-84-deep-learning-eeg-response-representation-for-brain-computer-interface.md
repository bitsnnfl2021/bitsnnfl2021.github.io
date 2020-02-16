---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_84] Deep learning EEG response representation for brain computer interface"
categories:
- BCI
tags: []

---
**Abstract:** In this paper, the multi-scale deep convolutional neural networks are introduced to deal with the representation for imagined motor Electroencephalography (EEG) signals. We propose to learn a set of high-level feature representations through deep learning algorithm, referred to as Deep Motor Features (DeepMF), for brain computer interface (BCI) with imagined motor tasks. As the extracted DeepMF are dissimilar for different tasks and alike for the same tasks, it is convenient to separate the diverse EEG signals for imagined motor tasks apart. Our approach achieves 100% accuracy for 4 classes imagined motor EEG signals classification on Project BCI - EEG motor activity dataset. Moreover, thanks to the highly abstract features DeepMF learned, only 4.125 seconds trials of training data are needed, compared with the conventional BLDA algorithm for 8.75 seconds trials demand to achieve the same accuracy, accordingly the BCI response time and the required trials for training are almost declined by half. Experiments are provided to illustrate the effectiveness of the proposed design approach.

Paper Link: [file:///home/jivat/Downloads/jingwei2015%20(1).pdf](file:///home/jivat/Downloads/jingwei2015%20(1).pdf) **(modify)**

Conference : Chinese Control Conference

**Task:**

1\.  Perform pre-processing as mentioned in section 2.

2\. Design the CNN architecture in Figure 1 as described in section 3.2

3\. Design the CNN architecture by directly connecting the output of the third pooling layer to the hidden layer as shown in Fig.11

4\. Compare the performance of the above two architectures in (2) and (3).

**Dataset**: Project BCI - EEG motor activity dataset **(Add link)**

**ID:** 84