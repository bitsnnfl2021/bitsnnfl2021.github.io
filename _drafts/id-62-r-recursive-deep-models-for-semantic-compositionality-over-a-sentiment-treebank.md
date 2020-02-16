---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_62] Recursive Deep Models for Semantic Compositionality Over a Sentiment
  Treebank"
categories:
- Sentiment Analysis
tags: []

---
Semantic word spaces have been very useful but cannot express the meaning of longer phrases in a principled way. Further progress towards understanding compositionality in tasks such as sentiment detection requires richer supervised training and evaluation resources and more powerful models of composition. To remedy this, we introduce a Sentiment Treebank. It includes fine grained sentiment labels for 215,154 phrases in the parse trees of 11,855 sentences and presents new challenges for sentiment compositionality. To address them, we introduce the Recursive Neural Tensor Network. When trained on the new treebank, this model outperforms all previous methods on several metrics. It pushes the state of the art in single sentence positive/negative classification from 80% up to 85.4%. The accuracy of predicting fine-grained sentiment labels for all phrases reaches 80.7%, an improvement of 9.7% over bag of features baselines. Lastly, it is the only model that can accurately capture the effects of negation and its scope at various tree levels for both positive and negative phrases.

Paper: [https://www.aclweb.org/anthology/D13-1170.pdf](https://www.aclweb.org/anthology/D13-1170.pdf "https://www.aclweb.org/anthology/D13-1170.pdf")

[Dataset](http://nlp.stanford.edu/sentiment "Dataset")

Tasks:

1. Implement the Recursive Neural Tensor Network as mentioned in the paper.
2. Implement a data-autoloader for text.
3. Try achieving the same accuracy measures as in the paper.

ID: 62