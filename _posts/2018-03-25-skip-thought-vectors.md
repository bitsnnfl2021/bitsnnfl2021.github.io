---
layout: post
share: true
title: Skip-Thought Vectors
date: 2018-03-25 23:24:44 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- " Natural Language Processing"
tags:
- Medium
- Theory
---
**Abstract:** We describe an approach for unsupervised learning of a generic, distributed sentence encoder. Using the continuity of text from books, we train an encoder-decoder model that tries to reconstruct the surrounding sentences of an encoded passage. Sentences that share semantic and syntactic properties are thus mapped to similar vector representations. We next introduce a simple vocabulary expansion method to encode words that were not seen as part of training, allowing us to expand our vocabulary to a million words. After training our model, we extract and evaluate our vectors with linear models on 8 tasks: semantic relatedness, paraphrase detection, image-sentence ranking, question-type classification and 4 benchmark sentiment and subjectivity datasets. The end result is an off-the-shelf encoder that can produce highly generic sentence representations that are robust and perform well in practice. We will make our encoder publicly available.

**Paper Link:** [https://arxiv.org/abs/1506.06726](https://arxiv.org/abs/1506.06726 "https://arxiv.org/abs/1506.06726")

**Task:** Implement the core algorithm in python using Tensorflow, Pytorch, MXNet or NumPy. The submitted code would be checked for similarity with the implementations available online. Train on SICK dataset for semantic relatedness.