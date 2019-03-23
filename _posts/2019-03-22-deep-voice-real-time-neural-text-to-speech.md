---
layout: post
share: true
title: 'Deep Voice: Real-time Neural Text-to-Speech'
author:
  name: Akash Sonth
  email: f2015265@pilani.bits-pilani.ac.in
categories:
- NLP
- Speech
tags: []
date: 2019-03-22 16:06:44 +0000

---
**Abstract:** We present Deep Voice, a production-quality text-to-speech system constructed entirely from deep neural networks. Deep Voice lays the groundwork for truly end-to-end neural speech synthesis. The system comprises five major building blocks: a segmentation model for locating phoneme boundaries, a grapheme-to-phoneme conversion model, a phoneme duration prediction model, a fundamental frequency prediction model, and an audio synthesis model. For the segmentation model, we propose a novel way of performing phoneme boundary detection with deep neural networks using connectionist temporal classification (CTC) loss. For the audio synthesis model, we implement a variant of WaveNet that requires fewer parameters and trains faster than the original. By using a neural network for each component, our system is simpler and more flexible than traditional text-to-speech systems, where each component requires laborious feature engineering and extensive domain expertise. Finally, we show that inference with our system can be performed faster than real time and describe optimized WaveNet inference kernels on both CPU and GPU that achieve up to 400x speedups over existing implementations.

**Paper Link:** [https://arxiv.org/pdf/1702.07825.pdf](https://arxiv.org/pdf/1702.07825.pdf "https://arxiv.org/pdf/1702.07825.pdf")

**Paper ID: 32**

**Guidelines:** Coming Soon!