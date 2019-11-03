---
layout: post
share: true
title: 'Deep Convolutional Neural Networks for Sentiment Analysis of Short Texts (Paper ID: 211)'
author:
  name: Vivek Golani
  email: f2016196@pilani.bits-pilani.ac.in
categories:
- CNN
- NLP
tags:
- Medium
date: 2019-10-21 13:37:49 +0000

---
**Abstract:** Sentiment analysis of short texts such as single sentences and Twitter messages is challenging because of the limited contextual information that they normally contain. Effectively solving this task requires strategies that combine the small text content with prior knowledge and use more than just bag-of-words. In this work we propose a new deep convolutional neural network that exploits from character- to sentence-level information to perform sentiment analysis of short texts. We apply our approach for two corpora of two different domains: the Stanford Sentiment Treebank (SSTb), which contains sentences from movie reviews; and the Stanford Twitter Sentiment corpus (STS), which contains Twitter messages. For the SSTb corpus, our approach achieves state-of-the-art results for single sentence sentiment prediction in both binary positive/negative classification, with 85.7% accuracy, and fine-grained classification, with 48.3% accuracy. For the STS corpus, our approach achieves a sentiment prediction accuracy of 86.4%.

**Paper Link:** [https://www.aclweb.org/anthology/C14-1008.pdf](https://www.aclweb.org/anthology/C14-1008.pdf)

**ID:** 211

**Guidelines:**

1. Use Tensorflow, PyTorch, Keras or Theano to implement the given CharSCNN architecture given in the paper.
2. For training: either use STS or SSTb. No need to compare with other baseline models, as specified in the paper.
3. Report accuracy of your model using pre-trained word embeddings.

**Dataset Link**: [http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip](http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip)
