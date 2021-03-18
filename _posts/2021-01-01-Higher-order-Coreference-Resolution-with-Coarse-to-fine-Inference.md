---
layout: post
author:
  name: Paper ID 22
  difficulty: medium
share: true
title: Higher-order-Coreference-Resolution-with-Coarse-to-fine-Inference
categories:
- conference resoultion
- nlp
tags: []

---
**Abstract** - We introduce a fully differentiable approxima-tion to higher-order inference for coreferenceresolution. Our approach uses the antecedentdistribution from a span-ranking architectureas an attention mechanism to iteratively re-fine span representations. This enables themodel to softly consider multiple hops in thepredicted clusters. To alleviate the computa-tional cost of this iterative process, we intro-duce a coarse-to-fine approach that incorpo-rates a less accurate but more efficient bilin-ear factor, enabling more aggressive pruningwithout hurting accuracy. Compared to the ex-isting state-of-the-art span-ranking approach,our model significantly improves accuracy onthe English OntoNotes benchmark, while be-ing far more computationally efficient

**Paper** - [https://arxiv.org/pdf/1804.05392.pdf](https://arxiv.org/pdf/1804.05392.pdf)

**Dataset -** [https://github.com/kentonl/e2e-coref](https://github.com/kentonl/e2e-coref)
    