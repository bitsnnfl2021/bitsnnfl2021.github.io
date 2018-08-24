---
layout: post
share: true
title: Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine
  Translation
date: 2018-08-24 12:50:59 +0530
author:
  name: Anmol Singhal
  email: f2015069@pilani.bits-pilani.ac.in
categories:
- Basic Architecture
tags:
- Medium

---
In this paper, we propose a novel neural network model called RNN Encoder– Decoder that consists of two recurrent neural networks (RNN). One RNN encodes a sequence of symbols into a fixedlength vector representation, and the other decodes the representation into another sequence of symbols. The encoder and decoder of the proposed model are jointly trained to maximize the conditional probability of a target sequence given a source sequence. The performance of a statistical machine translation system is empirically found to improve by using the conditional probabilities of phrase pairs computed by the RNN Encoder–Decoder as an additional feature in the existing log-linear model. Qualitatively, we show that the proposed model learns a semantically and syntactically meaningful representation of linguistic phrases.

[Link](https://arxiv.org/abs/1406.1078)