---
layout: post
share: true
title: "[ID_21] Learning Convolutional Networks for Content-weighted Image Compression"
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
categories:
- Autoencoders
- Compression
tags: []

---
**Abstract:** Lossy image compression is generally formulated as a joint rate-distortion optimization to learn encoder, quantizer, and decoder. However, the quantizer is non-differentiable, and discrete entropy estimation usually is required for rate control. These make it very challenging to develop a convolutional network (CNN)-based image compression system. In this paper, motivated by that the local information content is spatially variant in an image, we suggest that the bit rate of the different parts of the image should be adapted to local content. And the content aware bit rate is allocated under the guidance of a content-weighted importance map. Thus, the sum of the importance map can serve as a continuous alternative of discrete entropy estimation to control compression rate. And binarizer is adopted to quantize the output of encoder due to the binarization scheme is also directly defined by the importance map. Furthermore, a proxy function is introduced for binary operation in backward propagation to make it differentiable. Therefore, the encoder, decoder, binarizer and importance map can be jointly optimized in an end-to-end manner by using a subset of the ImageNet database. In low bit rate image compression, experiments show that our system significantly outperforms JPEG and JPEG 2000 by structural similarity (SSIM) index, and can produce the much better visual result with sharp edges, rich textures, and fewer artifacts.

Paper Link: [https://arxiv.org/pdf/1703.10553.pdf]()

Conference : CVPR 2018

**Task:**

1\. Implement the autoencoder proposed in the paper without the importance map branch.

2\. The binarizer function is non-differentiable so you will have to write your own forward pass and backward pass for this unit.

3\. Use the gradient pre-processing technique mentioned in the appendix and compare it with the variant which does not use that pre-processing scheme.

4\. Implement either Global averaging cells method or NTM BFGS or NTM L-BFGS on atleast one of the problems mentioned in first point.

**Dataset**
Use any publicly available dataset with high quality images. You may use [Flickr30k ](https://www.kaggle.com/hsankesara/flickr-image-dataset#1001545525.jpg) or [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

**ID:** 21