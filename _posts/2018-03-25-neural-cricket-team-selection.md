---
layout: post
share: true
title: Neural Cricket Team Selection
date: 2018-03-25 22:55:00 +0000
author:
  name: Amey Agrawal
  email: agrawalamey12@gmail.com
categories:
- General Deep Learning
tags:
- Easy
- Application
---
**Abstract:** Team selection for international sports competitions requires predicting performance of individual athletes. We explore the use of neural networks to rate players and select specific players for a competition. We take cricket as an example. Cricket is a game with mass following in British Commonwealth Countries as well as some other countries. National teams visit other countries for bilateral matches as well as play in World Cup tournaments. We employ neural networks to predict each cricketer’s performance in the future based upon their past performance. We classify cricketers into three categories – performer, moderate and failure. We collected data on cumulative player performance from 1985 onwards until the 2006–2007 season. The neural network models were progressively trained and tested using four sets of data. The trained neural network models were then applied to generate a forecast of the cricketer’s near term performance. Based on the ratings generated and by applying heuristic rules we recommend cricketers to be included in the World Cup 2007. We evaluate the actual performance of the cricketers in the World Cup to validate the applicability of neural networks. The results show that the neural networks can indeed provide valuable decision support in a team selection process.

**Paper Link:** [https://www.sciencedirect.com/science/article/pii/S095741740800420X](https://www.sciencedirect.com/science/article/pii/S095741740800420X "https://www.sciencedirect.com/science/article/pii/S095741740800420X")

**Task:** Implement the core algorithm in python using Tensorflow, Pytorch, MXNet or NumPy. Train the network using [Indian Premier League dataset](https://www.kaggle.com/harsha547/indian-premier-league-csv-dataset).