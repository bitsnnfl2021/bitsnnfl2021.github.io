---
layout: post
share: true
title: 'W-RNN: News text classification based on a Weighted RNN (Paper ID: 172)'
author:
  name: Aditi Agarwal
  email: f2016095@pilani.bits-pilani.ac.in
categories:
- NLP
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Most of the  information is stored as text, so text mining is regarded as having high commercial potential. Aiming at the semantic constraint problem of classification methods based on sparse representation, we propose a weighted recurrent neural network (W-RNN), which can fully extract text serialization semantic information. For the problem that the feature high dimensionality and unclear semantic relationship in text data representation, we first utilize the word vector to represent the  vocabulary in the text and use Recurrent Neural Network (RNN) to extract features of the serialized text data. The word vector is then automatically weighted and summed using the intermediate output of the word vector to form the text representation  vector. Finally, the neural network is used for classification. W-RNN is verified on the news dataset and proves that W-RNN is superior to other four baseline methods in Precision, Recall, F1 and loss values, which is suitable for text classification.

**Paper Link:** [https://arxiv.org/pdf/1909.13077.pdf](https://arxiv.org/pdf/1909.13077.pdf)

**ID:** 172

**Guidelines:**

1. For text length selection, threshold can be directly used as 0.85 and fixed text length as 300.
2. Implement the complete architecture.
3. Use regularisation and Adam Optimizer according to the guidelines given in the paper.
4. Show comparison of your model with RNN and BiRNN in terms of precision, recall, f1 measures and graph of loss function.
5. Show the classification results of atleast 15 documents in your presentation.

**Dataset Link**: [http://qwone.com/~jason/20Newsgroups/](http://qwone.com/~jason/20Newsgroups/)
