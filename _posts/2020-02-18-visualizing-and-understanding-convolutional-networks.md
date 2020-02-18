---
layout: post
author:
  name: 'Paper ID: 14'
  email: bitsnnfl@gmail.com
share: true
title: Study on the prediction of stock price based on the associated network model
  of LSTM
categories:
- LSTM
- Financial Time Series
tags: []

---
**Abstract -** Stock market has received widespread attention from investors. It has always been a hot spot for investors and investment companies to grasp the change regularity of the stock market and predict its trend. Currently, there are many methods for stock price prediction. The prediction methods can be roughly divided into two categories: statistical methods and artifcial intelligence methods. Statistical methods include logistic regression model, ARCH model, etc. Artifcial intelligence methods include multi-layer perceptron, convolutional neural network, naive Bayes network, back propagation network, single-layer LSTM, support vector machine, recurrent neural network, etc. But these studies predict only one single value. In order to predict multiple values in one model, it need to design a model which can handle multiple inputs and produces multiple associated output values at the same time. For this purpose, it is proposed an associated deep recurrent neural network model with multiple inputs and multiple outputs based on long short-term memory network. The associated network model can predict the opening price, the lowest price and the highest price of a stock simultaneously. The associated network model was compared with LSTM network model and deep recurrent neural network model. The experiments show that the accuracy of the associated model is superior to the other two models in predicting multiple values at the same time, and its prediction accuracy is over 95%.

Paper: [https://link.springer.com/article/10.1007/s13042-019-01041-1](https://link.springer.com/article/10.1007/s13042-019-01041-1 "https://link.springer.com/article/10.1007/s13042-019-01041-1")

Dataset: [https://www1.nseindia.com/products/content/equities/equities/eq_security.htm](https://www1.nseindia.com/products/content/equities/equities/eq_security.htm "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm")

From Table 2 in paper->For Volume use Total Quantity Traded, For Money use Turnover, For change -> compute change in close price of stock on consecutive days.

Task:

1. Implement the Associated Net model proposed in the paper(3)(4)
2. Experimental analysis in training and testing phase for Associated Network only for any one stock price(5.2)(5.3)

Section of the paper is mentioned for each task