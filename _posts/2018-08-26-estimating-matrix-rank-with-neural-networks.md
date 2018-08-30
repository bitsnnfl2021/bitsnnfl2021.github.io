---
layout: post
share: true
title: Estimating Matrix Rank With Neural Networks
date: 2018-08-26 04:38:53 +0530
author:
  name: Aditya Rana
  email: f2016182@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Medium
- Hard

---
The visual estimation of the rank of a matrix has eluded researchers across a myriad of disciplines many years. The rank of a matrix M reveals a great deal. By definition, it tells us how many linearly independent columns the matrix has; surprisingly, it also tells us how many linearly independent rows the matrix has, and if that does not get you excited, I do not know what will. If we think of M as an operator, the rank tells us about the dimensionality of its output, and thus for a square matrix, whether M is invertible.

In this paper, we demonstrate the successful visual estimation of a matrix’s rank by treating it as a classification problem. When tested on a dataset of tens-of-thousands of colormapped matrices of varying ranks, we not only achieve state-of-the-art performance, but also distressingly high performance on an absolute basis.

Link: [http://oneweirdkerneltrick.com/rank.pdf](http://oneweirdkerneltrick.com/rank.pdf "http://oneweirdkerneltrick.com/rank.pdf")

ID : 36