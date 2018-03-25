---
layout: post
share: true
title: Predicting Flight Ticket Prices
date: 2018-03-25 23:17:59 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories: []
tags: []
---
**Abstract:** Machine learning has been used in all kinds of fields. In this article, we introduce how machine learning can be applied into time series problem. Especially, we use the airline ticket prediction problem as our specific problem. Airline companies use many different variables to determine the flight ticket prices: indicator whether the travel is during the holidays, the number of free seats in the plane etc. Some of the variables are observed, but some of them are hidden. Based on the data over a 103 day period, we trained our models, getting the best model - which is AdaBoost-Decision Tree Classification. This algorithm has best performance over the observed 8 routes which has 61.35% better performance than the random purchase strategy, and relatively small variance over these routes. And we also considered the situation that we cannot get too much historical datas for some routes (for example the route is new and does not have historical data) or we do not want to train historical data to predict to buy or wait quickly, in which problem, we used HMM Sequence Classification based AdaBoost-Decision Tree Classification to perform our prediction on 12 new routes. Finally, we got 31.71% better performance than the random purchase strategy.

**Paper Link:** [https://arxiv.org/pdf/1705.07205.pdf](https://arxiv.org/pdf/1705.07205.pdf "https://arxiv.org/pdf/1705.07205.pdf")

**Task:** Implement the architecture in python using Tensorflow, Pytorch, MXNet or NumPy. Train the network on [DB1BTicket dataset](https://www.transtats.bts.gov/DL_SelectFields.asp). 