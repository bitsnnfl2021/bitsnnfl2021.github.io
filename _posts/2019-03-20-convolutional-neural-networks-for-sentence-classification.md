---
layout: post
share: true
title: 'Convolutional Neural Networks for Sentence Classification (Paper ID: 65)'
author:
  name: Kabir Ahuja
  email: f2015791@pilani.bits-pilani.ac.in
categories:
- NLP
tags:
- Easy
date: 2019-03-20 10:44:03 +0000

---
**Abstract:** We report on a series of experiments with convolutional neural networks (CNN) trained on top of pre-trained word vectors for sentence-level classification tasks. We show that a simple CNN with little hyperparameter tuning and static vectors achieves excellent results on multiple benchmarks. Learning task-specific vectors through fine-tuning offers further gains in performance. We additionally propose a simple modification to the architecture to allow for the use of both task-specific and static vectors. The CNN models discussed herein improve upon the state of the art on 4 out of 7 tasks, which include sentiment analysis and question classification.

**Paper Link:** [https://arxiv.org/pdf/1408.5882.pdf](https://arxiv.org/pdf/1408.5882.pdf)

**Paper ID: 65**

**Guidelines**:

1\. Implement all the model variants as given in setion 3.3 and compare their performance in terms of accuracy.

2\. Train on atleast 2 different datasets given in section 3

3\. As a sanity check train on 50 sentences first and see if the model can overfit i.e get close to 100% accuracy on those 50 sentences.

4\. Also train a baseline model which averages word vectors of all the words in the sentence and train a single layer neural network on the obtained vector to classify the sentence. Compare its performance with your cnn models. The accuracy obtained by your models should be more than this baseline.
