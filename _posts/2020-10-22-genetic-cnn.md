---
layout: post
author:
  name: Paper ID 76
  difficulty: Medium
share: true
title: Genetic CNN
categories:
- CNN
- Deep Network Structures
tags: []

---
**Abstract** - The deep Convolutional Neural Network (CNN) is the state-of-the-art solution for large-scale visual recognition. Following basic principles such as increasing the depth and constructing highway connections, researchers have manually designed a lot of fixed network structures and verified their effectiveness. In this paper, we discuss the possibility of learning deep network structures automatically. Note that the number of possible network structures increases exponentially with the number of layers in the network, which inspires us to adopt the genetic algorithm to efficiently traverse this large search space. We first propose an encoding method to represent each network structure in a fixed-length binary string, and initialize the genetic algorithm by generating a set of randomized individuals. In each generation, we define standard genetic operations, e.g., selection, mutation and crossover, to eliminate weak individuals and then generate more competitive ones. The competitiveness of each individual is defined as its recognition accuracy, which is obtained via training the network from scratch and evaluating it on a validation set. We run the genetic process on two small datasets, i.e., MNIST and CIFAR10, demonstrating its ability to evolve and find high-quality structures which are little studied before. These structures are also transferrable to the large-scale ILSVRC2012 dataset. 

**Paper** - [https://arxiv.org/pdf/1703.01513v1.pdf](https://arxiv.org/pdf/1703.01513v1.pdf "https://arxiv.org/pdf/1703.01513v1.pdf") 

**Dataset** - [https://www.kaggle.com/oddrationale/mnist-in-csv](https://www.kaggle.com/oddrationale/mnist-in-csv "https://www.kaggle.com/oddrationale/mnist-in-csv")