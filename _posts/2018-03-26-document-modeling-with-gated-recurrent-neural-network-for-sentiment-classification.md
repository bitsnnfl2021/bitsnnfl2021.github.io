---
layout: post
share: true
title: Document Modeling with Gated Recurrent Neural Network for Sentiment Classification
date: 2018-03-26 16:31:23 +0000
author:
  name: Jai Agarwal
  email: f2014428@pilani.bits-pilani.ac.in
categories:
- Natural Language Processing
tags:
- Hard
- Brownie Points
---
**Abstract:**  Document level sentiment classification remains a challenge: encoding the intrinsic relations between sentences in the semantic meaning of a document. To address this, we introduce a neural network model to learn vector-based document representation in a unified, bottom-up fashion. The model first learns sentence representation with convolutional neural network or long short-term memory. Afterwards, semantics of sentences and their relations are adaptively encoded in document representation with gated recurrent neural network. We conduct document level sentiment classification on four large-scale review datasets from IMDB and Yelp Dataset Challenge. Experimental results show that: (1) our neural model shows superior performances over several state-of-the-art algorithms; (2) gated recurrent neural network dramatically outperforms standard recurrent neural network in document modeling for sentiment classification.

**Paper Link:** [http://ir.hit.edu.cn/\~dytang/paper/emnlp2015/emnlp2015.pdf](http://ir.hit.edu.cn/\~dytang/paper/emnlp2015/emnlp2015.pdf "http://ir.hit.edu.cn/~dytang/paper/emnlp2015/emnlp2015.pdf")

**Task:** Implement the Conv-GRNN architecture in Python using Tensorflow, Pytorch, TheanoMXNet or NumPy. Train the network on IMDB dataset.

**Brownie Points:** Implement the LSTM-GRNN architecture.