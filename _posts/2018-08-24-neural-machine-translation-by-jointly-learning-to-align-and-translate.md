---
layout: post
share: true
title: " Neural Machine Translation by Jointly Learning to Align and Translate"
date: 2018-08-24 12:41:23 +0530
author:
  name: Anmol Singhal
  email: f2015069@pilani.bits-pilani.ac.in
categories:
- Deep Learning
- Encoder Decoder
tags:
- Hard

---
Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder-decoders and consists of an encoder that encodes a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder-decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

[Link](https://arxiv.org/abs/1409.0473)