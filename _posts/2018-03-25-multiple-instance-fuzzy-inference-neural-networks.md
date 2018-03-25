---
layout: post
share: true
title: 'Multiple Instance Fuzzy Inference Neural Networks '
date: 2018-03-25 21:36:51 +0000
author:
  name: Kabir Ahuja
  email: kabirahuja2431@gmail.com
categories:
- Fuzzy Logic
tags:
- Hard
- Application
---
**Abstract:** Fuzzy logic is a powerful tool to model knowledge uncertainty, measurements imprecision, and vagueness. However, there is another type of vagueness that arises when data have multiple forms of expression that fuzzy logic does not address quite well. This is the case for multiple instance learning problems (MIL). In MIL, an object is represented by a collection of instances, called a bag. A bag is labeled negative if all of its instances are negative, and positive if at least one of its instances is positive. Positive bags encode ambiguity since the instances themselves are not labeled. In this paper, we introduce fuzzy inference systems and neural networks designed to handle bags of instances as input and capable of learning from ambiguously labeled data. First, we introduce the Multiple Instance Sugeno style fuzzy inference (MI-Sugeno) that extends the standard Sugeno style inference to handle reasoning with multiple instances. Second, we use MI-Sugeno to define and develop Multiple Instance Adaptive Neuro Fuzzy Inference System (MI-ANFIS). We expand the architecture of the standard ANFIS to allow reasoning with bags and derive a learning algorithm using backpropagation to identify the premise and consequent parameters of the network. The proposed inference system is tested and validated using synthetic and benchmark datasets suitable for MIL problems. We also apply the proposed MI-ANFIS to fuse the output of multiple discrimination algorithms for the purpose of landmine detection using Ground Penetrating Radar.

**Paper Link:** [https://arxiv.org/pdf/1610.04973.pdf](https://arxiv.org/pdf/1610.04973.pdf "Arxiv")

**Tasks:** 

1. Implement the complete algorithm
2. Test it on different datasets mentioned in the paper
3. Make a report on the work done