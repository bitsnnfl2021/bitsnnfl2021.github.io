---
layout: post
author:
  name: Paper ID 34
  difficulty: Medium
share: true
title: DoubleU-Net- A Deep Convolutional NeuralNetwork for Medical Image Segmentation
categories:
- Segmentation
- Computer Vision
- medium

tags: []

---
**Abstract** - Semantic image segmentation is the process of la-beling each pixel of an image with its corresponding class. Anencoder-decoder based approach, like U-Net and its variants, isa popular strategy for solving medical image segmentation tasks.To improve the performance of U-Net on various segmentationtasks, we propose a novel architecture called DoubleU-Net, whichis a combination of two U-Net architectures stacked on top of eachother. The first U-Net uses a pre-trained VGG-19 as the encoder,which has already learned features from ImageNet and can betransferred to another task easily. To capture more semanticinformation efficiently, we added another U-Net at the bottom.We also adopt Atrous Spatial Pyramid Pooling (ASPP) to capturecontextual information within the network. We have evaluatedDoubleU-Net using four medical segmentation datasets, coveringvarious imaging modalities such as colonoscopy, dermoscopy, andmicroscopy. Experiments on the 2015 MICCAI sub-challenge onautomatic polyp detection dataset, the CVC-ClinicDB, the 2018Data Science Bowl challenge, and the Lesion boundary segmen-tation datasets demonstrate that the DoubleU-Net outperformsU-Net and the baseline models. Moreover, DoubleU-Net producesmore accurate segmentation masks, especially in the case of theCVC-ClinicDB and 2015 MICCAI sub-challenge on automaticpolyp detection dataset, which have challenging images such assmaller and flat polyps. These results show the improvementover the existing U-Net model. The encouraging results, pro-duced on various medical image segmentation datasets, showthat DoubleU-Net can be used as a strong baseline for bothmedical image segmentation and cross-dataset evaluation testingto measure the generalizability of Deep Learning (DL) models.Index Terms—semantic segmentation, convolutional neuralnetwork, U-Net, DoubleU-Net, CVC-ClinicDB, ETIS-Larib,ASPP, 2015 MICCAI sub-challenge on automatic polyp detec-tion, 2018 Data Science Bowl, Lesion Boundary Segmentationchallenge

**Paper** - [https://arxiv.org/pdf/2006.04868v2.pdf](https://arxiv.org/pdf/2006.04868v2.pdf)

**Dataset -** [https://polyp.grand-challenge.org/databases/](https://polyp.grand-challenge.org/databases/)
    