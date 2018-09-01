---
layout: post
share: true
title: LONG SHORT-TERM MEMORY
date: 2018-08-24 12:45:18 +0530
author:
  name: Anmol Singhal
  email: f2015069@pilani.bits-pilani.ac.in
categories:
- Basic Architecture
tags:
- Easy

---
Learning to store information over extended time intervals via recurrent backpropagation takes a very long time, mostly due to insufficient, decaying error back ow. We briefly review Hochreiter's 1991 analysis of this problem, then address it by introducing a novel, efficient, gradient-based method called "Long Short-Term Memory" (LSTM). Truncating the gradient where this does not do harm, LSTM can learn to bridge minimal time lags in excess of 1000 discrete time steps by enforcing constant error ow through "constant error carousels" within special units. Multiplicative gate units learn to open and close access to the constant error ow. LSTM is local in space and time; its computational complexity per time step and weight is O(1). Our experiments with artificial data involve local, distributed, real-valued, and noisy pattern representations. In comparisons with RTRL, BPTT, Recurrent Cascade-Correlation, Elman nets, and Neural Sequence Chunking, LSTM leads to many more successful runs, and learns much faster. LSTM also solves complex, articial long time lag tasks that have never been solved by previous recurrent network algorithms.

[Link](http://www.bioinf.jku.at/publications/older/2604.pdf)

ID : 43