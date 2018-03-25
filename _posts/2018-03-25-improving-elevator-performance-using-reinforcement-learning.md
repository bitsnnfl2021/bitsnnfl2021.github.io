---
layout: post
share: true
title: 'Improving Elevator Performance Using Reinforcement Learning '
date: 2018-03-25 21:06:04 +0000
author:
  name: Abhishek Lalwani
  email: f2014257@pilani.bits-pilani.ac.in
categories:
- Reinforcement Learning
tags:
- Easy
---
**Abstract :** This paper describes the application of reinforcement learning (RL) to the difficult real world problem of elevator dispatching. The elevator domain poses a combination of challenges not seen in most RL research to date. Elevator systems operate in continuous state spaces and in continuous time as discrete event dynamic systems. Their states are not fully observable and they are non-stationary due to changing passenger arrival rates. In addition, we use a team of RL agents, each of which is responsible for controlling one elevator car. The team receives a global reinforcement signal which appears noisy to each agent due to the effects of the actions of the other agents, the random nature of the arrivals and the incomplete observation of the state. In spite of these complications, we show results that in simulation surpass the best of the heuristic elevator control algorithms of which we are aware. These results demonstrate the power of RL on a very large scale stochastic dynamic optimization problem of practical utility. 

**Paper Link :** [https://papers.nips.cc/paper/1073-improving-elevator-performance-using-reinforcement-learning.pdf](https://papers.nips.cc/paper/1073-improving-elevator-performance-using-reinforcement-learning.pdf "https://papers.nips.cc/paper/1073-improving-elevator-performance-using-reinforcement-learning.pdf")

**Task :** Recreate the results of the paper mentioned in python using TensorFlow, Numpy, Pytorch or MXNet