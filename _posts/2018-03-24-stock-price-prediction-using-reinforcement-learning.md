---
layout: post
share: true
title: Stock Price Prediction Using Reinforcement Learning
date: 2018-03-24 03:38:06 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- Reinforcement Learning
tags:
- Easy
- Application
- Brownie Points
---
**Abstract:** Recently, numerous investigations for stock price prediction and portfolio management using machine learning have been trying to develop efficient mechanical trading systems. But these systems have a limitation in that they are mainly based on the supervised learning which is not so adequate for learning problems with long-term goals and delayed rewards. This paper proposes a method of applying reinforcement learning, suitable for modeling and learning various kinds of interactions in real situations, to the problem of stock price prediction. The stock price prediction problem is considered as Markov process which can be optimized by reinforcement learning based algorithm. TD(0), a reinforcement learning algorithm which learns only from experiences, is adopted and function approximation by an artificial neural network is performed to learn the values of states each of which corresponds to a stock price trend at a given time. An experimental result based on the Korean stock market is presented to evaluate the performance of the proposed method.

**Paper Link:** [http://ieeexplore.ieee.org/document/931880/](http://ieeexplore.ieee.org/document/931880/ "http://ieeexplore.ieee.org/document/931880/")

**Task:** Implement the architecture in python using Tensorflow, Pytorch, MXNet or NumPy. Train the network on [Huge Stock Market Dataset](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs). The submitted code would be checked for similarity with the implementations available online. Show results on Google's historical stock prices.

**Brownie points:** Implement Q-learning or REINFORCE and compare the results.