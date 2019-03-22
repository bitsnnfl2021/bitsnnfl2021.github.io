---
layout: post
share: true
title: Training recurrent networks to generate hypotheses about how the brain solves
  hard navigation problems
author:
  name: Achal Agarwal
  email: f2015436@pilani.bits-pilani.ac.in
categories:
- RNN
- Brain
- LSTM
tags:
- Medium
date: 2019-03-19 10:12:06 +0000

---
**Abstract:** Self-localization during navigation with noisy sensors in an ambiguous world is computationally challenging, yet animals and humans excel at it. In robotics, Simultaneous Location and Mapping (SLAM) algorithms solve this problem though joint sequential probabilistic inference of their own coordinates and those of external spatial landmarks. We generate the first neural solution to the SLAM problem by training recurrent LSTM networks to perform a set of hard 2D navigation tasks that include generalization to completely novel trajectories and environments. The hidden unit representations exhibit several key properties of hippocampal place cells, including stable tuning curves that remap between environments. Our result is also a proof of concept for end-to-end-learning of a SLAM algorithm using recurrent networks, and a demonstration of why this approach may have some advantages for robotic SLAM.

**Link to Paper:** [https://arxiv.org/abs/1609.09059](https://arxiv.org/abs/1609.09059 "Link to Paper")

**ID:** 15

**Restrictions:** None

**Advice:** Designing the environment might not be trivial, keep it as simple as possible.

**Dataset:** Self-Developed Environment

**Requirements**:

1. Build the network as specified in Section 2.3
2. Implement the random environment as explained in Section 2.1
3. Perform experiments on your network in accordance with Sections 3.1.1 and 3.1.2. 
4. Modify the environment in 2. to incorporate a 100% error in distance and relative angle with a probability of 0.01 on boundary contact.
5. Perform experiments with the new environment as carried out in 3.