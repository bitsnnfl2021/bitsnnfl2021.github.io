---
layout: post
share: true
title: "[ID_61] Star-Transformer"
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
categories:
- Natural Language Inference
- Text Classification
tags: []

---
Although Transformer has achieved great successes on many NLP tasks, its heavy structure with fully-connected attention connections leads to dependencies on large training data. In this paper, we present StarTransformer, a lightweight alternative by careful sparsification. To reduce model complexity, we replace the fully-connected structure with a star-shaped topology, in which every two non-adjacent nodes are connected through a shared relay node. Thus, complexity is reduced from quadratic to linear, while preserving capacity to capture both local composition and long-range dependency. The experiments on four tasks (22 datasets) show that Star-Transformer achieved significant improvements against the standard Transformer for the modestly sized datasets.

Paper: [https://arxiv.org/pdf/1902.09113v2.pdf](https://arxiv.org/pdf/1902.09113v2.pdf "https://arxiv.org/pdf/1902.09113v2.pdf")

NAACL 2019

Tasks:

1. Implement the LSTM architecture in Tensorflow.
2. Show the results for Text Classification. (Dataset-SST is mentioned in the paper)
3. 