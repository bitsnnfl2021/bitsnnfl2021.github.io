---
layout: post
author:
  name: 'Paper ID: 82'
  email: bitsnnfl@gmail.com
share: true
title: 3D Convolutional Neural Networks for Human Action Recognition
categories:
- Action Recognition
- CNN
tags: []

---
**Abstract:** We consider the automated recognition of human actions in surveillance videos. Most current methods build classifiers based on complex handcrafted features computed from the raw inputs. Convolutional neural networks (CNNs) are a type of deep model that can act directly on the raw inputs. However, such models are currently limited to handling 2D inputs. In this paper, we develop a novel 3D CNN model for action recognition. This model extracts features from both the spatial and the temporal dimensions by performing 3D convolutions, thereby capturing the motion information encoded in multiple adjacent frames. The developed model generates multiple channels of information from the input frames, and the final feature representation combines information from all channels. To further boost the performance, we propose regularizing the outputs with high-level features and combining the predictions of a variety of different models. We apply the developed models to recognize human actions in the real-world environment of airport surveillance videos, and they achieve superior performance in comparison to baseline methods

Paper Link: [https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6165309](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6165309 "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6165309")

Conference : IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

**Task:**

1\. Implement the 3D CNN architecture for human recognition as given in Fig. 3.

2\. Implement the three alternative 3D CNN architectures as described in section 4.1.

3\. Present results as given in Table 2 for a minimum of five different class of activities for the architectures designed above.

**Dataset**: Use any human motion database (Eg: HMDB51)

**ID:** 82