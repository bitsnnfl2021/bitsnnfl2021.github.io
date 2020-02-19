---
layout: post
author:
  name: 'Paper ID: 41'
  email: bitsnnfl@gmail.com
share: true
title: Neural Machine Translation by Jointly Learning to Align and Translate
categories:
- Natural Language Processing
- LSTM
- Attention
- Neural Machine Translation
tags: []

---
ABSTRACT - Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encoder source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder-decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts like a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

Paper Link: [https://arxiv.org/abs/1409.0473](https://arxiv.org/abs/1409.0473 "https://arxiv.org/abs/1409.0473")

Paper Link for GloVe : [https://nlp.stanford.edu/pubs/glove.pdf](https://nlp.stanford.edu/pubs/glove.pdf "https://nlp.stanford.edu/pubs/glove.pdf")

Conference: ICLR 2015

Dataset: Train ([English](https://nlp.stanford.edu/projects/nmt/data/iwslt15.en-vi/train.en), [Vietnamese](https://nlp.stanford.edu/projects/nmt/data/iwslt15.en-vi/train.vi))

Dataset: Test ([English](https://nlp.stanford.edu/projects/nmt/data/iwslt15.en-vi/tst2013.en), [Vietnamese](https://nlp.stanford.edu/projects/nmt/data/iwslt15.en-vi/tst2013.vi))

**Task:**

1. Preprocess the data from the English and Vietnamese corpus and pick the top 100k words from both.

   a) For English words that exist in GloVe, use pre-trained GloVe word embeddings as their initialization and for those that don't exist, initialize them with random valued vectors. Keep all the vectors trainable.

   b) For Vietnamese, initialize the vectors with random values and keep them trainable.
2. Create the bi-directional LSTM model with attention in Pytorch from Scratch
3. Make sure to write functions to plot attention matrices as shown in Figure 3 of the paper for any input/output given to your model.

**ID:** 41