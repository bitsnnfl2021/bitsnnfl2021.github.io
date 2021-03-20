---
layout: post
author:
  name: Paper ID 50
  difficulty: Difficulty - Medium
share: true
title: Deep Pyramid Convolutional Neural Networks for Text Categorization
categories:
- Natural Language Processing
- Classification
- medium

tags: []

---
**Abstract** - This paper proposes a low-complexity word-level deep convolutional neural network (CNN) architecture for text categorization that can efficiently represent long-range associations in text. In the literature, several deep and complex neural networks have been proposed for this task, assuming availability of relatively large amounts of training data. However, the associated computational complexity increases as the networks go deeper, which poses serious challenges in practical applications. Moreover, it was shown recently that shallow word-level CNNs are more accurate and much faster than the state-of-the-art very deep nets such as character-level CNNs even in the setting of large training data. Motivated by these findings, we carefully studied deepening of word-level CNNs to capture global representations of text, and found a simple network architecture with which the best accuracy can be obtained by increasing the network depth without increasing computational cost by much. We call it deep pyramid CNN. The proposed model with 15 weight layers outperforms the previous best models on six benchmark datasets for sentiment classification and topic categorization.

**Paper** - [https://pdfs.semanticscholar.org/2f79/66bd3bc7aaf64c7db40fb7f3309f5207cbf7.pdf?_ga=2.81462615.1581587070.1564247907-742172260.1564247907](https://pdfs.semanticscholar.org/2f79/66bd3bc7aaf64c7db40fb7f3309f5207cbf7.pdf?_ga=2.81462615.1581587070.1564247907-742172260.1564247907)

**Dataset -** [yelp full review dataset -https://s3.amazonaws.com/fast-ai-nlp/yelp_review_full_csv.tgz](yelp full review dataset -https://s3.amazonaws.com/fast-ai-nlp/yelp_review_full_csv.tgz)
    