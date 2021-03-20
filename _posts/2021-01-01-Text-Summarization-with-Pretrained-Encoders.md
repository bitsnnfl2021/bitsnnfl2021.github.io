---
layout: post
author:
  name: Paper ID 56
  difficulty: Difficulty - Medium
share: true
title: Text Summarization with Pretrained Encoders
categories:
- Natural Language Processing
- Summarization
- medium

tags: []

---
**Abstract** - Bidirectional Encoder Representations from Transformers (BERT) represents the latest incarnation of pretrained language models which have recently advanced a wide range of natural language processing tasks. In this paper, we showcase how BERT can be usefully applied in text summarization and propose a general framework for both extractive and abstractive models. We introduce a novel document-level encoder based on BERT which is able to express the semantics of a document and obtain representations for its sentences. Our extractive model is built on top of this encoder by stacking several inter-sentence Transformer layers. For abstractive summarization, we propose a new fine-tuning schedule which adopts different optimizers for the encoder and the decoder as a means of alleviating the mismatch between the two (the former is pretrained while the latter is not). We also demonstrate that a two-staged fine-tuning approach can further boost the quality of the generated summaries. Experiments on three datasets show that our model achieves state-of-the-art results across the board in both extractive and abstractive settings

**Paper** - [https://arxiv.org/abs/1908.08345v2](https://arxiv.org/abs/1908.08345v2)

**Dataset -** [https://www.tensorflow.org/datasets/catalog/cnn_dailymail](https://www.tensorflow.org/datasets/catalog/cnn_dailymail)

[ https://paperswithcode.com/dataset/new-york-times-annotated-corpus]( https://paperswithcode.com/dataset/new-york-times-annotated-corpus)

[ https://www.tensorflow.org/datasets/catalog/xsumm]( https://www.tensorflow.org/datasets/catalog/xsumm)
    