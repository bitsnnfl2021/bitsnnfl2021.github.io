---
layout: post
share: true
title: 'Overcoming Blind Spots in the Real World: Leveraging Complementary Abilities for Joint Execution (Paper ID: 154)'
author:
  name: Saksham Consul
  email: f2016424@pilani.bits-pilani.ac.in
categories:
- Reinforcement Learning
tags:
- Medium
date: 2019-10-09 13:47:49 +0000

---
**Abstract:** Simulators are being increasingly used to train agents before deploying them in real-world environments. While training in simulation provides a cost-effective way to learn, poorly modeled aspects of the simulator can lead to costly mistakes, or blind spots. While humans can help guide an agent towards identifying these error regions, humans themselves have blind spots and noise in execution. We study how learning about blind spots of both can be used to manage hand-off decisions when humans and agents jointly act in the real-world in which neither of them are trained or evaluated fully. The formulation assumes that agent blind spots result from representational limitations in the simulation world, which leads the agent to ignore important features that are relevant for acting in the open world. Our approach for blind spot discovery combines experiences collected in simulation with limited human demonstrations. The first step applies imitation learning to demonstration data to identify important features that the human is using but that the agent is missing. The second step uses noisy labels extracted from action mismatches between the agent and the human across simulation and demonstration data to train blind spot models. We show through experiments on two domains that our approach is able to learn a succinct representation that accurately captures blind spot regions and avoids dangerous errors in the real world through transfer of control between the agent and the human.

**Paper Link:** [https://www.aaai.org/ojs/index.php/AAAI/article/view/4571/4449](https://www.aaai.org/ojs/index.php/AAAI/article/view/4571/4449)

**ID:** 154

**Guidelines:**

Very well written paper. Implement the paper. You can choose any game environment but discuss with me before selection.

