---
layout: post
author:
  name: Paper ID 25
  difficulty: Difficulty - Medium
share: true
title: Evaluating the Utility of Hand-crafted Features in Sequence Labelling∗
categories:
- Natural Language Processing
- Named Entity Recognition
- medium

tags: []

---
**Abstract** - Conventional wisdom is that hand-crafted features are redundant for deep learning models, as they already learn adequate representations of text automatically from corpora. In this work, we test this claim by proposing a new method for exploiting handcrafted features as part of a novel hybrid learning approach, incorporating a feature auto-encoder loss component. We evaluate on the task of named entity recognition (NER), where we show that including manual features for part-of-speech, word shapes and gazetteers can improve the performance of a neural CRF model. We obtain a F 1 of 91.89 for the CoNLL-2003 English shared task, which significantly outperforms a collection of highly competitive baseline models. We also present an ablation study showing the importance of auto-encoding, over using features as either inputs or outputs alone, and moreover, show including the autoencoder components reduces training requirements to 60%, while retaining the same predictive accuracy.

**Paper** - [https://arxiv.org/pdf/1808.09075v1.pdf](https://arxiv.org/pdf/1808.09075v1.pdf)

**Dataset -** [https://github.com/synalp/ner/tree/master/corpus/conll-2003](https://github.com/synalp/ner/tree/master/corpus/conll-2003)
    