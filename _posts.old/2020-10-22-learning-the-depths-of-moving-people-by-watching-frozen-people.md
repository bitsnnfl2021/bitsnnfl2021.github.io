---
layout: post
author:
  name: Paper ID 55
  difficulty: Hard
share: true
title: Learning the Depths of Moving People by Watching Frozen People
categories:
- Computer Vision
- Pattern Recognition
tags: []

---
**Abstract** - We present a method for predicting dense depth in scenarios where both a monocular camera and people in the scene are freely moving. Existing methods for recovering depth for dynamic, non-rigid objects from monocular video impose strong assumptions on the objects’ motion and may only recover sparse depth. In this paper, we take a data-driven approach and learn human depth priors from a new source of data: thousands of Internet videos of people imitating mannequins, i.e., freezing in diverse, natural poses, while a hand-held camera tours the scene. Because people are stationary, training data can be generated using multi-view stereo reconstruction. At inference time, our method uses motion parallax cues from the static areas of the scenes to guide the depth prediction. We demonstrate our method on real-world sequences of complex human actions captured by a moving hand-held camera, show improvement over stateof-the-art monocular depth prediction methods, and show various 3D effects produced using our predicted depth.

**Paper** - [https://arxiv.org/abs/1904.11111](https://arxiv.org/abs/1904.11111 "https://arxiv.org/abs/1904.11111")

**Dataset -** [https://google.github.io/mannequinchallenge/www/download.html](https://google.github.io/mannequinchallenge/www/download.html "https://google.github.io/mannequinchallenge/www/download.html")