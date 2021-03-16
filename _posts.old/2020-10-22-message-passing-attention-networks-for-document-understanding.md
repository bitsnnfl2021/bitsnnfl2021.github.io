---
layout: post
author:
  name: Paper ID 82
  difficulty: Medium
share: true
title: Message Passing Attention Networks for Document Understanding
categories:
- Graph neural network
- Attention
- NLP
- Document Classification
tags: []

---
**Abstract** - Graph neural networks have recently emerged as a very effective framework for processing graph-structured data. These models have achieved state-of-the-art performance in many tasks. Most graph neural networks can be described in terms of message passing, vertex update, and readout functions. In this paper, we represent documents as word co-occurrence networks and propose an application of the message passing framework to NLP, the Message Passing Attention network for Document understanding (MPAD). We also propose several hierarchical variants of MPAD. Experiments conducted on 10 standard text classification datasets show that our architectures are competitive with the state-of-the-art. Ablation studies reveal further insights about the impact of the different components on performance. Code is publicly available at: [this https URL](https://github.com/giannisnik/mpad) .

**Paper** - [https://arxiv.org/pdf/1908.06267.pdf](https://arxiv.org/pdf/1908.06267.pdf "https://arxiv.org/pdf/1908.06267.pdf")

**Dataset -** Reuters (available in nltk). Alternatively: [https://www.kaggle.com/nltkdata/reuters](https://www.kaggle.com/nltkdata/reuters "https://www.kaggle.com/nltkdata/reuters")