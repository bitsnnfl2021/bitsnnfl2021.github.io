---
layout: post
author:
  name: Paper ID 44
  difficulty: Hard
share: true
title: Dueling Network Architectures for Deep Reinforcement Learning
categories:
- Reinforcement Learning
- Deep Q Networks
- Atari Environment
tags: []

---
**Abstract** - In recent years there have been many successes of using deep representations in reinforcement learning. Still, many of these applications use conventional architectures, such as convolutional networks, LSTMs, or auto-encoders. In this paper, we present a new neural network architecture for model-free reinforcement learning. Our dueling network represents two separate estimators: one for the state value function and one for the state-dependent action advantage function. The main benefit of this factoring is to generalize learning across actions without imposing any change to the underlying reinforcement learning algorithm. Our results show that this architecture leads to better policy evaluation in the presence of many similar-valued actions. Moreover, the dueling architecture enables our RL agent to outperform the state-of-the-art on the Atari 2600 domain. 

**Paper** - [https://arxiv.org/abs/1511.06581](https://arxiv.org/abs/1511.06581 "https://arxiv.org/abs/1511.06581") 

**Dataset** - OpenAI Gym