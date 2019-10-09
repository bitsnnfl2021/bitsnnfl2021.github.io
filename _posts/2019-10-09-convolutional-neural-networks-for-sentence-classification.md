---
layout: post
share: true
title: 'Convolutional Neural Networks for Sentence Classification (Paper ID: 65)'
author:
  name: Parth Patel
  email: f2016150@pilani.bits-pilani.ac.in
categories:
- CNN
- NLP
tags:
- Easy
date: 2019-10-09 10:44:03 +0000

---
**Abstract:** We report on a series of experiments with convolutional neural networks (CNN) trained on top of pre-trained word vectors for sentence-level classification tasks. We show that a simple CNN with little hyperparameter tuning and static vectors achieves excellent results on multiple benchmarks. Learning task-specific vectors through fine-tuning offers further gains in performance. We additionally propose a simple modification to the architecture to allow for the use of both task-specific and static vectors. The CNN models discussed herein improve upon the state of the art on 4 out of 7 tasks, which include sentiment analysis and question classification.

**Paper Link:** [https://arxiv.org/pdf/1408.5882.pdf](https://arxiv.org/pdf/1408.5882.pdf)

**Paper ID: 65**

**Guidelines**:

1\. Implement the following 3 model variants as given in setion 3.3: CNN-static, CNN-non-static and CNN-multichannel.

2\. Compare the performance of the above 3 models in terms of accuracy by training on TREC question dataset [https://cogcomp.seas.upenn.edu/Data/QA/QC/train_5500.label](https://cogcomp.seas.upenn.edu/Data/QA/QC/train_5500.label), mentioned in section 3 of the paper.

3\. As a sanity check train on 50 sentences first and see if the model can overfit i.e get close to 100% accuracy on those 50 sentences.

4\. Also train a baseline model which averages word vectors of all the words in the sentence and train a single layer neural network on the obtained vector to classify the sentence. Compare its performance with your cnn models. The accuracy obtained by your models should be more than this baseline.

**Side Note:** Just in case you are curious to know how the word vectors are trained in an unsupervised manner for _word2vec_, visit [http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/).
