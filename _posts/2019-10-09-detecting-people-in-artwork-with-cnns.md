---
layout: post
share: true
title: 'Detecting People in Artwork with CNNs (Paper ID: 171)'
author:
  name: Aditi Agarwal
  email: f2016095@pilani.bits-pilani.ac.in
categories:
- CNN
- Object Detection
tags:
- Hard
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** CNNs have massively improved performance in object detection in photographs. However research into object detection in artwork remains limited. We show state-of-the-art performance on a challenging dataset,People-Art,  which  contains  people  from  photos,  cartoons  and 41  different artwork  movements.  We  achieve  this  high  performance  byfine-tuning a CNN for this task, thus also demonstrating that trainingCNNs on photos results in overfitting for photos: only the first three or four layers transfer from photos to artwork. Although the CNN’s perfor-mance is the highest yet, it remains less than 60% AP, suggesting furtherwork is needed for the cross-depiction problem.

**Paper Link:** [https://arxiv.org/pdf/1610.08871v1.pdf](https://arxiv.org/pdf/1610.08871v1.pdf)

**ID:** 171

**Guidelines:**

1. Implement the full architecture.
2. Use CaffeNet  and VGG1024 for pretraining and fcompare their validation results.
3. Compare default, gap, all-neg, gap+all-neg, configuration for fine tuning for the above models and compare them.

**Dataset Link**: [https://github.com/BathVisArtData/PeopleArt/tree/master/JPEGImages](https://github.com/BathVisArtData/PeopleArt/tree/master/JPEGImages)

