---
layout: post
share: true
title: Deep Visual-Semantic Alignments for Generating Image Descriptions
author:
  name: Charu
  email: f2015825@pilani.bits-pilani.ac.in
categories:
- Image description
- RNNs
- CNNs
tags:
- Hard
date: 2019-03-19 10:10:19 +0000

---
We present a model that generates natural language descriptions of images and their regions. Our approach leverages datasets of images and their sentence descriptions to learn about the inter-modal correspondences between language and visual data. Our alignment model is based on a novel combination of Convolutional Neural Networks over image regions, bidirectional Recurrent Neural Networks over sentences, and a structured objective that aligns the two modalities through a multimodal embedding. We then describe a Multimodal Recurrent Neural Network architecture that uses the inferred alignments to learn to generate novel descriptions of image regions. We demonstrate that our alignment model produces state of the art results in retrieval experiments on Flickr8K, Flickr30K and MSCOCO datasets. We then show that the generated descriptions significantly outperform retrieval baselines on both full images and on a new dataset of region-level annotations

Link to paper: [https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Karpathy_Deep_Visual-Semantic_Alignments_2015_CVPR_paper.pdf](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Karpathy_Deep_Visual-Semantic_Alignments_2015_CVPR_paper.pdf "https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Karpathy_Deep_Visual-Semantic_Alignments_2015_CVPR_paper.pdf")

ID :122

Tasks:

1. Map every image and sentences into set of vectors.
2. Use Multi modal-RNNs to generate descriptions.
3. Do Image segment Alignment evaluation and generated descriptions: full frame evaluation only.