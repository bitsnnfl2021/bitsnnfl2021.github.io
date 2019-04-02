---
layout: post
share: true
title: 'Ask Me Anything: Dynamic Memory Networks for Natural Language Processing (Paper
  ID: 82)'
author:
  name: Sanskriti Sharma
  email: f2015553@pilani.bits-pilani.ac.in
categories:
- NLP
- QA
- 'Question Answering Systems '
tags:
- Medium
date: 2019-03-23 10:00:54 +0000

---
**Abstract:** Most tasks in natural language processing can be cast into question answering (QA) problems over language input. We introduce the dynamic memory network (DMN), a unified neural network framework which processes input sequences and questions, forms semantic and episodic memories, and generates relevant answers. Questions trigger an iterative attention process which allows the model to condition its attention on the result of previous iterations. These results are then reasoned over in a hierarchical recurrent sequence model to generate answers. The DMN can be trained end-to-end and obtains state of the art results on several types of tasks and datasets: question answering (Facebook’s bAbI dataset), sequence modeling for part of speech tagging (WSJ-PTB), and text classification for sentiment analysis (Stanford Sentiment Treebank). The model relies exclusively on trained word vector representations and requires no string matching or manually engineered features.

**Paper Link:** [https://arxiv.org/pdf/1506.07285v1.pdf](https://arxiv.org/pdf/1506.07285v1.pdf "https://arxiv.org/pdf/1506.07285v1.pdf")

**ID:** 82

**Guidelines:** 

1. Implement the full architecture as given in the paper.
2. Use LSTMs instead of GRUs and word2vec instead of Glove vectors in your implementation.
3. Its compulsory to train a model on the task 4.1. Out of 4.2 and 4.3 you can train your model on one of them only.
4. For the above tasks first try to train on a very small number of examples (50-100) and see if the network is able to overfit on those examples.
5. Report your results in terms of accuracy.