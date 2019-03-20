---
layout: post
share: true
title: Skip-Thought Vectors
author:
  name: Kabir Ahuja
  email: f2015791@pilani.bits-pilani.ac.in
categories:
- NLP
tags:
- Medium
date: 2019-03-20 10:48:13 +0000

---
**Abstract:** We describe an approach for unsupervised learning of a generic, distributed sentence encoder. Using the continuity of text from books, we train an encoder-decoder model that tries to reconstruct the surrounding sentences of an encoded passage. Sentences that share semantic and syntactic properties are thus mapped to similar vector representations. We next introduce a simple vocabulary expansion method to encode words that were not seen as part of training, allowing us to expand our vocabulary to a million words. After training our model, we extract and evaluate our vectors with linear models on 8 tasks: semantic relatedness, paraphrase detection, image-sentence ranking, question-type classification and 4 benchmark sentiment and subjectivity datasets. The end result is an off-the-shelf encoder that can produce highly generic sentence representations that are robust and perform well in practice. We will make our encoder publicly available.

**Paper Link:** [https://arxiv.org/abs/1506.06726](https://arxiv.org/abs/1506.06726 "https://arxiv.org/abs/1506.06726")

**Guidelines**:

1\. Train the encoder decoder networks for learning skip thought vectors of sentences.

2\. After training use the encoder to obtain the nearest neighbors of different sentences scored by cosine similarity as in table 2 of the paper.

3\. Use the skip thought vectors on at least 2 tasks out of 8 mentioned in paper: semantic relatedness,

paraphrase detection, image-sentence ranking, question-type classification and benchmark sentiment and subjectivity datasets.