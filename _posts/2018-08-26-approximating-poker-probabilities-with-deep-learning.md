---
layout: post
share: true
title: Approximating Poker Probabilities with Deep Learning
date: 2018-08-26 12:01:13 +0530
author:
  name: Rohitkumar Arasanipalai
  email: f2015666@pilani.bits-pilani.ac.in
categories:
- Neural Network
- Monte Carlo Simulations
tags:
- Easy

---
Many poker systems, whether created with heuristics or machine learning, rely on the probability of winning as a key input. However calculating the precise probability using combinatorics is an intractable problem, so instead we approximate it. Monte Carlo simulation is an effective technique that can be used to approximate the probability that a player will win and/or tie a hand. However, without the use of a memory-intensive lookup table or a supercomputer, it becomes infeasible to run millions of times when training an agent with self-play. To combat the space-time tradeoff, we use deep learning to approximate the probabilities obtained from the Monte Carlo simulation with high accuracy. The learned model proves to be a lightweight alternative to Monte Carlo simulation, which ultimately allows us to use the probabilities as inputs during self-play efficiently.

Link: [https://arxiv.org/abs/1808.07220](https://arxiv.org/abs/1808.07220 "https://arxiv.org/abs/1808.07220")

ID: 76