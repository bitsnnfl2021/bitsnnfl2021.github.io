---
layout: post
share: true
title: Document Embedding with Paragraph Vectors
date: 2018-03-25 23:39:25 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- " Natural Language Processing"
tags:
- Theory
- Medium
---
**Abstract:** Paragraph Vectors has been recently proposed as an unsupervised method for learning distributed representations for pieces of texts. In their work, the authors showed that the method can learn an embedding of movie review texts which can be leveraged for sentiment analysis. That proof of concept, while encouraging, was rather narrow. Here we consider tasks other than sentiment analysis, provide a more thorough comparison of Paragraph Vectors to other document modelling algorithms such as Latent Dirichlet Allocation, and evaluate performance of the method as we vary the dimensionality of the learned representation. We benchmarked the models on two document similarity data sets, one from Wikipedia, one from arXiv. We observe that the Paragraph Vector method performs significantly better than other methods, and propose a simple improvement to enhance embedding quality. Somewhat surprisingly, we also show that much like word embeddings, vector operations on Paragraph Vectors can perform useful semantic results.

**Paper Link:** [https://arxiv.org/abs/1507.07998](https://arxiv.org/abs/1507.07998 "https://arxiv.org/abs/1507.07998")

**Task:** Implement the core algorithm in python using Tensorflow, Pytorch, MXNet or NumPy. The submitted code would be checked for similarity with the implementations available online. Train the network on Wikipedia dataset.