---
layout: post
author:
  name: Paper ID 37
  difficulty: Medium
share: true
title: Neural Machine Translation by Jointly Learning to Align and Translate
categories:
- Natural Language Processing
- Machine Translation
- Attention
- medium

tags: []

---
**Abstract** - Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encoder source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder-decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts like a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

**Paper** - [https://arxiv.org/abs/1409.0473](https://arxiv.org/abs/1409.0473)

**Dataset -** [dataset: train (english](dataset: train (english)

[ vietnamese)
dataset: test (english]( vietnamese)
dataset: test (english)

[ vietnamese)]( vietnamese))
    