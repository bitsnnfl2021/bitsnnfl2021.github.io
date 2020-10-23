---
layout: post
author:
  name: Paper ID 35
  difficulty: Medium
share: true
title: Conditional Image Generation with PixelCNN Decoders
categories:
- Gated Convolutional Layers
- Conditional PixelCNN
tags: []

---
**Abstract** - This work explores conditional image generation with a new image density model based on the PixelCNN architecture. The model can be conditioned on any vector, including descriptive labels or tags, or latent embeddings created by other networks. When conditioned on class labels from the ImageNet database, the model is able to generate diverse, realistic scenes representing distinct animals, objects, landscapes and structures. When conditioned on an embedding produced by a convolutional network given a single image of an unseen face, it generates a variety of new portraits of the same person with different facial expressions, poses and lighting conditions. We also show that conditional PixelCNN can serve as a powerful decoder in an image autoencoder. Additionally, the gated convolutional layers in the proposed model improve the log-likelihood of PixelCNN to match the state-ofthe-art performance of PixelRNN on ImageNet, with greatly reduced computational cost.

**Paper** - [https://papers.nips.cc/paper/6527-conditional-image-generation-with-pixelcnn-decoders.pdf](https://papers.nips.cc/paper/6527-conditional-image-generation-with-pixelcnn-decoders.pdf "https://papers.nips.cc/paper/6527-conditional-image-generation-with-pixelcnn-decoders.pdf")

**Dataset** - [https://github.com/anantzoid/Conditional-PixelCNN-decoder/tree/master/images](https://github.com/anantzoid/Conditional-PixelCNN-decoder/tree/master/images "https://github.com/anantzoid/Conditional-PixelCNN-decoder/tree/master/images")