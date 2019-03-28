---
layout: post
share: true
title: 'Text classification based on deep belief network and softmax regression (Paper
  ID: 53)'
author:
  name: Harsh Jaiswal
  email: f2015525@pilani.bits-pilani.ac.in
categories:
- NLP
tags:
- Hard
date: 2019-03-22 15:58:45 +0000

---
**Abstract:** In this paper, we propose a novel hybrid text classification model based on deep belief network and softmax regression. To solve the sparse high-dimensional matrix computation problem of texts data, a deep belief network is introduced. After the feature extraction with DBN, softmax regression is employed to classify the text in the learned feature space. In pre-training procedures, the deep belief network and softmax regression are first trained, respectively. Then, in the fine-tuning stage, they are transformed into a coherent whole and the system parameters are optimized with Limited-memory Broyden– Fletcher–Goldfarb–Shanno algorithm. The experimental results on Reuters-21,578 and 20-Newsgroup corpus show that the proposed model can converge at fine-tuning stage and perform significantly better than the classical algorithms, such as SVM and KNN.

**Paper Link:** [https://link.springer.com/content/pdf/10.1007%2Fs00521-016-2401-x.pdf](https://link.springer.com/content/pdf/10.1007%2Fs00521-016-2401-x.pdf "https://link.springer.com/content/pdf/10.1007%2Fs00521-016-2401-x.pdf")

**Paper ID: 53**

**Guidelines:** Implement DBN+Softmax(2) on large scale Reuters and compare it with results obtained from knn algorithm.