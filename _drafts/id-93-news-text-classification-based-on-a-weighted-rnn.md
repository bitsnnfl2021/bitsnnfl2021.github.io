---
layout: post
author:
  name: 'Paper ID: 21'
  email: bitsnnfl@gmail.com
share: true
title: "[ID_93]  News text classification based on a Weighted RNN"
categories:
- NLP
- RNN
tags: []

---
**Abstract** - Most of the information is stored as text, so text mining is regarded as having high commercial potential. Aiming at the semantic constraint problem of classification methods based on sparse representation, we propose a weighted recurrent neural network (W-RNN), which can fully extract text serialization semantic information. For the problem that the feature high dimensionality and unclear semantic relationship in text data representation, we first utilize the word vector to represent the vocabulary in the text and use Recurrent Neural Network (RNN) to extract features of the serialized text data. The word vector is then automatically weighed and summed using the intermediate output of the word vector to form the text representation vector. Finally, the neural network is used for classification. W-RNN is verified on the news dataset and proves that W-RNN is superior to the other four baseline methods in Precision, Recall, F1 and loss values, which is suitable for text classification.

**Paper** - [https://arxiv.org/ftp/arxiv/papers/1909/1909.13077.pdf](https://arxiv.org/ftp/arxiv/papers/1909/1909.13077.pdf "https://arxiv.org/ftp/arxiv/papers/1909/1909.13077.pdf")

**Dataset** - [http://qwone.com/\~jason/20Newsgroups/](http://qwone.com/\~jason/20Newsgroups/ "http://qwone.com/~jason/20Newsgroups/") (Use the [20news-bydate.tar.gz](http://qwone.com/\~jason/20Newsgroups/20news-bydate.tar.gz) version)

**Problem Statement -**

1. Implement the paper using Keras and Tensorflow. Split the training and testing set as given in the paper and then develop the model. Clearly report the number of data samples of each category in training and testing sets.
2. Use GRU blocks as the RNN units while developing the model. Use early stopping with respect to cross-validation loss as stopping criteria.
3. Show comparison with replacing the GRU unit by LSTM unit in the above model, and with baseline GRU-based RNN model. Clearly report the difference in terms of accuracy, convergence rate of loss function and avg time per epoch.
4. Report graph of loss function & accuracy vs. epochs, confusion matrix, precision, recall, F1 score, and accuracy for all three cases.