---
layout: post
share: true
title: 'Automatic Text Scoring Using Neural Networks (Paper ID: 112)'
author:
  name: Dhaivata Pandya
  email: f2016020@pilani.bits-pilani.ac.in
categories:
- LSTM
- Architecture
tags:
- Medium
date: 2019-03-22 00:54:11 +0000

---
**Abstract:** Automated Text Scoring (ATS) provides a cost-effective and consistent alternative to human marking. However, in order to achieve good performance, the predictive features of the system need to be manually engineered by human experts. We introduce a model that forms word representations by learning the extent to which specific words contribute to the text’s score. Using Long-Short Term Memory networks to represent the meaning of texts, we demonstrate that a fully automated framework is able to achieve excellent results over similar approaches. In an attempt to make our results more interpretable, and inspired by recent advances in visualising neural networks, we introduce a novel method for identifying the regions of the text that the model has found more discriminative.

**Paper Link:** [https://arxiv.org/pdf/1606.04289.pdf](https://arxiv.org/pdf/1606.04289.pdf "https://arxiv.org/pdf/1606.04289.pdf")

**Tasks:**

1. Learn the SSWE as mentioned in section 3.2 of the paper. You can augment the existing C&W model as mentioned in the paper. (If you are new to word embeddings, you can watch this Stanford lecture: [https://www.youtube.com/watch?v=ERibwqs9p38&t=2s](https://www.youtube.com/watch?v=ERibwqs9p38&t=2s "https://www.youtube.com/watch?v=ERibwqs9p38&t=2s") to learn more about them)
2. Train the LSTM or BLSTM layers on top of the augmented word embeddings to reproduce the accuracy as represented in table 1 of the paper.
3. Bonus: Use pre-trained word2vec embeddings to compare the accuracy.
4. Preferably use Torch to implement the paper.

**ID:** 112  
