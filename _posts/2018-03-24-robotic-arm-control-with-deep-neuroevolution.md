---
layout: post
share: true
title: Robotic Arm Control With Deep Neuroevolution
date: 2018-03-24 03:28:46 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- Neural Evolution
- Robotics
tags:
- Hard
- Application
- Theory
---
**Abstract:** Deep artificial neural networks (DNNs) are typically trained via gradient-based learning algorithms, namely backpropagation. Evolution strategies (ES) can rival backprop-based algorithms such as Q-learning and policy gradients on challenging deep reinforcement learning (RL) problems. However, ES can be considered a gradient-based algorithm because it performs stochastic gradient descent via an operation similar to a finite-difference approximation of the gradient. That raises the question of whether non-gradient-based evolutionary algorithms can work at DNN scales. Here we demonstrate they can: we evolve the weights of a DNN with a simple, gradient-free, population-based genetic algorithm (GA) and it performs well on hard deep RL problems, including Atari and humanoid locomotion. The Deep GA successfully evolves networks with over four million free parameters, the largest neural networks ever evolved with a traditional evolutionary algorithm. These results (1) expand our sense of the scale at which GAs can operate, (2) suggest intriguingly that in some cases following the gradient is not the best choice for optimizing performance, and (3) make immediately available the multitude of techniques that have been developed in the neuroevolution community to improve performance on RL problems. To demonstrate the latter, we show that combining DNNs with novelty search, which was designed to encourage exploration on tasks with deceptive or sparse reward functions, can solve a high-dimensional problem on which reward-maximizing algorithms (e.g. DQN, A3C, ES, and the GA) fail. Additionally, the Deep GA parallelizes better than ES, A3C, and DQN, and enables a state-of-the-art compact encoding technique that can represent million-parameter DNNs in thousands of bytes.

**Paper Link:** [https://arxiv.org/pdf/1712.06567.pdf](https://arxiv.org/pdf/1712.06567.pdf "https://arxiv.org/pdf/1712.06567.pdf")

**Task:** Implement the core algorithm in python using Tensorflow, Pytorch, MXNet or NumPy. The submitted code would be checked for similarity with the implementations available online. Train the network on [FetchPush-v0](https://gym.openai.com/envs/FetchPush-v0) and [HandManipulateBlock-v0](https://gym.openai.com/envs/HandManipulateBlock-v0) and compare results with Q-learning.