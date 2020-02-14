---
layout: post
author:
  name: Team NNFL
  email: bitsnnfl@gmail.com
share: true
title: "[ID_21] Learning Convolutional Networks for Content-weighted Image Compression"
categories:
- Object Detection
- CNN
tags: []

---
**Abstract:** Lossy image compression is generally formulated as a joint rate-distortion optimization to learn encoder, quantizer, and decoder. However, the quantizer is non-differentiable, and discrete entropy estimation usually is required for rate control. These make it very challenging to develop a convolutional network (CNN)-based image compression system. In this paper, motivated by that the local information content is spatially variant in an image, we suggest that the bit rate of the different parts of the image should be adapted to local content. And the content aware bit rate is allocated under the guidance of a content-weighted importance map. Thus, the sum of the importance map can serve as a continuous alternative of discrete entropy estimation to control compression rate. And binarizer is adopted to quantize the output of encoder due to the binarization scheme is also directly defined by the importance map. Furthermore, a proxy function is introduced for binary operation in backward propagation to make it differentiable. Therefore, the encoder, decoder, binarizer and importance map can be jointly optimized in an end-to-end manner by using a subset of the ImageNet database. In low bit rate image compression, experiments show that our system significantly outperforms JPEG and JPEG 2000 by structural similarity (SSIM) index, and can produce the much better visual result with sharp edges, rich textures, and fewer artifacts.

Paper Link: [https://arxiv.org/pdf/1506.04878.pdf](https://arxiv.org/pdf/1506.04878.pdf "https://arxiv.org/pdf/1506.04878.pdf")

Conference : CVPR 2018

**Task:**

1\. Implement the autoencoder proposed in the paper without the importance map branch and without the binarizer.

2\. Implement the proper dataloader with any 2 data augmentation techniques.

3\. Show reconstructed images and calculate the corresponding PSNR/SSIM metrics.

4\. (Bonus): The binarizer function is non-differentiable so you may choose to write your own forward pass and backward pass for this unit using this [link](https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_custom_function.html). The bonus is just for you to learn more from this project. Do it only if you have time left towards the end.

5\. You can use any framework you want.

**Dataset** Use any publicly available dataset with high quality images. You may use [Flickr30k ](https://www.kaggle.com/hsankesara/flickr-image-dataset#1001545525.jpg) or [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

**ID:** 21