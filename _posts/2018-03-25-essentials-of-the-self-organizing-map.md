---
layout: 'Title: Essentials of the self-organizing map'
share: true
title: Essentials of the self-organizing map
date: 2018-03-25 20:15:43 +0000
author:
  name: Abhishek Lalwani
  email: f2014257@pilani.bits-pilani.ac.in
categories:
- Unsupervised Learning
tags:
- Easy
- Text Data
---
**Abstract:** The self-organizing map (SOM) is an automatic data-analysis method. It is widely applied to clustering problems and data exploration in industry, finance, natural sciences, and linguistics. The most extensive applications, exemplified in this paper, can be found in the management of massive textual databases and in bioinformatics. The SOM is related to the classical vector quantization (VQ), which is used extensively in digital signal processing and transmission. Like in VQ, the SOM represents a distribution of input data items using a finite set of models. In the SOM, however, these models are automatically associated with the nodes of a regular (usually two-dimensional) grid in an orderly fashion such that more similar models become automatically associated with nodes that are adjacent in the grid, whereas less similar models are situated farther away from each other in the grid. This organization, a kind of similarity diagram of the models, makes it possible to obtain an insight into the topographic relationships of data, especially of high-dimensional data items. If the data items belong to certain predetermined classes, the models (and the nodes) can be calibrated according to these classes. An unknown input item is then classified according to that node, the model of which is most similar with it in some metric used in the construction of the SOM. A new finding introduced in this paper is that an input item can even more accurately be represented by a linear mixture of a few best-matching models. This becomes possible by a least-squares fitting procedure where the coefficients in the linear mixture of models are constrained to non-negative values.

**Paper Link:** [https://www.sciencedirect.com/science/article/pii/S0893608012002596](https://www.sciencedirect.com/science/article/pii/S0893608012002596 "https://www.sciencedirect.com/science/article/pii/S0893608012002596")

**Task:**  Implement the SOM of any large textual data set in python using TensorFlow, Numpy, Pytorch or MXNet. An example of such a large dataset can be Encyclopedia Britannica as mentioned in the article number 5.3.2.