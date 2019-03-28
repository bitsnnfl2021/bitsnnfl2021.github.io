---
layout: post
share: true
title: 'Evolution Strategies as a Scalable Alternative to Reinforcement Learning (Paper
  ID: 66)'
author:
  name: Kabir Ahuja
  email: f2015791@pilani.bits-pilani.ac.in
categories:
- Evolution Strategies
- Reinforcement Learning
tags:
- Medium
date: 2019-03-22 16:33:40 +0000

---
**Abstract**: We explore the use of Evolution Strategies (ES), a class of black box optimization algorithms, as an alternative to popular MDP-based RL techniques such as Qlearning and Policy Gradients. Experiments on MuJoCo and Atari show that ES is a viable solution strategy that scales extremely well with the number of CPUs available: By using a novel communication strategy based on common random numbers, our ES implementation only needs to communicate scalars, making it possible to scale to over a thousand parallel workers. This allows us to solve 3D humanoid walking in 10 minutes and obtain competitive results on most Atari games after one hour of training. In addition, we highlight several advantages of ES as a black box optimization technique: it is invariant to action frequency and delayed rewards, tolerant of extremely long horizons, and does not need temporal discounting or value function approximation.

**Paper Link**: [https://arxiv.org/pdf/1703.03864.pdf](https://arxiv.org/pdf/1703.03864.pdf "https://arxiv.org/pdf/1703.03864.pdf")

**Paper ID: 66**

**Guidelines:**

1. Implement the ES algorithm on CartPole Gym Environment and atleast 1 Mujoco Environment like HalfCheetah, Walker, Hopper etc. (A pain free installation alternative to mujoco is Open AI's Roboschool, which gives the same environments as gym but is much easier to install).
2. Implement both vanilla and parallel versions of the algorithm.
3. Obtain the plots of the total reward with the training iterations as in figure 2 of the paper.