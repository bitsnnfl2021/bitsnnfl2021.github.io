---
layout: post
author:
  name: Paper ID 5
  difficulty: Medium
share: true
title: Zero-Shot Knowledge Distillation in Deep Networks
categories:
- Zero-Shot Learning
tags: []

---
**Abstract** - Knowledge distillation deals with the problem of training a smaller model (Student) from a high capacity source model (Teacher) so as to retain most of its performance. Existing approaches use either the training data or meta-data extracted from it in order to train the Student. However, accessing the dataset on which the Teacher has been trained may not always be feasible if the dataset is very large or it poses privacy or safety concerns (e.g., bio-metric or medical data). Hence, in this paper, we propose a novel data-free method to train the Student from the Teacher. Without even using any meta-data, we synthesize the Data Impressions from the complex Teacher model and utilize these as surrogates for the original training data samples to transfer its learning to Student via knowledge distillation. We, therefore, dub our method “ZeroShot Knowledge Distillation” and demonstrate that our framework results in competitive generalization performance as achieved by distillation using the actual training data samples on multiple benchmark datasets 

**Paper** - [http://proceedings.mlr.press/v97/nayak19a/nayak19a.pdf](http://proceedings.mlr.press/v97/nayak19a/nayak19a.pdf "http://proceedings.mlr.press/v97/nayak19a/nayak19a.pdf") 

**Dataset** - [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/ "http://yann.lecun.com/exdb/mnist/")