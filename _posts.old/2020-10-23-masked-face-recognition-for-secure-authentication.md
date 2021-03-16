---
layout: post
author:
  name: Paper ID 38
  difficulty: Medium
share: true
title: Masked Face Recognition for Secure Authentication
categories:
- Deep Learning
- CNN
tags: []

---
**Abstract** - With the recent world-wide COVID-19 pandemic, using face masks have become an important part of our lives. People are encouraged to cover their faces when in public area to avoid the spread of infection. The use of these face masks has raised a serious question on the accuracy of the facial recognition system used for tracking school/office attendance and to unlock phones. Many organizations use facial recognition as a means of authentication and have already developed the necessary datasets in-house to be able to deploy such a system. Unfortunately, masked faces make it difficult to be detected and recognized, thereby threatening to make the in-house datasets invalid and making such facial recognition systems inoperable. This paper addresses a methodology to use the current facial datasets by augmenting it with tools that enable masked faces to be recognized with low false-positive rates and high overall accuracy, without requiring the user dataset to be recreated by taking new pictures for authentication. We present an opensource tool, MaskTheFace to mask faces effectively creating a large dataset of masked faces. The dataset generated with this tool is then used towards training an effective facial recognition system with target accuracy for masked faces. We report an increase of ∼ 38% in the true positive rate for the Facenet system. We also test the accuracy of re-trained system on a custom real-world dataset MFR2 and report similar accuracy.

**Paper** - [https://arxiv.org/pdf/2008.11104v1.pdf](https://arxiv.org/pdf/2008.11104v1.pdf "https://arxiv.org/pdf/2008.11104v1.pdf")

**Dataset** - [https://github.com/aqeelanwar/MaskTheFace/tree/master/datasets](https://github.com/aqeelanwar/MaskTheFace/tree/master/datasets "https://github.com/aqeelanwar/MaskTheFace/tree/master/datasets")