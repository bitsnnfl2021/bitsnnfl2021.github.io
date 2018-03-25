---
layout: post
share: true
title: 'GloVe: Global Vectors for Word Representation'
date: 2018-03-25 23:42:48 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- " Natural Language Processing"
tags:
- Medium
- Theory
---
**Abstract:** Recent methods for learning vector space representations of words have succeeded in capturing fine-grained semantic and syntactic regularities using vector arithmetic, but the origin of these regularities has remained opaque. We analyze and make explicit the model properties needed for such regularities to emerge in word vectors. The result is a new global logbilinear regression model that combines the advantages of the two major model families in the literature: global matrix factorization and local context window methods. Our model efficiently leverages statistical information by training only on the nonzero elements in a word-word cooccurrence matrix, rather than on the entire sparse matrix or on individual context windows in a large corpus. The model produces a vector space with meaningful substructure, as evidenced by its performance of 75% on a recent word analogy task. It also outperforms related models on similarity tasks and named entity recognition.

**Paper Link:** [https://nlp.stanford.edu/pubs/glove.pdf](https://nlp.stanford.edu/pubs/glove.pdf "https://nlp.stanford.edu/pubs/glove.pdf")

**Task:** Implement the core algorithm in python using Tensorflow, Pytorch, MXNet or NumPy. The submitted code would be checked for similarity with the implementations available online. Train the network on word analogy dataset.