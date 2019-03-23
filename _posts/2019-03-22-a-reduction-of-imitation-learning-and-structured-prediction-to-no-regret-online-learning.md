---
layout: post
share: true
title: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online
  Learning
author:
  name: Kabir Ahuja
  email: f2015791@pilani.bits-pilani.ac.in
categories:
- Imitation Learning
tags:
- Easy
date: 2019-03-22 16:46:04 +0000

---
**Abstract:** Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning. This leads to poor performance in theory and often in practice. Some recent approaches (Daumé III et al., 2009; Ross and Bagnell, 2010) provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train either non-stationary or stochastic policies and require a large number of iterations. In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting. We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings. We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.

**Paper Link:** [https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf](https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf "https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf")

**Paper ID: 67**

**Useful Links:** You can use the expert policies given here [https://github.com/berkeleydeeprlcourse/homework/tree/master/hw1](https://github.com/berkeleydeeprlcourse/homework/tree/master/hw1 "https://github.com/berkeleydeeprlcourse/homework/tree/master/hw1") to run your experiments. The expert policies for the experiments in the paper are not made public, hence you should use the expert policies from the link.

**Guidelines:**

1. Implement the Dataset Aggregation algorithm (DAGGER) as given in section 3 to train policies on atleast 2 of the experts from the useful links.
2. After you have trained your policies using DAGGER demonstrate how these policies perform on these environments by comparing the total reward achieved by your policy with the total reward by the expert policy.