---
layout: post
share: true
title: 'Infrared Colorization Using Deep Convolutional Neural Networks (Paper ID:
  34)'
author:
  name: Abhilash Neog
  email: f2016004@pilani.bits-pilani.ac.in
categories:
- CNN
tags:
- Medium
date: 2019-03-25 09:28:33 +0000

---
**Abstract:** This paper proposes a method for transferring the RGB color spectrum to near-infrared (NIR) images using deep multi-scale convolutional neural networks. A direct and integrated transfer between NIR and RGB pixels is trained. The trained model does not require any user guidance or a reference image database in the recall phase to produce images with a natural appearance. To preserve the rich details of the NIR image, its high frequency features are transferred to the estimated RGB image. The presented approach is trained and evaluated on a real-world dataset containing a large amount of road scene images in summer. The dataset was captured by a multi-CCD NIR/RGB camera, which ensures a perfect pixel to pixel registration.

**Paper Link:** [https://arxiv.org/pdf/1604.02245.pdf](https://arxiv.org/pdf/1604.02245.pdf "https://arxiv.org/pdf/1604.02245.pdf")

**Paper ID: 34**

**Guidelines:**

1. Go through the paper, understand the training technique and the preprocessing involved before feeding an image to the network.
2. Implement the mentioned architecture from the paper with 3 pyramid levels.
3. Train the network on the RGB-NIR Scene Dataset, and test it on your own images. You can also scale down the image size for faster processing.
4. Since you won't be having much computational power, very light colorization of images would also be considered.
