---
layout: post
author:
  name: 'Paper ID: 91'
  email: bitsnnfl@gmail.com
share: true
title: Hand Gesture Recognition Using an Adapted Convolutional Neural Network with
  Data Augmentation
categories:
- Gesture Recognition
- CNN
tags: []

---
**Abstract** - Hand gestures provide a natural way for humans to interact with computers to perform a variety of different applications. However, factors such as the complexity of hand gesture structures, differences in hand size, hand posture, and environmental illumination can influence the performance of hand gesture recognition algorithms. Recent advances in Deep Learning have significantly advanced the performance of image recognition systems. In particular, the Deep Convolutional Neural Network has demonstrated superior performance in image representation and classification, compared to conventional machine learning approaches. This paper proposes an Adapted Deep Convolutional Neural Network (ADCNN) suitable for hand gesture recognition tasks. Data augmentation is initially applied which shifts images both horizontally and vertically to an extent of 20% of the original dimensions randomly, in order to numerically increase the size of the dataset and to add the robustness needed for a deep learning approach. These images are input into the proposed ADCNN model which is empowered by the presence of network initialization (ReLU and Softmax) and L2 Regularization to eliminate the problem of data overfitting. With these modifications, the experimental results using the ADCNN model demonstrate that it is an effective method of increasing the performance of CNN for hand gesture recognition. The model was trained and tested using 3750 static hand gesture images, which incorporate variations in features such as scale, rotation, translation, illumination, and noise. The proposed ADCNN was compared to a baseline Convolutional Neural Network and the results show that the proposed ADCNN achieved a classification recognition accuracy of 99.73% and a 4% improvement over the baseline Convolutional Neural Network model (95.73%).

**Paper** - [https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8392660](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8392660 "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8392660")

**Dataset:** [https://www.kaggle.com/grassknoted/asl-alphabet](https://www.kaggle.com/grassknoted/asl-alphabet "https://www.kaggle.com/grassknoted/asl-alphabet")

**Problem Statement:**

1. The paper is based on Peru sign language. Implement it for the American Sign language using the above dataset. Split the training set into 2700 and 300 for each case. Train Using 2700 samples and test on 300 samples, along with the test data. Clearly report the number of data samples of each category in training and testing sets by generating necessary graphs in the notebook. Submit the final dataset used for the project along with the notebook.
2. Use Keras API of Tensorflow to implement the model as in the paper
3. Train the model on ADCNN and baseline CNN after necessary data augmentation as given in the paper
4. Report the graph of the loss function & accuracy vs. epochs for training data, and confusion matrix, precision, recall, F1 score and accuracy of the model for the test case (in the notebook) for both the models.