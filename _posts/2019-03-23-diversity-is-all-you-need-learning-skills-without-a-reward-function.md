---
layout: post
share: true
title: 'DIVERSITY IS ALL YOU NEED: LEARNING SKILLS WITHOUT A REWARD FUNCTION (Paper
  ID: 83)'
author:
  name: Sanskriti Sharma
  email: f2015553@pilani.bits-pilani.ac.in
categories:
- Reinforcement Learning
tags: []
date: 2019-03-23 10:08:02 +0000

---
**Abstract:** Intelligent creatures can explore their environments and learn useful skills without supervision. In this paper, we propose “Diversity is All You Need”(DIAYN), a method for learning useful skills without a reward function. Our proposed method learns skills by maximizing an information theoretic objective using a maximum entropy policy. On a variety of simulated robotic tasks, we show that this simple objective results in the unsupervised emergence of diverse skills, such as walking and jumping. In a number of reinforcement learning benchmark environments, our method is able to learn a skill that solves the benchmark task despite never receiving the true task reward. We show how pretrained skills can provide a good parameter initialization for downstream tasks, and can be composed hierarchically to solve complex, sparse reward tasks. Our results suggest that unsupervised discovery of skills can serve as an effective pretraining mechanism for overcoming challenges of exploration and data efficiency in reinforcement learning.

**Paper Link:** [https://arxiv.org/pdf/1802.06070.pdf](https://arxiv.org/pdf/1802.06070.pdf "https://arxiv.org/pdf/1802.06070.pdf")

**ID:** 83

**Guidelines:**

1. Implement the proposed algorithm (Algorithm 1: DIAYN) on any one of the environments mentioned in Appendix C1 or inverted pendulum or mountain car. 
2. Understand the results obtained in section 4.2.1 and depict the same on your chosen environment.
3. Evaluate distribution of task rewards over untrained and trained skills as done in Appendix D3 to ensure that the learned skills are, in fact, not random.