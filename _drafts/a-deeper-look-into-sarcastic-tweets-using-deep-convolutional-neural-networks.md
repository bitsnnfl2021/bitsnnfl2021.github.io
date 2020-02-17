---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_42] A Deeper Look into Sarcastic Tweets Using Deep Convolutional Neural
  Networks"
categories:
- Natural Language Processing
tags:
- CNN
- Text Convolutions
- Sarcasm Detection

---

# A Deeper Look into Sarcastic Tweets Using Deep Convolutional Neural Networks

Abstract: Sarcasm detection is a key task for many natural language processing tasks. In sentiment analysis, for example, sarcasm can flip the polarity of an “apparently positive” sentence and, hence, negatively affect polarity detection performance. To date, most approaches to sarcasm detection have treated the task primarily as a text categorization problem. Sarcasm, however, can be expressed in very subtle ways and requires a deeper understanding of natural language that standard text categorization techniques cannot grasp. In this work, we develop models based on a pre-trained convolutional neural network for extracting sentiment, emotion and personality features for sarcasm detection. Such features, along with the network’s baseline features, allow the proposed models to outperform the state of the art on benchmark datasets. We also address the often ignored generalizability issue of classifying data that have not been seen by the models at the learning phase

Paper Link: [https://sentic.net/sarcasm-detection-with-deep-convolutional-neural-networks.pdf](https://sentic.net/sarcasm-detection-with-deep-convolutional-neural-networks.pdf "https://sentic.net/sarcasm-detection-with-deep-convolutional-neural-networks.pdf")

Sentiment Dataset: [IMDB Movie Reviews](https://www.kaggle.com/iarunava/imdb-movie-reviews-dataset)

Personality Dataset: [OCEAN](https://drive.google.com/file/d/1xTg5iJZzzNEf3jJJKhBpgwkMnYDHaKQJ/view?usp=sharing)

Test Dataset: [Amazon Review Dataset](https://github.com/ef2020/SarcasmAmazonReviewsCorpus)

Task: Broadly you will have to create a model that is able to detect sarcasm in customer product reviews.

1. Create the model mentioned in Pytorch. You may refer to [this](https://ieeexplore.ieee.org/document/7887639) and [this](https://web.stanford.edu/class/cs224n/slides/cs224n-2019-lecture11-convnets.pdf) to understand more about the model.
2. Train your model for sentiment analysis on IMDB dataset
3. Train your model for personality identification on OCEAN dataset
4. Use the models in (2) and (3) and then train an SVM on their predictions to make the final prediction as mentioned in the paper.