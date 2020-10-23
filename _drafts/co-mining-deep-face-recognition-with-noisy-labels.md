---
layout: post
author:
  name: Paper ID 98
  difficulty: Hard
share: true
title: 'Co-Mining: Deep Face Recognition with Noisy Labels'
categories:
- CNN
- Noisy Labels
tags: []

---
**Abstract** - Face recognition has achieved significant progress with the growing scale of collected datasets, which empowers us to train strong convolutional neural networks (CNNs). While a variety of CNN architectures and loss functions have been devised recently, we still have a limited under- standing of how to train the CNN models with the label noise inherent in existing face recognition datasets. To address this issue, this paper develops a novel co-mining strategy to effectively train on the datasets with noisy la- bels. Specifically, we simultaneously use the loss val- ues as the cue to detect noisy labels, exchange the high- confidence clean faces to alleviate the errors accumulated issue caused by the sample-selection bias, and re-weight the predicted clean faces to make them dominate the dis- criminative model training in a mini-batch fashion. Ex- tensive experiments by training on three popular datasets (i.e., CASIA-WebFace, MS-Celeb-1M and VggFace2) and testing on several benchmarks, including LFW, CALFW, CPLFW, AgeDB, CFP, RFW, and MegaFace, have demon- strated the effectiveness of our new approach over the state- of-the-art alternatives. Our code is available at http: //www.cbsr.ia.ac.cn/users/xiaobowang/.

**Paper** - [https://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Co-Mining_Deep_Face_Recognition_With_Noisy_Labels_ICCV_2019_paper.pdf](https://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Co-Mining_Deep_Face_Recognition_With_Noisy_Labels_ICCV_2019_paper.pdf "https://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Co-Mining_Deep_Face_Recognition_With_Noisy_Labels_ICCV_2019_paper.pdf")

**Dataset** - [https://drive.google.com/uc?id=1Of_EVz-yHV7QVWQGihYfvtny9Ne8qXVz&export=download](https://drive.google.com/uc?id=1Of_EVz-yHV7QVWQGihYfvtny9Ne8qXVz&export=download "https://drive.google.com/uc?id=1Of_EVz-yHV7QVWQGihYfvtny9Ne8qXVz&export=download") [https://academictorrents.com/details/9e67eb7cc23c9417f39778a8e06cca5e26196a97/tech&hit=1&filelist=1](https://academictorrents.com/details/9e67eb7cc23c9417f39778a8e06cca5e26196a97/tech&hit=1&filelist=1 "https://academictorrents.com/details/9e67eb7cc23c9417f39778a8e06cca5e26196a97/tech&hit=1&filelist=1") [http://www.robots.ox.ac.uk/\~vgg/data/vgg_face2/](http://www.robots.ox.ac.uk/\~vgg/data/vgg_face2/ "http://www.robots.ox.ac.uk/~vgg/data/vgg_face2/")