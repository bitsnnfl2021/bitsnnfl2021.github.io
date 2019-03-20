---
layout: post
share: true
title: 'Show, Attend and Tell: Neural Image Caption Generation with Visual Attention'
author:
  name: Kabir Ahuja
  email: f2015791@pilani.bits-pilani.ac.in
categories:
- Computer Vision
- NLP
tags: []
date: 2019-03-20 10:39:35 +0000

---
**Abstract**: Inspired by recent work in machine translation and object detection, we introduce an attention based model that automatically learns to describe the content of images. We describe how we can train this model in a deterministic manner using standard backpropagation techniques and stochastically by maximizing a variational lower bound. We also show through visualization how the model is able to automatically learn to fix its gaze on salient objects while generating the corresponding words in the output sequence. We validate the use of attention with state-of-the-art performance on three benchmark datasets: Flickr8k, Flickr30k and MS COCO.

**Paper Link**: [https://arxiv.org/abs/1502.03044](https://arxiv.org/abs/1502.03044 "https://arxiv.org/abs/1502.03044")

**Guidelines**:

1\. Implement the full model architecture as defined in section 3 of the paper. (edited) 

2\. Implement the attention mechanism as described in section 3, you can skip the attention methods described in section 4.

3\. Use Flickr 8k dataset or Caltech Bird dataset (http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) instead of coco since these are much smaller data sets and it will be easier to train on them.