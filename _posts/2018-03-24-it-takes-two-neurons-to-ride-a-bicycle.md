---
layout: post
share: true
title: It Takes Two Neurons To Ride a Bicycle
date: 2018-03-24 03:35:55 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- Reinforcement Learning
- Robotics
tags:
- Medium
- Application
---
**Abstract:** Past attempts to get computers to ride bicycles have required an inordinate amount of learning time (1700 practice rides for a reinforcement learning approach \[1\], while still failing to be able to ride in a straight line), or have required an algebraic analysis of the exact equations of motion for the specific bicycle to be controlled \[2, 3\]. Mysteriously, humans do not need to do either of these when learning to ride a bicycle. Here we present a two-neuron network1 that can ride a bicycle in a desired direction (for example, towards a desired goal or along a desired path), which may be chosen or changed at run time. Just as when a person rides a bicycle, the network is very accurate for long range goals, but in the short run stability issues dominate the behavior. This happens not by explicit design, but arises as a natural consequence of how the network controls the bicycle.

**Paper Link:** [http://paradise.caltech.edu/cook/papers/TwoNeurons.pdf](http://paradise.caltech.edu/cook/papers/TwoNeurons.pdf "http://paradise.caltech.edu/cook/papers/TwoNeurons.pdf")

**Task:** Implement the architecture in python using Tensorflow, Pytorch, MXNet or NumPy. Create simulations using V-REP motorbike model and python API. Show results on a path similar to figure 5 in paper.