---
layout: post
share: true
title: 'Converting Your Thoughts to Texts: Enabling Brain Typing via Deep Feature
  Learning of EEG Signals (Paper ID: 111)'
author:
  name: Smith Shah
  email: f2016039@pilani.bits-pilani.ac.in
categories:
- CNN
- EEG
- RNN
tags:
- Hard
date: 2019-03-22 00:30:49 +0000

---
**Abstract:** An electroencephalography (EEG) based Brain Computer Interface (BCI) enables people to communicate with the outside world by interpreting the EEG signals of their brains to interact with devices such as wheelchairs and intelligent robots. More specifically, motor imagery EEG (MI-EEG), which reflects a subject’s active intent, is attracting increasing attention for a variety of BCI applications. Accurate classification of MI-EEG signals while essential for effective operation of BCI systems, is challenging due to the significant noise inherent in the signals and the lack of informative correlation between the signals and brain activities. In this paper, we propose a novel deep neural network based learning framework that affords perceptive insights into the relationship between the MI-EEG data and brain activities. We design a joint convolutional recurrent neural network that simultaneously learns robust high-level feature presentations through low-dimensional dense embeddings from raw MI-EEG signals. We also employ an Autoencoder layer to eliminate various artefacts such as background activities. The proposed approach has been evaluated extensively on a large scale public MI-EEG dataset and a limited but easy-to-deploy dataset collected in our lab. The results show that our approach outperforms a series of baselines and the competitive state-of-the art methods, yielding a classification accuracy of 95.53%. The applicability of our proposed approach is further demonstrated with a practical BCI system for typing.

**Paper Link:** [https://arxiv.org/pdf/1709.08820.pdf](https://arxiv.org/pdf/1709.08820.pdf "https://arxiv.org/pdf/1709.08820.pdf")

**Tasks:**

1. Implement RNN and CNN networks as mentioned in Figure 1 of section II of the paper.
2. Implement the autoencoder using the two formulae mentioned on page 4 of the paper.
3. Use any classifier you like as the final layer of the network to classify the EEG streams.
4. Preferably use Torch for implementing the networks.

**ID :** 111
